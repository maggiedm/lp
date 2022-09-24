from math import *

def calculo_i0_a ():
    return round(log(11/10),3)

def calculo_in_a (n, in_anterior):
    return (1/n - 10*(in_anterior))

def calculo_i_25_b ():
    return 1/275

def calculo_in_anterior_b (n, i_n):
    return (1/10 * (1/n - i_n))

def imprimir_fmt_tabla (col_a, col_b):
    print("{:^4} | {:^20}".format(col_a, col_b))

def punto_a():
    resultados_a = list()
    resultados_a.append(calculo_i0_a())

    print("-" * 30)
    print("{:^30}".format("RESULTADOS A"))
    print("-" * 30)
    imprimir_fmt_tabla('n', 'I_n')
    print("-" * 30)

    imprimir_fmt_tabla(0, resultados_a[-1])
    for n in range(1, 26):
        i_n = calculo_in_a(n, resultados_a[-1])
        resultados_a.append(i_n)
        imprimir_fmt_tabla(n, resultados_a[-1])

def punto_b():
    resultados_b = list()
    resultados_b.append(calculo_i_25_b())

    print("-" * 30)
    print("{:^30}".format("RESULTADOS B"))
    print("-" * 30)
    imprimir_fmt_tabla('n', 'I_n')
    print("-" * 30)
    imprimir_fmt_tabla(25, resultados_b[-1])
    resultados_b.append(calculo_i_25_b())
    imprimir_fmt_tabla(24, resultados_b[-1])

    for n in range(24, 0, -1):
        i_n = calculo_in_anterior_b(n, resultados_b[-1])
        resultados_b.append(i_n)
        imprimir_fmt_tabla(n - 1, resultados_b[-1])

if __name__ == "__main__":

    punto_a()

    print("\n"*3)

    punto_b()