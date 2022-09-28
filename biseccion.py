from math import exp, cos


def validar_cambio_signo(ext_a, ext_b):
    return f(ext_a) * f(ext_b) < 0


def f(x):
    return x * exp(x) - 1


def biseccion(a, b, err):
    n = 0

    if not validar_cambio_signo(a, b):
        print("Intervalo no Valido")
        return

    imprimir_fmt_tabla('N', 'Medio', 'f(a)', 'f(medio)', 'f(b)', 'error')
    print("-" * 135)

    condicion = True
    while condicion:
        medio = (a + b) / 2
        imprimir_fmt_tabla(n, str(medio), str(f(a)), str(f(medio)), str(f(b)), abs(medio - a))
        condicion = not (abs(medio - a) < err)
        if validar_cambio_signo(a, medio):
            b = medio
        else:
            a = medio
        n += 1
    print("\n" + "La raiz es " + str((a + b) / 2))


def imprimir_fmt_tabla(i, val_medio, fa, fm, fb, err):
    print("{:^3} | {:^23} | {:^23} | {:^23} | {:^23} | {:^23}".format(i, val_medio, fa, fm, fb, err))


if __name__ == "__main__":
    a = 0
    b = 1
    error = 1 * 10 ** -5
    biseccion(a, b, error)
