# 🎵 Music Recommender Simulation

## Project Summary

WaveTune is a content-based music recommender system that analyzes song features and user preferences to generate personalized recommendations. The system represents songs using attributes such as genre, mood, energy, tempo, valence, danceability, and acousticness.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - Each song uses features that describe its overall music traits, and its vibe, and they are:
    - genres, tempo, mood, energy, tempo_bpm, valence, danceability, acousticness
- What information does your `UserProfile` store
  - The UserProfile stores information about the user's musical preferences, which include the preffered genres, tempo, mood, energy, tempo_bpm, valence, danceability, acousticness. The profile acts as a representation of the user's personal musical taste
- How does your `Recommender` compute a score for each song
  - The Recommender calculates a score by comparing each song's features with the user's preferences.
  - For categorical features like genre and mood, the system gives points when the song matches the user's preferences. and for numerical features like energy, tempo, and valence, the system calculates how close the song's value is to the user's preferred value.
- How do you choose which songs to recommend
  - The recommender calculates an overall score for every song in the dataset. After scoring all songs, it sorts them from the highest score to the lowest.

**Possible Biases:**   It could over-prioritize certain features, such as genre, causing it to recommend songs that are similar in category but may not match the user's actual mood or preferences.

<!-- You can include a simple diagram or bullet list if helpful. -->

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

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
========================================
       TOP MUSIC RECOMMENDATIONS
========================================

#1: Sunrise City
Artist: Neon Echo
Genre: pop | Mood: happy
Score: 4.80
Reasons:
  ✓ Genre matches preference (+2.0)
  ✓ Mood matches preference (+1.0)
  ✓ Energy similarity score (+0.98)
  ✓ Non-acoustic preference score (+0.82)

#2: Gym Hero
Artist: Max Pulse
Genre: pop | Mood: intense
Score: 3.82
Reasons:
  ✓ Genre matches preference (+2.0)
  ✓ Energy similarity score (+0.87)
  ✓ Non-acoustic preference score (+0.95)

#3: Rooftop Lights
Artist: Indigo Parade
Genre: indie pop | Mood: happy
Score: 2.61
Reasons:
  ✓ Mood matches preference (+1.0)
  ✓ Energy similarity score (+0.96)
  ✓ Non-acoustic preference score (+0.65)

#4: Neon Dreams
Artist: Pixel Mirage
Genre: electronic | Mood: excited
Score: 1.80
Reasons:
  ✓ Energy similarity score (+0.92)
  ✓ Non-acoustic preference score (+0.88)

#5: After the Storm
Artist: Echo Valley
Genre: metal | Mood: powerful
Score: 1.80
Reasons:
  ✓ Energy similarity score (+0.86)
  ✓ Non-acoustic preference score (+0.94)

========================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried
- Changing the genre weight from 2.0 to 0.5: Reducing the genre weight caused the recommender to rely less on matching a user's favorite genre and focus more on other musical characteristics.

- Adding tempo and valence to the scoring system: allowed the recommender to consider more aspects of a song's style. 

- Testing different user profiles: profiles such as High-Energy Pop, Chill Lofi, and Deep Intense Rock users

---

## Limitations and Risks

The recommender only works with a small music catalog, which limits the variety and accuracy of recommendations.

The system only analyzes structured song features such as genre, mood, energy, tempo, valence, danceability, and acousticness. It does not understand lyrics, themes, cultural context, or the personal meaning a song may have to a listener.

The scoring system may over-prioritize certain features, such as genre, causing songs from a user's favorite genre to dominate recommendations.

The system may create a filter bubble by repeatedly recommending songs with similar characteristics and reducing exposure to new genres or styles.

---

## Reflection


Reflection is in [**Model Card**](model_card.md)