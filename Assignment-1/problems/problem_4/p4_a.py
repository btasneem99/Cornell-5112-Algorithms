'''
Problem 4a

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n log n).
'''


def binary_search_first(a, low, high, x) -> int:
    if (high >= low):
        mid = low + (high - low)//2
        if (x == a[mid]) and (mid==low or x > a[mid-1]):
            return mid
        elif (x > a[mid]):
            return binary_search_first(a, (mid + 1), high, x)
        else:
            return binary_search_first(a, low, (mid - 1), x)
    return -1


def binary_search_last(a, low, high, x) -> int:
    if (high >= low):
        mid = low + (high - low)//2
        n = len(a)
        if (x == a[mid]) and (mid==high or x < a[mid+1]):
            return mid
        elif (x < a[mid]):
            return binary_search_last(a, low, (mid - 1), x)
        else:
            return binary_search_last(a, (mid + 1), high, x)      
    return -1


def most_frequent_difference_a(values, d_mode) -> int:
    values.sort()

    d_mode_count = 0

    i = 0
    n = len(values)

    while (i < n):
        index_first = binary_search_first(values, 0, n-1, values[i] + d_mode)
        if (index_first != -1):
            index_last = binary_search_last(values, 0, n-1, values[i] + d_mode)
            d_mode_count += (index_last - index_first + 1)
            if (i >= index_first and i<=index_last):
                d_mode_count -= 1
        i += 1

    return d_mode_count