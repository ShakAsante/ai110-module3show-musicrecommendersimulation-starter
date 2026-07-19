"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 40)
    print("       TOP MUSIC RECOMMENDATIONS")
    print("=" * 40)

    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{index}: {song['title']}")
        print(f"Artist: {song['artist']}")
        print(f"Genre: {song['genre']} | Mood: {song['mood']}")
        print(f"Score: {score:.2f}")
        print("Reasons:")
        
        for reason in explanation.split(", "):
            print(f"  ✓ {reason}")

    print("\n" + "=" * 40)
    
if __name__ == "__main__":
    main()
