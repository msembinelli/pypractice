def reverse(s):
    """
    Given a string, return a new string with the reversed order of characters.
    reverse('apple') == 'elppa'
    reverse('hello') == 'olleh'
    reverse('Greetings!') == '!sgniteerG'
    """
    return s[::-1]

def reverse_join(s):
    return ''.join(reversed(s))

def reverse_manual(s):
    tmp = ""
    for c in reversed(s):
        tmp += c
    return tmp

def reverse_array(s):
    tmp = []
    for c in list(s):
        tmp.insert(0, c)
    return ''.join(tmp)