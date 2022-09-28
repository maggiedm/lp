from math import exp, cos, sin


def validar_cambio_signo(ext_a, ext_b):
    return f(ext_a) * f(ext_b) < 0


def f(x):
    return x * exp(x) - 1


def df(x):
    return exp(x) * (x + 1)


def ddf(x):
    return exp(x) * (x + 2)


def x_n(x_ant):
    return x_ant - f(x_ant) / df(x_ant)


def newton_raphson(a, b, max, e):
    n = 0
    condicion = True

    if not validar_cambio_signo(a, b):
        print("Intervalo no Valido")
        return
    if f(a) * ddf(a) > 0:
        x = a
    else:
        x = b

    imprimir_fmt_tabla('N', 'x', 'f(x)', 'df(x)', 'Error')
    print("-" * 110)
    imprimir_fmt_tabla(n, x, f(x), df(x), '-')

    n += 1
    while condicion:
        xa = x
        x = x_n(xa)
        imprimir_fmt_tabla(n, x, f(x), df(x), abs(x - xa))
        n += 1
        condicion = not (n > max or abs(x - xa) < e)

    if abs(x - xa) > e:
        print("No Converge")
    else:
        print("\n" + "La raiz es " + str(x))


def imprimir_fmt_tabla(i, val, fx, dfx, err):
    print("{:^3} | {:^23} | {:^23} | {:^23} | {:^23}".format(i, val, fx, dfx, err))


if __name__ == "__main__":
    a = 0
    b = 1
    error = 1 * 10 ** -5
    max_n = 20

    newton_raphson(a, b, max_n, error)
