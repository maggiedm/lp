from math import exp


def validar_cambio_signo(ext_a, ext_b):
    return f(ext_a) * f(ext_b) < 0


def f(valor):
    return valor * exp(valor) - 1


def aprox_df(valor, valor_ant):
    return f(valor) - f(valor_ant) / (valor - valor_ant)


def x_sig(x_n, x_ant):
    return x_n - f(x_n) / aprox_df(x_n, x_ant)


def imprimir_fmt_tabla(i, x_i, fx, err):
    print("{:^3} | {:^23} | {:^23} | {:^23}".format(i, x_i, fx, err))


if __name__ == "__main__":
    n = 0
    a = 0
    b = 1
    error = 1 * 10 ** -5
    if not validar_cambio_signo(a, b):
        print("Intervalo no Valido")
    imprimir_fmt_tabla('N', 'x_n', 'f(x)', 'Error')
    print("-" * 110)
    xa = a
    imprimir_fmt_tabla(n, xa, f(xa), '-')
    n += 1
    x = b
    imprimir_fmt_tabla(n, x, f(x), abs(x - xa))
    while True:
        if n != 1:
            if abs(x - xa) < error:
                break
        aux = x_sig(x, xa)
        xa = x
        x = aux
        n += 1
        imprimir_fmt_tabla(n, x, f(x), abs(x - xa))
