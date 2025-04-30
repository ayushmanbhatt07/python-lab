
# Given a dataset of concerts, count the number of concerts per (artist, venue), per year
# month. Make the resulting table be a wide table - one row per year month with a column
# for each unique (artist, venue) pair. Use the cross product of the artists and venues Series
# to determine which (artist, venue) pairs to include in the result.
# Example dataset
import pandas as pd
data = {
    'artist': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'venue': ['X', 'Y', 'X', 'Z', 'Y', 'Z', 'X'],
    'date': ['2023-01-15', '2023-01-15', '2023-02-20', '2023-02-20', '2023-03-10', '2023-03-10', '2023-03-10']
}

# Create DataFrame
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')

# Get unique artists and venues
artists = df['artist'].unique()
venues = df['venue'].unique()

# Create cross product of artists and venues
artist_venue_pairs = pd.MultiIndex.from_product([artists, venues], names=['artist', 'venue'])

# Count concerts per (artist, venue), per year_month
concert_counts = df.groupby(['year_month', 'artist', 'venue']).size().unstack(fill_value=0)

# Reindex to include all (artist, venue) pairs
concert_counts = concert_counts.reindex(columns=artist_venue_pairs, fill_value=0)

# Reset index to make it a wide table
result = concert_counts.reset_index()

print(result)