from math import *


def f(x):
    return exp(2 - 0.5 * sin(x))


def trapecios_compuesto(a, b, h):
    n = int((b - a) / h)

    x = [a + i * h for i in range(n + 1)]
    y = [f(i) for i in x]
    t = h / 2 * (y[0] + 2 * sum(y[1:n]) + y[n])

    return t


def romberg(a, b, n):
    mr = []
    mc = []
    h = b - a
    for i in range(n + 1):
        t = trapecios_compuesto(a, b, h)
        mr.insert(0, t)
        h = h/2
    mc.append(mr.copy())
    for i in range(n):
        p = 4 ** (i + 1)
        for j in range(n - i):
            mr[j] = (p * mr[j] - mr[j + 1]) / (p - 1)
        aux = mr.copy()
        for j in range(n - i, n + 1):
            aux.pop()
        mc.append(aux)
    for r in mc:
        print(r)
    print("\n")

    return mr[0]


if __name__ == "__main__":
    pasos = 3
    print("El metodo de Romberg, con " + str(pasos) + " pasos, aproxima la integral a: " + str(romberg(0, 2 * pi, pasos)))

