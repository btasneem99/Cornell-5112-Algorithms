'''
Problem 2c
'''
import random
import math

from collections import defaultdict


def d(point1, point2):
    return math.pi * ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def closest_pair(points):
    n = len(points)
    
    if n < 2:
        return []

    random.shuffle(points)
    points.sort(key=lambda p: p[0])

    def make_dictionary(points):
        d = {}
        for point in points:
            x, y = point
            key = (int(x), int(y))
            d[key] = point
        return d

    def find_closest_in_subgrid(subgrid, point):
        min_dist = float('inf')
        closest = None
        for p in subgrid:
            if p != point:
                dist = d(point, p)
                if dist < min_dist:
                    min_dist = dist
                    closest = p
        return closest, min_dist

    delta = d(points[0], points[1])
    best_pair = [points[0], points[1]]

    delta_dict = make_dictionary([points[0], points[1]])
    
    for i in range(2, n):
        point = points[i]
        x, y = point
        subsquare_size = delta / 2
        subsquare_x = int(x // subsquare_size)
        subsquare_y = int(y // subsquare_size)
        close_subgrids = []
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                close_subgrids.append((subsquare_x + dx, subsquare_y + dy))
        
        closest, min_dist = find_closest_in_subgrid(delta_dict.values(), point)
        
        if min_dist < delta:
            delta = min_dist
            best_pair = [closest, point]
            delta_dict = make_dictionary([closest, point])
            
            for subgrid in close_subgrids:
                for key in list(delta_dict.keys()):
                    if d(point, delta_dict[key]) >= delta:
                        del delta_dict[key]
        else:
            delta_dict[(int(x), int(y))] = point

    return best_pair
