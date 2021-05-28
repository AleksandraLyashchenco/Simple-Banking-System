a = 5
b = 3


def sum_sum (a, b):
    return a + b


def mul(a, b):
    c = 1
    d = a
    while c < b:
        d = sum_sum(d, a)
        c += 1
    return d

d = mul( a, b)
print(d)
