from math import exp


def f(x):
    return x * exp(x) - 1


def imprimir_fmt_tabla(i, x, fx, err):
    print("{:^3} | {:^23} | {:^23} | {:^23}".format(i, x, fx, err))


def g(x):
    return 1 / exp(x)


def punto_fijo(xo, err, max_n):
    n = 1
    condicion = True

    imprimir_fmt_tabla('N', 'xn', 'f(xn)', 'Error')
    print('-' * 85)

    imprimir_fmt_tabla(0, x0, f(x0), '-')

    while condicion:

        xn = g(xo)
        imprimir_fmt_tabla(n, xn, f(xn), abs(xn - xo))
        n += 1

        condicion = not (n > max_n or abs(xn - xo) < err)
        xo = xn

    if abs(xn - xo) > err:
        print('La funcion diverge')
    else:
        print("\n" + "La raiz es " + str(xn))

if __name__ == "__main__":
    a = 0.1 # Saco el 0 porque |g'(0)| = 1
    b = 1
    error = 1 * 10 ** -5
    x0 = 0.5
    max_i = 15

    punto_fijo(x0, error, max_i)
