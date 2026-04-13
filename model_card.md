# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  : AtTUNEment

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
  It generates a ranked list of the top 5 songs from a small catalog based on how well they match a user's taste profile.

- What assumptions does it make about the user  
  It assumes the user cares most about genre, then mood, then energy level and that these preferences don't change over time.

- Is this for real users or classroom exploration  
  This is for classroom exploration only, not for real users or production use.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
  The system looks at genre, mood, energy, and acousticness for each song.

- What user preferences are considered  
  The user provides their favorite genre, preferred mood, a target energy level (0.0–1.0), and whether they like acoustic music.

- How does the model turn those into a score  
  It awards +2.0 points for a genre match, +1.0 for a mood match, up to +1.0 based on how close the song's energy is to the user's target, and +0.5 if the user likes acoustic and the song's acousticness is above 0.7. All points are added up into a final score.

- What changes did you make from the starter logic  
  The starter code had empty TODO functions. I implemented the full scoring recipe with weighted points and added explanation strings so each recommendation shows why it was picked.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
  18 songs total.

- What genres or moods are represented  
  Genres include pop, lofi, rock, ambient, jazz, synthwave, indie pop, r&b, edm, folk, hip-hop, classical, world, and indie rock. Moods include happy, chill, intense, focused, relaxed, moody, romantic, melancholy, and aggressive.

- Did you add or remove data  
  I added 8 songs to the original 10 to cover genres and moods that were missing from the starter dataset.

- Are there parts of musical taste missing in the dataset  
  Yes. There's no country, metal, reggae, or Latin music, and most genres only have one or two songs, which limits variety.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
  Users with clear, specific tastes like "chill lofi" or "intense rock" get strong results with high-confidence scores.

- Any patterns you think your scoring captures correctly  
  The energy similarity formula rewards songs that are close to the user's target rather than just high-energy songs, which feels fair.

- Cases where the recommendations matched your intuition  
  The Chill Lofi Listener got Midnight Coding and Library Rain as top picks, which genuinely feels like what Spotify would suggest for that vibe.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
  Tempo, valence, and danceability are in the CSV but never used in scoring, so the system ignores potentially useful information.

- Genres or moods that are underrepresented  
  Rock, classical, folk, and several other genres only have one song each, so users who prefer those genres get almost no variety.

- Cases where the system overfits to one preference  
  Genre carries +2.0 points, which means a song in the "right" genre can beat a perfect mood and energy match in the "wrong" genre. Gym Hero ranked #2 for Happy Pop Fan even though its mood is "intense," not "happy."

- Ways the scoring might unintentionally favor some users  
  Users who like lofi get three songs to choose from while users who like classical only get one, so the system gives better results to some tastes purely because of dataset size.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
  Five profiles: Happy Pop Fan, Chill Lofi Listener, Intense Rock Lover, Sad But Energetic (edge case), and Quiet Classical Fan (edge case).

- What you looked for in the recommendations  
  Whether the top results matched the user's stated preferences and whether the scores and explanations made logical sense.

- What surprised you  
  The "Sad But Energetic" profile completely ignored the melancholy mood because the only melancholy song had low energy and the system just fell back to genre and energy matching.

- Any simple tests or comparisons you ran  
  I ran a weight experiment where I halved the genre weight (2.0 - 1.0) and doubled the energy weight (1.0 - 2.0). This caused Rooftop Lights to jump above Gym Hero for the Pop Fan, showing the rankings are very sensitive to weight changes.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
  Add valence, danceability, and tempo into the scoring so the system understands songs more deeply.

- Better ways to explain recommendations  
  Show users what they're missing — like "You might also like this song even though it's a different genre, because the mood and energy are a perfect match."

- Improving diversity among the top results  
  Add a diversity penalty so the top 5 can't all be from the same artist or genre.

- Handling more complex user tastes  
  Let users set their own weights for how much genre, mood, and energy matter to them instead of using fixed values.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
  Even a simple algorithm with just four rules can produce recommendations that actually feel right, which made me realize real apps are doing the same thing at a much bigger scale.

- Something unexpected or interesting you discovered  
  The edge case testing showed how easily the system breaks when preferences contradict each other/it just silently ignores the parts it can't satisfy.

- How this changed the way you think about music recommendation apps  
  I now think about what data Spotify is actually using when it suggests a song, and I realize there are probably hundreds of features and weights behind every recommendation, not just genre and mood.