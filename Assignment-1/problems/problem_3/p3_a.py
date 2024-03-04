'''
Problem 3a

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n (see README). 
    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n^2) as described in the homework.
'''


def number_of_large_inversions_3a(file_path, delta):
    # Read input from the file

    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        ranking = list(map(int, file.readline().split()))

    # Create a dictionary to store the index of each number
    index_map = {ranking[i]: i for i in range(n)}

    # Reorder the ranking based on the index of each number
    re_ranking = [index_map[i] for i in range(1, n + 1)]
    print(re_ranking)

    # Initialize inversion count
    large_inversions_count = 0

    # Iterate through the reordered ranking and count large inversions
    for i in range(n):
        for j in range(i + 1, n):
            if re_ranking[i] > re_ranking[j] + delta:
                large_inversions_count += 1

    return large_inversions_count

  
# Return the count of large inversions