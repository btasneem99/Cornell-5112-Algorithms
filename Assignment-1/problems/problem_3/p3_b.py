'''
Problem 3b

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n (see README). 
    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n log n) as described in the homework.
'''


def number_of_large_inversions_3b(file_path, delta):
    def merge(arr, left, mid, right, delta):
        inv_count = 0
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if arr[i] > arr[j] + delta:
                inv_count += mid - i + 1
                j += 1
            else:
                i += 1

        temp = []
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[left + k] = temp[k]

        return inv_count

    def merge_sort(arr, left, right, delta):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort(arr, left, mid, delta)
            inv_count += merge_sort(arr, mid + 1, right, delta)
            inv_count += merge(arr, left, mid, right, delta)
        return inv_count

    # Read input from the file
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        ranking = list(map(int, file.readline().split()))

    # Create a dictionary to store the index of each number
    indices = {ranking[i]: i for i in range(n)}

    # Reorder the ranking based on the index of each number
    re_ranking = [indices[i] for i in range(1, n + 1)]

    # Create a copy of the reordered ranking list for sorting
    sorted_ranking = re_ranking[:]

    # Use Merge Sort to count large inversions
    large_inversions_count = merge_sort(sorted_ranking, 0, n - 1, delta)

    return large_inversions_count
'''
# Example:
file_name = '../tests/input/test_p3_public_n4_1.txt'  
delta = 1

result = number_of_large_inversions_3b(file_name, delta)
if result is not None:
    print(f'Number of large inversions: {result}')
'''