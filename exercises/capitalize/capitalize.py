def capitalize_string(s):
    """
    Write a function that accepts a string. The function should
    capitalize the first letter of each word in the string then
    return the capitalized string.
    self.assertEqual(func('a short sentence'), 'A Short Sentence'))
    self.assertEqual(func('a lazy fox'), 'A Lazy Fox'))
    self.assertEqual(func('look, it is working!'), 'Look, It Is Working!'))
    """
    word_list = []
    for word in s.split(' '):
        cap_word = word

        if word[0].isalnum():
            cap_word = word[0].upper() + word[1:]

        word_list.append(cap_word)
    
    new_s = ' '.join(word_list)

    return new_s

def capitalize_string_char(s):
    char_list = []
    last_c = ' '
    for c in s:
        new_c = c

        if last_c == ' ' and c.isalnum():
            new_c = c.upper()

        char_list.append(new_c)
        last_c = new_c
    
    new_s = ''.join(char_list)
    return new_s
    
