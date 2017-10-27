#!/usr/env/bin python3
import sys

MAX_RECURS = 5000
sys.setrecursionlimit(10000) 

ERROR = -1
memo = []
NOT_SEEN = -999999

# what follows are some recurrences for you to try:

# Fibonacci series:
fibb = {0: 0, 1: 1}
def fibf(n, bases):
    return recur(n - 1, bases, fibf) + recur(n - 2, bases, fibf)
# call like this:
#    recur(500, fibb, fibf, True) -- returns 500th Fibonacci number

# Lucas series:
lucb = {0: 2, 1: 1}
# just use fibonacci function with Lucas bases!
# call like this:
#    recur(500, lucb, fibf, True) -- returns 500th Lucas number

# geometric series:
RATIO = 2    # redefine RATIO to get a different multiple
geob = {0: 1, 1: RATIO}
def geof(n, bases):
    return geob[1] * recur(n - 1, bases, geof)
# call like this:
#    recur(500, geob, geof, True) -- returns 500th power of 2

# arithmetic series:
STEP = 4     # redefine STEP to get a different step size
arib = {0: 0, 1: STEP}
def arif(n, bases):
    return arib[1] + recur(n - 1, bases, arif)
# call like this:
#    recur(500, arib, arif, True) -- returns 500th number counting by 4s

# the value of an annuity with equal contributions each year
#  and interest compounded annually:
INT_RATE = .05
INITIAL = 1000     # redefine INITIAL to get different yearly amount
compb = {0: INITIAL}
def compf(n, bases):
    return compb[0] + recur(n - 1, bases, compf) * (1 + INT_RATE)
# call like this:
#    recur(20, compb, compf, True) -- value of annuity after 20 years

# an arbitrary recurrence:
arbb = {0: 1.01, 1: .98, 2: .88, 3: 1.1}
def arbf(n, bases):
    return recur(n - 1, bases, arbf) * recur(n - 4, bases, arbf)

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
        memo[n] = f(n, bases)
        return memo[n]
