def maximo(x, y, z):
    max = 0
    if x > y:
        max = x
    else:
        max = y
    if z > max:
        max = z

    return max
