'''
Problem 2a
'''

import math


def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def closest_pair(points):
    n = len(points)

    if n < 2:
        return []

    closest_pair = [points[0], points[1]]
    min_distance = d(points[0], points[1])

    for i in range(n - 1):
        for j in range(i + 1, n):
            distance = d(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = [points[i], points[j]]

    return closest_pair
