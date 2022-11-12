from math import exp, sin, pi


def f(x):
    return exp(2 - 0.5 * sin(x))


def trapecios_simple(a, b):
    return trapecios_compuesto(a, b, 1)


def trapecios_compuesto(a, b, n):
    h = (b - a) / n

    x = [a + i * h for i in range(n + 1)]
    y = [f(i) for i in x]

    return round(h / 2 * (y[0] + 2 * sum(y[1:n]) + y[n]), 4)


if __name__ == "__main__":
    print("El metodo de trapecios simple obtiene como resultado para la funcion "
          + str(trapecios_simple(0, 2 * pi)))

    cant_intervalos = 8

    print("El metodo de trapecios compuesto, usando " + str(cant_intervalos) + " intervalos, obtiene como resultado "
          + "para la funcion " + str(trapecios_compuesto(0, 2 * pi, cant_intervalos)))
