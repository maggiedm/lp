from math import e


def f_real(t):
    return (t + 1) ** 2 - 0.5 * e ** t


def df(t, y):
    return y - t ** 2 + 1


# a, b: extremos
# n: # iteraciones
# y0: condicion inicial
def runge_kutta_4(a, b, y0, n):
    h = (b - a) / n
    t = a
    w = y0
    print("{:^4} | {:^4} | {:^20} | {:^20} | {:^20}".format("i", "ti", "f(t)", "wi", "Error Absoluto"))
    print("-" * 80)
    print("{:^4} | {:^4} | {:^20} | {:^20} | {:^20}".format(0, t, f_real(t), w, abs(f_real(t) - w)))

    for i in range(1, n + 1):
        k1 = h * df(t, w)
        k2 = h * df(t + h / 2, w + k1 / 2)
        k3 = h * df(t + h / 2, w + k2 / 2)
        k4 = h * df(t + h, w + k3)

        w = w + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = a + i * h
        print("{:^4} | {:^4} | {:^20} | {:^20} | {:^20}".format(i, round(t, 2), f_real(t), w, abs(f_real(t) - w)))

    print("\n")
    return w


if __name__ == "__main__":
    y0 = .5
    b = 2
    a = 0
    print("El valor aproximado de y en t = " + str(b) + " es " + str(runge_kutta_4(a, b, y0, 10)))
