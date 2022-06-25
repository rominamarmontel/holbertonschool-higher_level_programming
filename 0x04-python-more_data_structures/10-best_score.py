#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[best]:
                best = key
        return best
    return None
