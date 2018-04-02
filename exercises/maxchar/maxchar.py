def max_char(s):
    """
    Given a string, return the character that has the most
    occurrences in the string.
    max_char("abccccccd") == "c"
    max_char("apple 1231111") == "1"
    """
    max_val = 0
    max_c = ''
    c_map = dict()
    for c in s:
        if c not in c_map.keys():
            c_map[c] = 0

        c_map[c] += 1
        if c_map[c] > max_val:
            max_val = c_map[c]
            max_c = c

    return max_c