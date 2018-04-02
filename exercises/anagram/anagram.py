import string

def is_anagram(s1, s2):
    """
    Check to see if two provided strings are anagrams of eachother.
    One string is an anagram of another if it uses the same characters
    in the same quantity. Only consider characters, not spaces or
    punctuation. Consider capital letters to be the same as lower case.
    self.assertTrue(func('rail safety', 'fairy tales'))
    self.assertTrue(func('RAIL! SAFETY!', 'fairy tales'))
    self.assertFalse(func('Hi there', 'Bye there'))
    """
    anagram_map = dict.fromkeys(string.ascii_lowercase, 0)

    for c in s1.lower():
        if c in anagram_map:
            anagram_map[c] += 1

    for c in s2.lower():
        if c in anagram_map:
            anagram_map[c] -= 1

    for item in anagram_map:
        if anagram_map[item] != 0:
            return False
    
    return True

def map_helper(s):
    s_mod = ''.join(e for e in s if e.isalnum()).lower()
    s_map = dict.fromkeys(s_mod, 0)
    for c in s_mod:
        s_map[c] += 1
    return s_map

def is_anagram_better(s1, s2):
    s1_dict = map_helper(s1)
    s2_dict = map_helper(s2)

    if len(s1_dict) != len(s2_dict):
        return False
    
    for item in s1_dict:
        if item not in s2_dict:
            return False
        if s1_dict[item] != s2_dict[item]:
            return False

    return True

def sort_helper(s):
    s_mod = ''.join(sorted(''.join(e for e in s if e.isalnum()).lower()))
    return s_mod

def is_anagram_sort(s1, s2):
    return sort_helper(s1) == sort_helper(s2)
