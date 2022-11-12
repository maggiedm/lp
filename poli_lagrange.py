def calcular_base_li(li, xi, xk):
    if len(li) == 0:
        li = "[ (x - (" + str(xk) + ")) / " + str(xi - xk) + " ]"
    else:
        li = li + " * [ (x - (" + str(xk) + ")) / " + str(xi - xk) + "]"

    return li


def calcular_polinomio(pol, li, yi):
    if len(pol) == 0:
        pol = pol + li + " * (" + str(yi) + ")"
    else:
        pol = pol + " + \n\t\t + " + li + " * (" + str(yi) + ")"

    return pol


def lagrange(x, y, a):
    s = 0
    n = len(x)

    if len(x) != len(y):
        print("Error: tiene que haber igual cantidad de puntos de x que de y")
        return
    l = [""] * n
    pol = ""

    for i in range(n):
        p = 1
        for k in range(n):
            if i != k:
                p = p * (a - x[k]) / (x[i] - x[k])
                l[i] = calcular_base_li(l[i], x[i], x[k])
        s = s + p * y[i]
        pol = calcular_polinomio(pol, l[i], y[i])

    print("El polinomio interpolador es: \n\tP(x) = " + pol)
    print("\nEl valor interpolado de la función en %.5f es %.5f" % (a, s))


if __name__ == "__main__":
    x = [-1.5, -0.75, 0, 0.75, 1.5]
    y = [-14.1014, -0.931596, 0, 0.931596, 14.1014]
    a = 0.5

    lagrange(x, y, a)
