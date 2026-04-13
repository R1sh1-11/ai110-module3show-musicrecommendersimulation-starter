"""
Command line runner for the Music Recommender Simulation.
"""

from recommender import load_songs, recommend_songs


def print_recommendations(profile_name, user_prefs, songs, k=5):
    """Prints formatted recommendations for a given user profile."""
    print(f"\n{'='*50}")
    print(f"  Profile: {profile_name}")
    print(f"  Prefs: {user_prefs}")
    print(f"{'='*50}\n")

    recommendations = recommend_songs(user_prefs, songs, k=k)

    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"  #{i} {song['title']} by {song['artist']} — Score: {score:.2f}")
        print(f"     Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Profile 1: Happy Pop Fan
    profile_1 = {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False}
    print_recommendations("Happy Pop Fan", profile_1, songs)

    # Profile 2: Chill Lofi Listener
    profile_2 = {"genre": "lofi", "mood": "chill", "energy": 0.4, "likes_acoustic": True}
    print_recommendations("Chill Lofi Listener", profile_2, songs)

    # Profile 3: Intense Rock Lover
    profile_3 = {"genre": "rock", "mood": "intense", "energy": 0.9, "likes_acoustic": False}
    print_recommendations("Intense Rock Lover", profile_3, songs)

    # Edge Case 1: Conflicting preferences (high energy but sad mood)
    profile_4 = {"genre": "pop", "mood": "melancholy", "energy": 0.95, "likes_acoustic": False}
    print_recommendations("Sad But Energetic (Edge Case)", profile_4, songs)

    # Edge Case 2: Preferences that barely match anything in the catalog
    profile_5 = {"genre": "classical", "mood": "relaxed", "energy": 0.2, "likes_acoustic": True}
    print_recommendations("Quiet Classical Fan (Edge Case)", profile_5, songs)


if __name__ == "__main__":
    main()