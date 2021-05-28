a = 5
b = 4


def mul(a, b):
    c = 1
    d = a
    while c < b:
        d += a
        c += 1
    return d

d = mul( a, b)
print(d)
