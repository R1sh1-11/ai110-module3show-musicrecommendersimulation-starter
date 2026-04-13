# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real music platforms like Spotify use two main approaches to recommend songs. Collaborative filtering looks at what similar users listened to, like if someone with your exact taste loved a song, you probably will too. Content-based filtering looks at the actual attributes of songs you already like (genre, energy, tempo) and finds other songs with similar attributes. My system uses a simplified content-based approach since we don't have other users, it will be just one user profile matched against song features.

Song features used: genre, mood, energy, tempo_bpm, valence, danceability, acousticness
UserProfile stores: favorite genre, favorite mood, target energy level, and whether the user prefers acoustic songs
Scoring logic (Algorithm Recipe):

+2.0 points for a genre match (strongest signal)
+1.0 points for a mood match
Up to +1.0 points for energy similarity (closer to the user's target = higher score)
+0.5 bonus if the user likes acoustic music and the song's acousticness is above 0.7

The system scores every song individually (the "Scoring Rule"), then sorts all scores from highest to lowest and returns the top K results (the "Ranking Rule"). Each recommendation includes the reasons it scored well, so the user can understand why a song was suggested.

Dataset:
The song catalog contains 18 songs across 10+ genres including pop, lofi, rock, ambient, jazz, synthwave, indie pop, r&b, edm, folk, hip-hop, classical, world, and indie rock. Moods range from happy and chill to intense, melancholy, aggressive, and romantic. All numerical features (energy, valence, danceability, acousticness) are on a 0.0–1.0 scale, and tempo is in BPM.
User Profile Structure:
Each user profile is a dictionary with four keys:

genre — the user's favorite genre (string)
mood — the user's preferred mood (string)
energy — target energy level from 0.0 to 1.0 (float)
likes_acoustic — whether the user prefers acoustic sounds (boolean)

Potential Biases:
This system will likely over-prioritize genre since it carries the heaviest weight (+2.0). A great song that matches a user's mood and energy perfectly but is in the "wrong" genre would score lower than a mediocre genre match. The dataset is also small enough that some genres only have one song, meaning those users get very limited recommendations.

- System Mechanisms created with Claude

## Terminal Output

### Profile 1: Happy Pop Fan
![alt text](image.png)

### Profile 2: Chill Lofi Listener
![alt text](image-1.png)

### Profile 3: Intense Rock Lover
![alt text](image-2.png)

### Profile 4: Edge Case 1
![alt text](image-3.png)

### Profile 5: Edge Case 2
![alt text](image-4.png)

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

