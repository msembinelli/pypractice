def pyramid(n, start = 0):
    """
    Write a function that accepts a positive number N.
    The function should console log a pyramid shape
    with N levels using the # character. Make sure the pyramid
    has spaces on both the left and right hand sides.
    pyramid(3)
    self.assertEqual(output, '  #  \n ### \n#####')
    """
    spaces = ([' '] * (start/2))
    hashes = (['#'] * (2*n - 1))
    out = spaces + hashes + spaces
    if (2*n - 1) > 1:
        pyramid(n-1, start+2)
    print ''.join(out)


