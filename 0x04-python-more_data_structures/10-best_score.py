#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = list(a_dictionary)[0]
        for i in a_dictionary:
            if a_dictionary[i] > a_dictionary[best]:
                best = i
        return best
    return None
