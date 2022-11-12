from math import e, sqrt


def f(x):
    return x ** 4 + 5 * x ** 2 - 3 * x - 7


def pol_base(i, x):
    return x ** i


def integral_base(n):
    return 1 / (n + 1) - (-1) ** (n + 1) / (n + 1)


def gauss_jordan(mat, n):

    for i in range(n):
        if mat[i][i] == 0.0:
            print('ERROR: Division por Cero')
            return

        for j in range(n):
            if i != j:
                p = mat[j][i] / mat[i][i]

                for k in range(n + 1):
                    mat[j][k] = mat[j][k] - p * mat[i][k]
    return mat


def hallar_solucion(mat):

    n = len(mat[0]) - 1
    x = []
    a = gauss_jordan(mat, n)

    for i in range(n):
        x.append(a[i][n] / a[i][i])

    return x


def gauss_lobatto(n, xi):

    resul = 0
    xi.insert(0, - 1)
    xi.append(1)
    sis = sistema_ecuaciones(n, xi)
    a_i = hallar_solucion(sis)
    for i in range(n + 1):
        resul = resul + a_i[i] * f(xi[i])

    return resul


def sistema_ecuaciones(n, xi):
    ecs = []

    for i in range(n + 1):
        ec_i = []
        for k in range(n + 1):
            ec_i.append(pol_base(i, xi[k]))
        ec_i.append(integral_base(i))
        ecs.append(ec_i)

    return ecs


if __name__ == "__main__":
    print("El metodo de Gauss-Lobatto aproxima, con n = 3, el valor de la integral a: " + str(gauss_lobatto(3, [-1/3, 1/3])))

    print("El metodo de Gauss-Lobatto aproxima, con n = 4, el valor de la integral a: "
          + str(gauss_lobatto(4, [-sqrt(3/5), 0, sqrt(3/5)])))
