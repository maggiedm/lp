from math import exp


def f(x):
    return x * exp(x) - 1


def imprimir_fmt_tabla(i, x0, x1, xn, fx, err):
    print("{:^3} | {:^23} | {:^23} | {:^23} | {:^23} | {:^23}".format(i, x0, x1, xn, fx, err))


def regula_falsi (x0, x1, err):
    n = 0
    condicion = True
    imprimir_fmt_tabla('N', 'x0', 'x1', 'xn', 'f(xn)', 'Error')
    print('-' * 135)

    while condicion:
        xn = x0 - ((x0-x1) * f(x0))/(f(x0) - f(x1))
        imprimir_fmt_tabla(n, x0, x1, xn, f(xn), abs(f(xn)))

        if f(x0) * f(xn) < 0:
            x1 = xn
        elif f(x0) * f(xn) > 0:
            x0 = xn

        condicion = abs(f(xn)) > err
        n += 1

    print("\n" + "La raiz es " + str(xn))


if __name__ == "__main__":
    a = 0
    b = 1
    error = 1 * 10 ** -5

    regula_falsi(a, b, error)