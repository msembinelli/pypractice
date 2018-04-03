def step(n, current = 0):
    """
    Print a staircase using the '#' character up to n rows and n length.
    step(5)
    self.assertEqual(output, '#    \n##   \n###  \n#### \n#####')
    """
    char_out = ['#'] * (n - current) + [' '] * current
    if current < n:
        step(n, current + 1)
    print ''.join(char_out)

def step_naive(n):
    out_chars = []
    for i in range(n):
        for j in range(n):
            if j<= i:
                out_chars.append('#')
            else:
                out_chars.append(' ')
        print ''.join(out_chars)
        out_chars = []


