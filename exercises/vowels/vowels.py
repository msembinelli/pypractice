def vowels(s):
    """
    Write a function that returns the number of vowels
    used in a string. Vowels are the characters 'a', 'e',
    'i', 'o', and 'u'.
    self.assertEqual(vowels('Hi There!'), 3)
    self.assertEqual(vowels('Why do you ask?'), 4)
    self.assertEqual(vowels('Why?'), 0)
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    vowels = 0
    for c in s.lower():
        if c in vowel_list and c.isalnum():
            vowels += 1
    return vowels

import re

def vowels_regex(s):
    vowels = re.findall('[aeiou]', s, re.IGNORECASE)
    return len(vowels)


