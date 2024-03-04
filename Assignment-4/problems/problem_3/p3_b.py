def calculate_cost(cost_matrix, sequence):
    tot_cost = 0
    for i in range(len(sequence) - 1):
        tot_cost += cost_matrix[sequence[i] - 1][sequence[i+1] - 1]
    return tot_cost


def swap(sequence, i, j):
    new_seq = sequence.copy()
    new_seq[i], new_seq[j] = new_seq[j], new_seq[i]
    return new_seq


def local_search_2opt(cost_matrix, candidate):
    curr_best_seq = list(candidate)
    curr_cost = calculate_cost(cost_matrix, curr_best_seq)
    for _ in range(1000):
        for i in range(len(cost_matrix)):
            for j in range(i+1, len(cost_matrix)):
                trial_seq = list(candidate)
                new_seq = swap(trial_seq, i, j)
                new_cost = calculate_cost(cost_matrix, new_seq)

                if new_cost < curr_cost:
                    curr_best_seq = new_seq
                    curr_cost = new_cost
        candidate = curr_best_seq

    return tuple(curr_best_seq)