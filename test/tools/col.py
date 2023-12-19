# File: tools/col.py

def myzip(it1, it2):
    min_len = min(len(it1), len(it2))
    return [(it1[i], it2[i]) for i in range(min_len)]
