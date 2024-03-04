'''
Problem 1c

input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals (see README).
output: Dictionary mapping students to hospitals. 

TODO: Implement the Gale-Shapley algorithm to run in O(n^2).
'''


def stable_matching_1c(file) -> dict:
    n = 0
    doctors_pref = []
    hospitals_pref = []

    with open(file, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])
    
    print(hospitals_pref)

    # doctors to hospitals map
    matched_hospitals = set()
    for i in range(n):
        matched_hospitals.add(i)
    pairs = {}
    print("matches", matched_hospitals)
    while len(matched_hospitals) > 0:
        h = matched_hospitals.pop()
        doc_preference = hospitals_pref[h].pop(0)

        # If the hospital's preference hasn't been matched
        if doc_preference not in pairs:
            pairs[doc_preference] = h

        # If the hospital's preference already has a match
        else:
            h2 = pairs[doc_preference]
            h1_idx = doctors_pref[doc_preference].index(h)
            h2_idx = doctors_pref[doc_preference].index(h2)
            if h1_idx < h2_idx:
                pairs[doc_preference] = h
                matched_hospitals.add(h2)

    return pairs


'''
instead of having to search through the list of hospitals to see which one has not been matched, you can just
keep track of a set that you pop from. the previous implementation added another O(n) time complexity
'''