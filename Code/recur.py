#!/usr/env/bin python3

ERROR = -1
memo = []
NOT_SEEN = -999999
MAX_RECURS = 501  # because van Rossum doesn't "like" recursion, we got dis
                  # dumb limit on stack depth. It can be extended if you need
                  # it!

# what follows are some recurrences for you to try:

# Fibonacci series:
fibb = {0: 0, 1: 1}
def fibf(n):
    return recur(n - 1, fibb, fibf) + recur(n - 2, fibb, fibf)
# call like this:
#    recur(500, fibb, fibf, True) -- returns 500th Fibonacci number

# Lucas series:
lucb = {0: 2, 1: 1}
def lucf(n):
    return recur(n - 1, lucb, lucf) + recur(n - 2, lucb, lucf)
# call like this:
#    recur(500, lucb, lucf, True) -- returns 500th Lucas number

# geometric series:
RATIO = 2
geob = {0: 1, 1: RATIO}  # redefine RATIO to get a different multiple
def geof(n):
    return geob[1] * recur(n - 1, geob, geof)
# call like this:
#    recur(500, geob, geof, True) -- returns 500th power of 2

# arithmetic series:
STEP = 4
arib = {0: 0, 1: STEP}  # redefine STEP to get a different step size
def arif(n):
    return arib[1] + recur(n - 1, arib, arif)
# call like this:
#    recur(500, arib, arif, True) -- returns 500th number counting by 4s

# the value of an annuity with equal contributions each year
#  and interest compounded annually:
INT_RATE = .05
INITIAL = 1000
compb = {0: INITIAL}  # redefine INITIAL to get different yearly amount

def compf(n):
    return compb[0] + recur(n - 1) * (1 + INT_RATE)
# call like this:
#    recur(20, compb, compf, True) -- value of annuity after 20 years

def recur(n, bases, f, init=False):
    global memo
    if init:
        memo = [NOT_SEEN for x in range(MAX_RECURS)]
    if n < 0:
        print("positive n only: n = " + str(n))
        return ERROR
    elif n > MAX_RECURS:
        print("Maximum recursion depth is " + str(MAX_RECURS))

    if n in bases:
        return bases[n]
    elif memo[n] != NOT_SEEN:
        return memo[n]
    else:
        memo[n] = f(n)
        return memo[n]
