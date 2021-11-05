# the all cyclomatic complexity:24


def factorial(n):
    # cyclomatic complexity: 2
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def add(a, b):
    # cyclomatic complexity: 1
    return a + b


def elif_(a):
    # cyclomatic complexity: 3
    if a == 0:
        return
    elif a == 1:
        return


def for_():
    # cyclomatic complexity: 2
    for i in range(1):
        return


def while_():
    # cyclomatic complexity: 2
    while True:
        return


def try_():
    # cyclomatic complexity: 2
    try:
        return
    except ValueError:
        return


def with_():
    # cyclomatic complexity: 2
    with open("test.txt"):
        return


def assert_():
    # cyclomatic complexity: 2
    assert True


def raise_():
    # cyclomatic complexity: 1
    raise ValueError


def pass_():
    # cyclomatic complexity: 1
    pass


def and_():
    # cyclomatic complexity: 2
    return 1 and 1


def or_():
    # cyclomatic complexity: 2
    return 1 or 1


def list_():
    # cyclomatic complexity: 2
    return [i for i in range(1)]
