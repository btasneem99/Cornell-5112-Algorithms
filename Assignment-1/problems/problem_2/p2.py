'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''


def interval_covering(M: int, intervals: list) -> list:
    intervals.sort()
    minimum_intervals = []
    left = 0
    right = -1
    i = 0
    while i < len(intervals):
        int_left, int_right = intervals[i]
        if int_left <= left:
            if int_right > right:
                right = int_right
                if len(minimum_intervals):
                    minimum_intervals.pop()
                minimum_intervals.append(intervals[i])
            i += 1
        else:
            left = right
            minimum_intervals.append(intervals[i])
        if right >= M:
            break
    
    return minimum_intervals