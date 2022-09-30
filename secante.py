from math import exp, cos


def validar_cambio_signo(ext_a, ext_b):
    return f(ext_a) * f(ext_b) < 0


def f(x):
    return x * exp(x) - 1


def aprox_df(x, x_ant):
    return f(x) - f(x_ant) / (x - x_ant)


def x_sig(x_n, x_ant):
    return x_n - f(x_n) / aprox_df(x_n, x_ant)


def secante(a, b, k, e):
    n = 0
    condicion = True

    if not validar_cambio_signo(a, b):
        print("Intervalo no Valido")
        return

    imprimir_fmt_tabla('N', 'x_n', 'f(x)', 'Error')
    print("-" * 80)

    xa = a
    imprimir_fmt_tabla(n, xa, f(xa), '-')

    n += 1
    x = b
    imprimir_fmt_tabla(n, x, f(x), abs(x - xa))

    while condicion:
        aux = x_sig(x, xa)
        xa = x
        x = aux

        n += 1
        condicion = not (abs(x - xa) < e or n >= k)
        imprimir_fmt_tabla(n, x, f(x), abs(x - xa))

    if abs(x - xa) > e:
        print("No Converge")
    else:
        print("\n" + "La raiz es " + str(x))


def imprimir_fmt_tabla(i, x_i, fx, err):
    print("{:^3} | {:^23} | {:^23} | {:^23}".format(i, x_i, fx, err))


if __name__ == "__main__":
    a = 0
    b = 1
    max = 20
    error = 1 * 10 ** -5

    secante(a, b, max, error)
