
# Write a Pandas program to convert all the string values to upper, lower cases in a given
# pandas series. Also find the length of the string values.
# s = pd.Series ([‘X’, ‘Y’, ‘T’, ‘Aaba’, ‘Baca’, ‘CABA’, None, ‘bird’, ‘horse’, ‘dog’])
import pandas as pd
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

# Convert to upper case
upper_case = s.str.upper()

# Convert to lower case
lower_case = s.str.lower()

# Find the length of each string
string_length = s.str.len()

print("Original Series:")
print(s)
print("\nUpper Case:")
print(upper_case)
print("\nLower Case:")
print(lower_case)
print("\nString Lengths:")
print(string_length)