from math import exp


def validar_cambio_signo(ext_a, ext_b):
    return f(ext_a) * f(ext_b) < 0


def f(valor):
    return valor * exp(valor) - 1


def df(valor):
    return exp(valor) * (valor + 1)


def ddf(valor):
    return exp(valor) * (valor + 2)


def x_n(x_ant):
    return x_ant - f(x_ant) / df(x_ant)


def imprimir_fmt_tabla(i, val, fx, dfx, err):
    print("{:^3} | {:^23} | {:^23} | {:^23} | {:^23}".format(i, val, fx, dfx, err))


if __name__ == "__main__":
    n = 0
    a = 0
    b = 1
    error = 1 * 10 ** -5
    if not validar_cambio_signo(a, b):
        print("Intervalo no Valido")
    if f(a) * ddf(a) > 0:
        x = a
    else:
        x = b
    imprimir_fmt_tabla('N', 'x', 'f(x)', 'df(x)', 'Error')
    print("-" * 110)
    imprimir_fmt_tabla(n, x, f(x), df(x), '-')
    n += 1
    xa = x
    while True:
        if n != 1:
            if abs(x - xa) < error:
                break
        xa = x
        x = x_n(xa)
        imprimir_fmt_tabla(n, x, f(x), df(x), abs(x - xa))
        n += 1
