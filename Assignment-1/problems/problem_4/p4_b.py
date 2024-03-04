'''
Problem 4b

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n).
'''


def most_frequent_difference_b(values, d_mode) -> int:

    count_dict = {}
    for val in values:
        if val not in count_dict:
            count_dict[val] = 0
        count_dict[val] += 1
    
    d_mode_count = 0
    for val in values:
        if (val + d_mode) in count_dict:
            d_mode_count += count_dict[val + d_mode]
            if d_mode == 0:
                d_mode_count -= 1
        # else:
        #     d_mode_count += (count_dict[val] * (count_dict[val] - 1))

    return d_mode_count