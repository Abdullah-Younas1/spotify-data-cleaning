import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the cleaned dataset
df = pd.read_csv('data/cleaned_spotify_data.csv')

# 2. Select numerical features for similarity comparison
feature_cols = ['danceability', 'energy', 'loudness', 'speechiness', 
                'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

# Normalize features to a 0-1 scale so things like 'tempo' don't dominate 'danceability'
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df[feature_cols])

def get_recommendations(song_name, num_recommendations=5):
    # Match the song name 
    song_matches = df[df['track_name'].str.lower() == song_name.lower()]
    
    if song_matches.empty:
        print(f"\n❌ Could not find a song named '{song_name}' in the dataset. Try another one!")
        return
    
    # Take the first match if there are duplicates of the same song name
    idx = song_matches.index[0]
    song_features = df_scaled[idx].reshape(1, -1)
    
    # Calculate cosine similarity of this song against all other songs
    similarity_scores = cosine_similarity(song_features, df_scaled).flatten()
    
    # Get indices of the most similar songs (excluding the input song itself)
    similar_indices = similarity_scores.argsort()[-(num_recommendations + 1):-1][::-1]
    
    print(f"\n🎧 If you like '{df.loc[idx, 'track_name']}' by {df.loc[idx, 'artists']}, you might also enjoy:")
    print("=" * 70)
    
    for i, sim_idx in enumerate(similar_indices, start=1):
        rec_track = df.loc[sim_idx, 'track_name']
        rec_artist = df.loc[sim_idx, 'artists']
        score = similarity_scores[sim_idx]
        print(f"{i}. {rec_track} — by {rec_artist} ({score:.2%} match)")
    print("=" * 70)

# terminal loop
if __name__ == "__main__":
    print("--- 🎵 Spotify Song Recommendation Engine Live ---")
    while True:
        song = input("\nEnter a song name (or type 'exit' to quit): ").strip()
        if song.lower() == 'exit':
            print("Goodbye! Enjoy the music. 🎧")
            break
        get_recommendations(song)