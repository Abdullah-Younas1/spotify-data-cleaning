import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Load the clean dataset
df = pd.read_csv('data/cleaned_spotify_data.csv')
print("--- Cleaned Data Loaded Successfully! ---")
print(f"Dataset shape: {df.shape}")

# Create an 'images' folder to save our charts if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set a clean style for our plots
sns.set_theme(style="whitegrid")

# ----------------------------------------------------
# INSIGHT 1: Top 10 Most Popular Artists
# ----------------------------------------------------
print("\nGenerating Chart 1: Top Artists...")
plt.figure(figsize=(10, 6))

# Group by artist and get their average popularity
top_artists = df.groupby('artists')['popularity'].mean().sort_values(ascending=False).head(10)

sns.barplot(x=top_artists.values, y=top_artists.index, palette="viridis")
plt.title('Top 10 Most Popular Artists (Average Track Popularity)', fontsize=14, fontweight='bold')
plt.xlabel('Average Popularity Score')
plt.ylabel('Artist')
plt.tight_layout()

# Save the plot
plt.savefig('images/top_artists.png', dpi=300)
plt.close()
print("Saved: images/top_artists.png")

# ----------------------------------------------------
# INSIGHT 2: Correlation Heatmap (How song features relate)
# ----------------------------------------------------
print("Generating Chart 2: Feature Correlation Heatmap...")
plt.figure(figsize=(10, 8))

# Select numerical columns to see how they correlate (e.g., does high energy mean high loudness?)
numerical_cols = ['popularity', 'duration_ms', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
correlation_matrix = df[numerical_cols].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Spotify Track Features Correlation Heatmap', fontsize=14, fontweight='bold')
plt.tight_layout()

# Save the plot
plt.savefig('images/feature_correlation.png', dpi=300)
plt.close()
print("Saved: images/feature_correlation.png")

print("\n🎉 EDA complete! Check your new 'images' folder for the charts.")