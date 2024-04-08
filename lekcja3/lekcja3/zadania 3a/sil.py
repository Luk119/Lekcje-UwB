def sn(x, y):
    return silnia(x)/(silnia(y) * silnia(x-y))
def silnia(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * silnia(x-1)