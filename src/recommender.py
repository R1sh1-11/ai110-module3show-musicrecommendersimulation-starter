from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """Represents a song and its attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """Represents a user's taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """OOP implementation of the recommendation logic."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k recommended songs for a user profile."""
        scored = []
        for song in self.songs:
            # Convert Song dataclass to dict for score_song
            song_dict = {
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "acousticness": song.acousticness,
                "title": song.title,
                "artist": song.artist,
            }
            user_dict = {
                "genre": user.favorite_genre,
                "mood": user.favorite_mood,
                "energy": user.target_energy,
                "likes_acoustic": user.likes_acoustic,
            }
            score, reasons = score_song(user_dict, song_dict)
            scored.append((song, score, reasons))

        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, score, reasons in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explains why a song was recommended for a given user profile."""
        song_dict = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "acousticness": song.acousticness,
            "title": song.title,
            "artist": song.artist,
        }
        user_dict = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        score, reasons = score_song(user_dict, song_dict)
        return f"Score: {score:.2f} — " + "; ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns a list of dictionaries."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields from strings to proper types
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences using the Algorithm Recipe."""
    score = 0.0
    reasons = []

    # Genre match: +2.0 points
    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 2.0
        reasons.append(f"Genre match: {song['genre']} (+2.0)")

    # Mood match: +1.0 point
    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1.0
        reasons.append(f"Mood match: {song['mood']} (+1.0)")

    # Energy similarity: up to +1.0 (closer to user's target = higher score)
    energy_diff = abs(song["energy"] - user_prefs["energy"])
    energy_score = round(1.0 - energy_diff, 2)
    score += energy_score
    reasons.append(f"Energy similarity: {energy_score:.2f} (+{energy_score:.2f})")

    # Acoustic bonus: +0.5 if user likes acoustic and song is acoustic
    if user_prefs.get("likes_acoustic") and song["acousticness"] > 0.7:
        score += 0.5
        reasons.append(f"Acoustic bonus: acousticness {song['acousticness']:.2f} (+0.5)")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Ranks all songs by score and returns the top k with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    # Sort by score descending — sorted() returns a new list, leaving original intact
    scored_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)

    return scored_songs[:k]