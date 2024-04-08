from math import pow


def a(n, a1=2, q=1):
    if n == 1:
        return a1
    elif n == 2:
        return a1 * q
    else:
        return a1 * pow(q, n - 1)


def b(n, a1=1, q=2):
    return a1 * (1 - pow(q, n)) / (1 - q)
