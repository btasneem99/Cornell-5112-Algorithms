def count_min_sketch(a, b, w, p, stream):
    c = len(a)

    ans = [[0 for _ in range(w)] for _ in range(c)]

    for x in stream:
        for i in range(c):
            hash_ind = ((a[i] * x + b[i]) % p) % w

            ans[i][hash_ind] += 1

    return ans