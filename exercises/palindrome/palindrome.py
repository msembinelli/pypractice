def is_palindrome(s):
    """
    Given a string, return true if the string is a palindrome
    or false if it is not. Palindromes are strings that form
    the same word if it is reversed. *Do* include spaces and
    punctuation in determining if the string is a palindrome.
    is_palindrome("abba") == True
    is_palindrome("abcdefg") == False 
    """
    return s[::-1] == s

def is_palindrome_element(s):
    max_i = len(s) - 1
    for i in range(len(s)):
        if i >= (max_i - i):
            break
        if s[i] != s[max_i - i]:
            return False
    return True