'''
Problem 1a

input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals (see README). 
output: Dictionary mapping students to hospitals. 
'''

def stable_matching_1a(file) -> dict:
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

    # doctors to hospitals map
    pairs = {}
    matched_hospitals = set()
    while len(matched_hospitals) < n:
        for h in range(n):
            if h not in matched_hospitals:
                doc_preference = hospitals_pref[h].pop(0)

                # If the hospital's preference hasn't been matched
                if doc_preference not in pairs:
                    pairs[doc_preference] = h
                    matched_hospitals.add(h)

                # If the hospital's preference already has a match
                else:
                    h2 = pairs[doc_preference]
                    h1_idx = doctors_pref[doc_preference].index(h)
                    h2_idx = doctors_pref[doc_preference].index(h2)

                    # bug is that it checks is doctor prefers h2 over h1 when it should be the other way
                    if h1_idx > h2_idx:
                        pairs[doc_preference] = h
                        matched_hospitals.add(h)
                        matched_hospitals.remove(h2)

    return pairs
