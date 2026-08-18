def add(*args):
    aux = 0
    for n in args:
        aux = aux + n
    return aux

print(add(3,6,1,5,6,1))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(3, multiply=5, add=3))