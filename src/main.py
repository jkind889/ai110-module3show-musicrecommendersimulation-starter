"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Example user preference profiles
    user_prefs_genre_purist = {
        "favorite_genre": "jazz",
        "favorite_mood": "calm",
        "target_energy": 0.3,
        "likes_acoustic": True,
    }

    user_prefs_energy_chaser = {
        "favorite_genre": "edm",
        "favorite_mood": "energetic",
        "target_energy": 1.0,
        "likes_acoustic": False,
    }

    user_prefs_acoustic_mood = {
        "favorite_genre": "folk",
        "favorite_mood": "melancholy",
        "target_energy": 0.4,
        "likes_acoustic": True,
    }

    # Pick which profile to run recommendations for
    user_prefs = user_prefs_genre_purist

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
