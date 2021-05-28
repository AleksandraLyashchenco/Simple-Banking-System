x = 5
y = 10


def sum_sum (a, b):
    return a + b


def mul(a, b):
    c = 1
    d = a
    while c < b:
        d = sum_sum(d, a)
        c = sum_sum(c, 1)
    return d

d = mul(x, y)
print(d)
