#!/usr/bin/env python3

def character_frequency(filename):
    """Counts the frequency of each charracter in the given file."""
    #first try to open the filename
    try:
        f = open(filename)
    except OSError:
        return None

    #Now process the filename
    charaters = {}
    for line in f:
        for char in line:
            characters[char] = cahracters.get(char, 0) + 1
    f.close()
    return characters
