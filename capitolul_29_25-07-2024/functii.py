def adunare(x, y):
    return x + y


def scadere(x, y):
    return x - y


def impartire(x, y):
    if y == 0:
        raise ZeroDivisionError("Impartirea la 0 nu are sens")
    return x / y


def inmultire(x, y):
    return x * y

def x_la_puterea_y(x, y):
    return x ** y