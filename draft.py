x = 5
y = 3


def sum_sum (x, y):
    return x + y


def mul(x, y):
    c = 1
    d = x
    while c < y:
        d = sum_sum(d, x)
        c = sum_sum(c, 1)
    return d

d = mul(x, y)
print(d)
