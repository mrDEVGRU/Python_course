def degree(a, b):
    if b == 0:
        return 1
    return a * degree(a, b - 1)
