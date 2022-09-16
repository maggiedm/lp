from math import *


def calc_h(i):
    return pow(2, -i)


def calculo_exacto(x):
    return exp(x)


def calculo_aproximado(x, i):
    h = calc_h(i)
    f_x = (exp(x + h) - exp(x - h)) / (2 * h)
    return f_x


def calculo_err_absoluto(real, rep):
    return abs(rep - real)


def calculo_err_relativo(real, rep):
    return calculo_err_absoluto(real, rep) / abs(real)


def truncar(numero, cant_decimales):
    return trunc(numero * pow(10, cant_decimales)) / pow(10, cant_decimales)


def imprimir_fmt_tabla(col_a, col_b, col_c, col_d, col_e, col_f, col_g, col_h):
    print("{:^15} | {:^20} | {:^10} | {:^25} | {:^25} | {:^10} | {:^30} | {:^25} ".format(col_a, col_b, col_c, col_d,
                                                                                          col_e, col_f, col_g, col_h))


result_exacto = calculo_exacto(0)
cant_decimales = 5
imprimir_fmt_tabla("Valor Real", "Valor Representado",
                   "Redondeado", "Error Absoluto Redondeo", "Error Relativo Redondeo",
                   "Truncado", "Error Absoluto Truncamiento", "Error Relativo Truncamiento")
print("-" * 185)
for i in range(1, 31):
    f_0 = calculo_aproximado(0, i)
    redondeado = round(f_0, cant_decimales)
    truncado = truncar(f_0, cant_decimales)
    imprimir_fmt_tabla(result_exacto, f_0,
                       redondeado, calculo_err_absoluto(result_exacto, redondeado),
                       calculo_err_relativo(result_exacto, redondeado),
                       truncado, calculo_err_absoluto(result_exacto, truncado),
                       calculo_err_relativo(result_exacto, truncado))
