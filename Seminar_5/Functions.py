def degree(a, b):
    if b == 0:
        return 1
    return a * degree(a, b - 1)


def recurs_sum(a, b):
    if b == 0:
        return a
    else:
        return recurs_sum(a + 1, b - 1)
