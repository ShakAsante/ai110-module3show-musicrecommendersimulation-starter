from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.

    Attributes:
        id (int): Unique identifier for the song.
        title (str): Name of the song.
        artist (str): Artist who created the song.
        genre (str): Genre category of the song.
        mood (str): Emotional tone of the song.
        energy (float): Energy level of the song from 0.0 to 1.0.
        tempo_bpm (float): Tempo of the song measured in beats per minute.
        valence (float): Positivity/happiness level of the song from 0.0 to 1.0.
        danceability (float): How suitable the song is for dancing from 0.0 to 1.0.
        acousticness (float): Amount of acoustic elements from 0.0 to 1.0.

    Required by:
        tests/test_recommender.py
    """

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
    """
    Represents a user's music preferences.

    Attributes:
        favorite_genre (str): User's preferred music genre.
        favorite_mood (str): User's preferred song mood.
        target_energy (float): Desired energy level from 0.0 to 1.0.
        likes_acoustic (bool): Whether the user prefers acoustic songs.

    Required by:
        tests/test_recommender.py
    """

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    Object-oriented implementation of the recommendation system.

    Stores a song catalog and provides methods for generating
    recommendations and explaining recommendation results.

    Required by:
        tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        """
        Initializes the recommender with a list of available songs.

        Args:
            songs (List[Song]): Collection of songs available for recommendation.
        """
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """
        Returns the top k recommended songs for a user.

        Args:
            user (UserProfile): User preference profile.
            k (int): Number of recommendations to return.

        Returns:
            List[Song]: Recommended songs ranked by similarity.
        """
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """
        Generates an explanation for why a song was recommended.

        Args:
            user (UserProfile): User preference profile.
            song (Song): Song being explained.

        Returns:
            str: Explanation describing matching features.
        """
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file and converts them into dictionaries.

    The CSV file must contain the following columns:
        id, title, artist, genre, mood, energy,
        tempo_bpm, valence, danceability, acousticness

    Numeric values are converted into their appropriate types.

    Args:
        csv_path (str): Path to the songs CSV file.

    Returns:
        List[Dict]: List of songs represented as dictionaries.

    Example:
        [
            {
                "id": 1,
                "title": "Sunrise City",
                "artist": "Neon Echo",
                "genre": "pop"
            }
        ]
    """

    songs = []

    with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a song using modified sensitivity test weights:
    - Genre importance reduced from +2.0 to +1.0
    - Energy importance increased from +1.0 to +2.0
    """

    score = 0.0
    reasons = []

    # Genre match: +1.0 point (half weight)
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 1.0
        reasons.append("Genre matches preference (+1.0)")

    # Mood match: +1.0 point
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append("Mood matches preference (+1.0)")

    # Energy similarity: up to +2.0 points (double weight)
    energy_difference = abs(song["energy"] - user_prefs["target_energy"])
    energy_score = (1 - energy_difference) * 2

    score += energy_score
    reasons.append(f"Energy similarity score (+{energy_score:.2f})")

    # Acoustic preference
    if user_prefs["likes_acoustic"]:
        acoustic_score = song["acousticness"]
        score += acoustic_score
        reasons.append(f"Acoustic preference score (+{acoustic_score:.2f})")
    else:
        acoustic_score = 1 - song["acousticness"]
        score += acoustic_score
        reasons.append(f"Non-acoustic preference score (+{acoustic_score:.2f})")

    return score, reasons

def recommend_songs(
    user_prefs: Dict, songs: List[Dict], k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Scores every song, ranks results, and returns the best recommendations.

    Each song is evaluated using score_song(). The songs are sorted
    from highest score to lowest score and only the top k results are returned.

    Args:
        user_prefs (Dict): User preference dictionary.
        songs (List[Dict]): List of available songs.
        k (int): Number of recommendations to return.

    Returns:
        List[Tuple[Dict, float, str]]:
            A list containing:
                - Song dictionary
                - Recommendation score
                - Explanation of score

    Example:
        [
            (
                {"title": "Sunrise City"},
                4.85,
                "Genre matches preference (+2.0)"
            )
        ]
    """

    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)

        explanation = ", ".join(reasons)

        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)

    return scored_songs[:k]
