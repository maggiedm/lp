from math import exp


def validar_cambio_signo(ext_a, ext_b):
    return f(ext_a) * f(ext_b) < 0


def f(valor):
    return valor * exp(valor) - 1


def imprimir_fmt_tabla(i, val_medio, fa, fm, fb, err):
    print("{:^3} | {:^23} | {:^23} | {:^23} | {:^23} | {:^23}".format(i, val_medio, fa, fm, fb, err))


if __name__ == "__main__":
    n = 0
    a = 0
    b = 1
    error = 1 * 10 ** -5
    while validar_cambio_signo(a, b):
        if n == 0:
            imprimir_fmt_tabla('N', 'Medio', 'f(a)', 'f(medio)', 'f(b)', 'error')
            print("-" * 110)
        medio = (a + b) / 2
        n += 1
        imprimir_fmt_tabla(n, str(medio), str(f(a)), str(f(medio)), str(f(b)), abs(medio - a))
        if abs(medio - a) < error:
            break
        if validar_cambio_signo(a, medio):
            b = medio
        else:
            a = medio
    if n == 0:
        print("Intervalo no Valido")
