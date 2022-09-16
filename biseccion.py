from sympy import lambdify
from sympy.abc import x


def validarCambioSigno(f, a, b):
    return (f(a) * f(b) < 0)


def imprimir_fmt_tabla(iter, val_medio, fa, fm, fb):
    print("{:^3} | {:^23} | {:^23} | {:^23} | {:^23}".format(iter, val_medio, fa, fm, fb))


n = 0
a = 0
b = 2
f = lambdify([x], x**2 - 2)
error = 1 * 10 ** -5
while validarCambioSigno(f, a, b):
    if (n == 0):
        imprimir_fmt_tabla('N', 'Medio', 'f(a)', 'f(medio)', 'f(b)')
        print("-" * 110)
    medio = (a + b) / 2
    n += 1
    imprimir_fmt_tabla(n, str(medio), str(f(a)), str(f(medio)), str(f(b)))
    if abs(f(medio)) < error:
        break
    if validarCambioSigno(f, a, medio):
        b = medio
    else:
        a = medio
if n == 0:
    print("Intervalo no Valido")
