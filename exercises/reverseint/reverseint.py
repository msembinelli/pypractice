def reverse_int(i):
    """
    Given an integer, return an integer that is the reverse
    ordering of numbers.
    reverse_int(15) == 51
    reverse_int(981) == 189
    reverse_int(500) == 5
    reverse_int(-15) == -51
    reverse_int(-90) == -9
    """
    negative = i < 0
    tmp = abs(i)
    tmp_str = str(tmp)[::-1]

    if negative:
        tmp_str = '-' + tmp_str

    return int(tmp_str)

def reverse_int_mod(i):
    negative = i < 0
    tmp = abs(i)
    r_int = 0

    while tmp:
        r_int *= 10
        r_int += tmp % 10
        tmp /= 10

    if negative:
        r_int *= -1

    return r_int