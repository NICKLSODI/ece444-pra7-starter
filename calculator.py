def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def is_missing(x):
    return x is None


def total(items):
    total_sum = 0
    for i in items:
        total_sum += i
    return total_sum


def count(items):
    n = 0
    for _i in items:
        n += 1
    return n


def broken_total():
    return 0
