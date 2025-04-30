
# Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space.
# Store them in a numpy array. Convert them to polar coordinates.
# Generate N random 2D points (N >= 10)
import numpy as np
N = 10
cartesian_points = np.random.rand(N, 2) * 100  # Random points in range [0, 100)

# Convert cartesian coordinates to polar coordinates
def cartesian_to_polar(points):
    r = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
    theta = np.arctan2(points[:, 1], points[:, 0])
    return np.column_stack((r, theta))

polar_points = cartesian_to_polar(cartesian_points)

print("Cartesian Points:\n", cartesian_points)
print("Polar Points:\n", polar_points)