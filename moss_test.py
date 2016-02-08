__author__ = 'saipc'


def fact(n):
    p = 1
    while n > 0:
        p = p * n
        n = n - 1
    return p

print(fact(6))

def fact2(n):
    p = 1
    for i in xrange(1, n + 1):
        p = p * i
    return p

print(fact2(6))

def fact3(n):
    x = 1
    for j in xrange(1, n + 1):
        x = x * j
    return x

print(fact3(6))