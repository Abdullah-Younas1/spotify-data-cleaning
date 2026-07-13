import pandas as pd

# 1. Load the data from the current folder (no 'data/' prefix needed!)
df = pd.read_csv('spotify-tracks-dataset.csv')

print("--- Data Loaded Successfully! ---")
print(f"Total rows before cleaning: {len(df)}")

# 2. Clean Missing Values
df.dropna(inplace=True)

# 3. Remove Duplicate Rows
df.drop_duplicates(inplace=True)

print(f"Total rows after cleaning: {len(df)}")

# 4. Save the polished data into your 'data' folder to keep things organized
df.to_csv('data/cleaned_spotify_data.csv', index=False)
print("--- Data cleaning complete! 'data/cleaned_spotify_data.csv' has been created. ---")