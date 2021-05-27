def sum_sum(a, b):
    return a + b


def mul(a, b):
    return sum_sum(a, b) * b


def sub(a, b):
    return mul(a, b) // b


def pow_pow(a, b):
    return sub(a, b) ** b


def to_upper_case(c):
    return c.upper()


def to_lower_case(d):
    return d.lower()


x = 2
y = 3
print(sum_sum(x, y))
print(mul(x, y))
print(sub(x, y))
print(pow_pow(x, y))
print(to_upper_case('PpPpPpPp'))
print(to_lower_case('SsSsSsSSS'))
