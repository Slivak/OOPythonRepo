def custom_sum(a=None, b=None, c=None, d=None):
    return a + b + c + d


def custom_sum_args(*args):
    total = 0
    for elem in args:
        total += elem
    return total

print(custom_sum_args(4, 3, 2, 7, 4, 1, 0, 9))


def digits(**kwargs):
    for elem in kwargs.items():
        print(elem)
    return 0

print(digits(a=3, b=5, c=2, e=1, d=8))

