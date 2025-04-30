import math

# Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
# of the points in your 3-D space and store them in a list. The final output is a list with each
# consisting of a point and its nearest neighbour. [Hint: Use distance between two points
# formula
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)

def find_nearest_neighbours(points):
    neighbours = []
    for i, point in enumerate(points):
        min_distance = float('inf')
        nearest_neighbour = None
        for j, other_point in enumerate(points):
            if i != j:
                dist = distance(point, other_point)
                if dist < min_distance:
                    min_distance = dist
                    nearest_neighbour = other_point
        neighbours.append((point, nearest_neighbour))
    return neighbours

# Input 10 3-D points
points = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 3, 5),
    (2, 4, 6),
    (3, 5, 7),
    (4, 6, 8),
    (5, 7, 9),
    (6, 8, 10),
    (7, 9, 11)
]

nearest_neighbours = find_nearest_neighbours(points)
print(nearest_neighbours)