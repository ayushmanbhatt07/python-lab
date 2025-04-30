# Write a program to make the length of each element 15 of a given Numpy array and the
# string centred, left-justified, right-justified with paddings of _ (underscore).
# Create a sample numpy array
import numpy as np

arr = np.array(["apple", "banana", "cherry", "date"])

# Make the length of each element 15 and apply different justifications
centered = np.char.center(arr, 15, fillchar='_')
left_justified = np.char.ljust(arr, 15, fillchar='_')
right_justified = np.char.rjust(arr, 15, fillchar='_')

# Print the results
print("Centered:")
print(centered)
print("Left-justified:")
print(left_justified)
print("Right-justified:")
print(right_justified)