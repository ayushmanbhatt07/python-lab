
# Whenever your friends John and Judy visit you together, y’all have a party. Given a
# DataFrame with 10 rows representing the next 10 days of your schedule and whether John
# and Judy are scheduled to make an appearance, insert a new column
# called days_til_party that indicates how many days until the next party.
# days_til_party should be 0 on days when a party occurs, 1 on days when a party doesn’t
# occur but will occur the next day, etc.
# Example DataFrame
import pandas as pd
data = {
    'John': [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    'Judy': [1, 1, 0, 0, 1, 0, 1, 0, 1, 1]
}
df = pd.DataFrame(data)

# Identify party days
df['party'] = (df['John'] & df['Judy']).astype(int)

# Calculate days_til_party
days_til_party = []
next_party = float('inf')

for is_party in reversed(df['party']):
    if is_party:
        next_party = 0
    else:
        next_party += 1
    days_til_party.append(next_party)

df['days_til_party'] = list(reversed(days_til_party))

# Drop the temporary 'party' column
df.drop(columns=['party'], inplace=True)

print(df)