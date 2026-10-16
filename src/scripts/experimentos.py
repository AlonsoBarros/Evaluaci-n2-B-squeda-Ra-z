# Corre los 6 métodos sobre las 6 funciones y guarda los CSV en data/
import os
import numpy as np
from funciones import FUNCIONES, TOL, MAX_ITER
from metodos import (biseccion, falsa_posicion, punto_fijo, secante, newton,
                     newton_mejorado)

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
ORDEN = ["Bisección", "Falsa posición", "Punto fijo", "Secante", "Newton",
         "Newton mejorado"]


def correr_metodos(fn, a, b, x0, x1):
    f = fn["f"]
    resultados = []
    resultados.append(biseccion(f, a, b, TOL, MAX_ITER))
    resultados.append(falsa_posicion(f, a, b, TOL, MAX_ITER))
    resultados.append(punto_fijo(fn["g"], x0, TOL, MAX_ITER))
    resultados.append(secante(f, x0, x1, TOL, MAX_ITER))
    resultados.append(newton(f, fn["df"], x0, TOL, MAX_ITER))
    resultados.append(newton_mejorado(f, fn["df"], fn["d2f"], x0, TOL, MAX_ITER))
    return resultados


def intervalo(fn):
    if fn["a"] is None:
        return fn["x0"], fn["x1"]
    return fn["a"], fn["b"]


def correr_todo():
    todos = {}
    for fn in FUNCIONES:
        a, b = intervalo(fn)
        todos[fn["id"]] = correr_metodos(fn, a, b, fn["x0"], fn["x1"])
    return todos


def guardar_curvas():
    for fn in FUNCIONES:
        x = np.linspace(fn["rango"][0], fn["rango"][1], 200)
        archivo = open(os.path.join(DATA, fn["id"] + ".csv"), "w", encoding="utf-8")
        archivo.write("x,f(x)\n")
        for xi in x:
            archivo.write(f"{xi},{fn['f'](xi)}\n")
        archivo.close()


def guardar_resumen(todos):
    resumen = open(os.path.join(DATA, "resumen_convergencia.csv"), "w", encoding="utf-8")
    resumen.write("funcion,metodo,convergio,iteraciones,raiz,error_abs,mensaje\n")
    historial = open(os.path.join(DATA, "historial_iteraciones.csv"), "w", encoding="utf-8")
    historial.write("funcion,metodo,n,x,paso\n")
    for fn in FUNCIONES:
        for r in todos[fn["id"]]:
            if r["iteraciones"] > 0:
                error = abs(r["raiz"] - fn["raiz"])
            else:
                error = ""
            mensaje = r["mensaje"].replace(",", " -")
            resumen.write(
                f"{fn['nombre']},{r['metodo']},{r['convergio']},"
                f"{r['iteraciones']},{r['raiz']},{error},{mensaje}\n"
            )
            for n, x, paso in r["historial"]:
                historial.write(f"{fn['nombre']},{r['metodo']},{n},{x},{paso}\n")
    resumen.close()
    historial.close()


def guardar_sensibilidad():
    archivo = open(os.path.join(DATA, "sensibilidad.csv"), "w", encoding="utf-8")
    archivo.write("funcion,ambiente,metodo,convergio,iteraciones,raiz\n")
    for fn in FUNCIONES:
        a, b = intervalo(fn)
        if fn["doble"]:
            casos = [("x0=1.2", a, b, fn["x0"], fn["x1"]),
                     ("x0=0.5", a, b, 0.5, 0.6),
                     ("x0=1.9", a, b, 1.9, 2.0),
                     ("x0=3.0", a, b, 3.0, 3.1)]
        else:
            ancho = b - a
            a2 = max(a - 0.5 * ancho, fn["dom_min"])
            b2 = b + 0.5 * ancho
            casos = [("intervalo original", a, b, fn["x0"], fn["x1"]),
                     ("intervalo ampliado", a2, b2, a, a + 0.1),
                     ("x0 en el extremo a", a, b, a, a + 0.1),
                     ("x0 en el extremo b", a, b, b, b + 0.1)]
        for ambiente, a_, b_, x0, x1 in casos:
            for r in correr_metodos(fn, a_, b_, x0, x1):
                archivo.write(
                    f"{fn['nombre']},{ambiente},{r['metodo']},"
                    f"{r['convergio']},{r['iteraciones']},{r['raiz']}\n"
                )
    archivo.close()


if __name__ == "__main__":
    os.makedirs(DATA, exist_ok=True)
    todos = correr_todo()
    guardar_curvas()
    guardar_resumen(todos)
    guardar_sensibilidad()
    print("CSV generados en", DATA)
