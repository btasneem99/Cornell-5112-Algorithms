'''
Problem 2b
'''

import math

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    def euclidean_distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def brute_force_closest_pair(points):
        min_dist = float('inf')
        closest = None
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                dist = euclidean_distance(points[i], points[j])
                if dist < min_dist:
                    min_dist = dist
                    closest = (points[i], points[j])
        return min_dist, closest

    def closest_pair_rec(Px, Py):
        n = len(Px)
        if n <= 3:
            return brute_force_closest_pair(Px)

        mid = n // 2
        Qx = Px[:mid]
        Rx = Px[mid:]
        x_mid = Px[mid][0]
        Qy = [p for p in Py if p in Qx]
        Ry = [p for p in Py if p in Rx]

        delta_1, closest_1 = closest_pair_rec(Qx, Qy)
        delta_2, closest_2 = closest_pair_rec(Rx, Ry)
        delta = min(delta_1, delta_2)

        # Compute the minimum distance between the closest pairs from both sides
        if delta_1 < delta_2:
            delta, closest = delta_1, closest_1
        else:
            delta, closest = delta_2, closest_2

        Sy = [p for p in Py if x_mid - delta <= p[0] <= x_mid + delta]
        min_dist, closest = delta, closest

        for i in range(len(Sy)):
            for j in range(i + 1, min(i + 16, len(Sy))):
                dist = euclidean_distance(Sy[i], Sy[j])
                if dist < min_dist:
                    min_dist = dist
                    closest = (Sy[i], Sy[j])

        return min_dist, closest

    points.sort(key=lambda p: p[0])
    Px = points
    points.sort(key=lambda p: p[1])
    Py = points

    return closest_pair_rec(Px, Py)[1]