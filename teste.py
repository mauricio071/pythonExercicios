def x(n):
    if (n <= 0):
        return 0
    else:
        return n + x(n - 1)

print(x(3))
