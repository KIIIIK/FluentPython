def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)
factorial(42)
factorial.__doc__
type(factorial)
help(factorial)

fact = factorial
fact
fact(5)
map(factorial, range(11))
list(map(fact, range(11)))












