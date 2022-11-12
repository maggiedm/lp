from math import exp, sin, pi


def f(x):
    return exp(2 - 0.5 * sin(x))


def simpson_simple(a, b):
    return simpson_compuesto(a, b, 2)


def simpson_compuesto(a, b, n):

    if n % 2 != 0:
        return "ERROR, la cantidad de intervalos debe ser par"

    h = (b - a) / n

    x = [a + q * h for q in range(n + 1)]
    y = [f(q) for q in x]

    ia = sum(y[2 * q - 1] for q in range(1, int(n / 2 + 1)))
    p = sum(y[2 * q] for q in range(1, int(n / 2)))

    return round(h / 3 * (y[0] + 4 * ia + 2 * p + y[n]), 4)


if __name__ == "__main__":
    print("El metodo de simpson simple obtiene como resultado para la funcion "
          + str(simpson_simple(0, 2 * pi)))

    cant_intervalos = 8

    print("El metodo de simpson compuesto, usando " + str(cant_intervalos) + " intervalos, obtiene como resultado "
          + "para la funcion " + str(simpson_compuesto(0, 2 * pi, cant_intervalos)))
