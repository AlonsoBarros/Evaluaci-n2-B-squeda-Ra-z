import os
import numpy as np
import matplotlib.pyplot as plt
from funciones import FUNCIONES
from experimentos import correr_todo, ORDEN

ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")

# grafico de la función f(x) con su raíz y límites a y b
def grafico_funcion(fn):
    x = np.linspace(fn["rango"][0], fn["rango"][1], 400)
    y = fn["f"](x)
    plt.figure(figsize=(7, 4))
    plt.plot(x, y, label="f(x) = " + fn["nombre"])
    plt.axhline(0, color="gray", linewidth=0.8)
    plt.plot(fn["raiz"], 0, "ro", label=f"raíz = {fn['raiz']:.6f}")
    if fn["doble"]:
        plt.text(fn["raiz"], 0.5, "Raíz doble (tangencia al eje x)", color="red")
    else:
        plt.axvline(fn["a"], color="green", linestyle="--", label="Límite a ")
        plt.axvline(fn["b"], color="green", linestyle="--", label="Límite b")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(fn["categoria"] + ": " + fn["nombre"])
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS, "funcion_" + fn["id"] + ".png"), dpi=130)
    plt.close()


# grafico de convergencia: |x_n - raíz| 
def grafico_convergencia(fn, resultados):
    plt.figure(figsize=(7, 4))
    for r in resultados:
        if len(r["historial"]) == 0:
            continue                       
        iteraciones = []
        errores = []
        for iteracion in r["historial"]:
            iteraciones.append(iteracion[0])
            errores.append(max(abs(iteracion[1] - fn["raiz"]), 1e-17))
        plt.semilogy(iteraciones, errores, marker="o", markersize=3, label=r["metodo"])
    plt.axhline(1e-6, color="gray", linestyle="--", linewidth=0.8, label="tolerancia = 1e-6")
    plt.xlabel("iteración")
    plt.ylabel("|x - raiz|")
    plt.title("Convergencia: " + fn["nombre"])
    plt.legend(fontsize=8)
    plt.grid(alpha=0.3, which="both")
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS, "convergencia_" + fn["id"] + ".png"), dpi=130)
    plt.close()


#grafico de resumen: barras con el número de iteraciones hasta converger para cada método y función
def grafico_resumen(todos):
    plt.figure(figsize=(11, 5))
    ancho = 0.13
    posiciones = np.arange(len(FUNCIONES))
    for i in range(len(ORDEN)):
        valores = []
        for fn in FUNCIONES:
            r = todos[fn["id"]][i]         
            if r["convergio"]:
                valores.append(r["iteraciones"])
            else:
                valores.append(0)          
        barras = plt.bar(posiciones + (i - 2.5) * ancho, valores, ancho, label=ORDEN[i]) 
        for j in range(len(valores)):
            if valores[j] == 0:
                plt.text(barras[j].get_x() + ancho / 2, 0.3, "No converge",
                         ha="center", fontsize=7, rotation=90)
    nombres = []
    for fn in FUNCIONES:
        nombres.append(fn["nombre"])
    plt.xticks(posiciones, nombres, fontsize=8)
    plt.ylabel("iteraciones hasta converger")
    plt.title("Iteraciones por método y función")
    plt.legend(fontsize=8)
    plt.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS, "resumen_iteraciones.png"), dpi=130)
    plt.close()


if __name__ == "__main__": # función principal, si se ejecuta este script directamente, genera todos los gráficos
    os.makedirs(ASSETS, exist_ok=True)
    todos = correr_todo()
    for fn in FUNCIONES:
        grafico_funcion(fn)
        grafico_convergencia(fn, todos[fn["id"]])
    grafico_resumen(todos)
    print("Gráficos generados en", ASSETS)