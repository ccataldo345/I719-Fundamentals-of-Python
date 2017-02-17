'''
Write a function charswap() that takes at least one argument

The function should swap first and last character of a string and return the resulting string.

Handle all cases of input. Char with length 1, 0 or even number. If the input is not string, then make it string.
E.g., if Taavi is passed in as the first argument then the function should return "iaavT".
'''

def charswap(s):
    s = str(s)
    if len(s)== 1 or len(s) == 0:
        return s
    else:
        s= s[-1] + s[1:-1] + s[0]
        return s

print (charswap("01"))

