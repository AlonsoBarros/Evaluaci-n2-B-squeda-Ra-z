# Cada método tiene su propia función de iteración, que recibe la función f(x) y sus derivadas según corresponda, y devuelve un diccionario con el resultado final y el historial de iteraciones
import numpy as np


# Arma el diccionario de salida común a todos los métodos.
def _resultado(metodo, historial, convergio, mensaje):
    if len(historial) > 0:
        raiz = historial[-1][1]
    else:
        raiz = np.nan
    return dict(metodo=metodo, raiz=raiz, iteraciones=len(historial),
                convergio=convergio, mensaje=mensaje, historial=historial)


# Bisección, necesita f(a)*f(b) < 0 teorema de Bolzano
def biseccion(f, a, b, tol, max_iter):
    if f(a) * f(b) > 0:
        return _resultado("Bisección", [], False, "No aplica: sin cambio de signo")
    historial = []
    for n in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        historial.append((n, c, (b - a) / 2))
        if abs(fc) < tol or (b - a) / 2 < tol:
            return _resultado("Bisección", historial, True, "correcto")
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return _resultado("Bisección", historial, False, "No convergió en max_iter")


# Falsa posición, necesita cambio de signo en [a, b]
def falsa_posicion(f, a, b, tol, max_iter):
    if f(a) * f(b) > 0:
        return _resultado("Falsa posición", [], False, "sin cambio de signo")
    historial = []
    c_actual = a
    for n in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        historial.append((n, c, abs(c - c_actual)))
        if abs(fc) < tol or abs(c - c_actual) < tol:
            return _resultado("Falsa posición", historial, True, "correcto")
        if fa * fc<0:
            b=c
        else:
            a=c
        c_actual=c
    return _resultado("Falsa posición", historial, False, "bucle infinito, no convergió en max_iter")


# Punto fijo: x_(n+1) = g(x_n). Converge si |g'(x)| < 1 cerca de la raíz
def punto_fijo(g, x0, tol, max_iter):
    historial = []
    x = x0
    for n in range(1, max_iter + 1):
        x_nuevo = g(x)
        historial.append((n, x_nuevo, abs(x_nuevo - x)))
        if abs(x_nuevo - x) < tol:
            return _resultado("Punto fijo", historial, True, "correcto")
        x=x_nuevo
    return _resultado("Punto fijo", historial, False, "bucle infinito, no convergió en max_iter")


# Secante: como Newton, pero la derivada se aproxima con dos puntos
def secante(f, x0, x1, tol, max_iter):
    historial = []
    for n in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        historial.append((n, x2, abs(x2 - x1)))
        if abs(f(x2)) < tol or abs(x2 - x1) < tol:
            return _resultado("Secante", historial, True, "correcto")
        x0, x1 = x1, x2
    return _resultado("Secante", historial, False, "bucle infinito, no convergió en max_iter")


# Newton-Raphson, x_(n+1) = x_n - f(x_n)/f'(x_n).
def newton(f, df, x0, tol, max_iter):
    historial = []
    x = x0
    for n in range(1, max_iter + 1):
        d = df(x)
        x_nuevo = x - f(x) / d
        historial.append((n, x_nuevo, abs(x_nuevo - x)))
        if abs(f(x_nuevo)) < tol or abs(x_nuevo - x) < tol:
            return _resultado("Newton", historial, True, "correcto")
        x=x_nuevo
    return _resultado("Newton", historial, False, "bucle infinito, no convergió en max_iter")


# Newton-Raphson modificado, f''. x_(n+1) = x_n - f*f' / (f'^2 - f*f'')
def newton_mejorado(f, df, d2f, x0, tol, max_iter):
    historial = []
    x = x0
    for n in range(1, max_iter + 1):
        fx = f(x)
        d1 = df(x)
        d2 = d2f(x)
        D = d1**2 - fx * d2
        x_nuevo = x - fx * d1 / D
        historial.append((n, x_nuevo, abs(x_nuevo - x)))
        if abs(f(x_nuevo)) < tol or abs(x_nuevo - x) < tol:
            return _resultado("Newton mejorado", historial, True, "correcto")
        x = x_nuevo
    return _resultado("Newton mejorado", historial, False, "bucle infinito, no convergió en max_iter")