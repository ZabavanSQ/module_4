import math


def divide(first, second):
    rez = 0
    if second == 0:
        rez = math.inf
    else:
        rez = first / second
    return rez
