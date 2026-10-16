#cada función tiene su propia función f(x), su derivada df(x), su segunda derivada d2f(x) y su función g(x) para el método de punto fijo
import numpy as np

TOL = 1e-6        # tolerancia, 1x10 elevado a -6 
MAX_ITER = 100    # tope de iteraciones, por si no tiene raíz, para evitar bucles infinitos


# raíz simple: x^3 - x - 2 //  x = (x+2)^(1/3)
def f1(x):   return x**3 - x - 2
def df1(x):  return 3 * x**2 - 1
def d2f1(x): return 6 * x
def g1(x):   return np.cbrt(x + 2)         

# raíz doble: (x-2)^2 //x = (x+2)/2
def f2(x):   return (x - 2)**2
def df2(x):  return 2 * (x - 2)
def d2f2(x): return 2.0 + 0 * x
def g2(x):   return (x + 2) / 2             
# Logarítmica: ln(x) + x - 4 // x = 4 - ln(x)
def f3(x):   return np.log(x) + x - 4
def df3(x):  return 1 / x + 1
def d2f3(x): return -1 / x**2
def g3(x):   return 4 - np.log(x)           
# Exponencial: e^(-x) - x //  x = e^(-x)
def f4(x):   return np.exp(-x) - x
def df4(x):  return -np.exp(-x) - 1
def d2f4(x): return np.exp(-x)
def g4(x):   return np.exp(-x)              
#Trigonométrica: cos(x) - x  //  x = cos(x)
def f5(x):   return np.cos(x) - x
def df5(x):  return -np.sin(x) - 1
def d2f5(x): return -np.cos(x)
def g5(x):   return np.cos(x)       
#Mixta: sqrt(x) - cos(x) //  x = x - f(x)/2
def f6(x):   return np.sqrt(x) - np.cos(x)
def df6(x):  return 1 / (2 * np.sqrt(x)) + np.sin(x)
def d2f6(x): return -1 / (4 * x**1.5) + np.cos(x)
def g6(x):   return x - 0.5 * (np.sqrt(x) - np.cos(x))  


FUNCIONES = [
    {
        "id": "f1_polinomica",
        "nombre": "x^3 - x - 2",
        "categoria": "raíz simple",
        "f": f1,
        "df": df1,
        "d2f": d2f1,
        "g": g1,
        "a": 1.0,
        "b": 2.0,
        "x0": 1.5,
        "x1": 1.6,
        "raiz": 1.5213797068045676,
        "doble": False,
        "dom_min": -np.inf,
        "rango": (0.8, 2.2)
    },
    {
        "id": "f2_raiz_doble",
        "nombre": "(x - 2)^2",
        "categoria": "raíz doble",
        "f": f2,
        "df": df2,
        "d2f": d2f2,
        "g": g2,
        "a": None,
        "b": None,
        "x0": 1.2,
        "x1": 1.5,
        "raiz": 2.0,
        "doble": True,
        "dom_min": -np.inf,
        "rango": (0.5, 3.5)
    },
    {
        "id": "f3_logaritmica",
        "nombre": "ln(x) + x - 4",
        "categoria": "Logarítmica",
        "f": f3,
        "df": df3,
        "d2f": d2f3,
        "g": g3,
        "a": 2.0,
        "b": 3.0,
        "x0": 2.5,
        "x1": 2.6,
        "raiz": 2.926271062443501,
        "doble": False,
        "dom_min": 1e-3,
        "rango": (1.5, 3.5)
    },
    
    {
        "id": "f4_exponencial",
        "nombre": "e^(-x) - x",
        "categoria": "Exponencial",
        "f": f4,
        "df": df4,
        "d2f": d2f4,
        "g": g4,
        "a": 0.0,
        "b": 1.0,
        "x0": 0.5,
        "x1": 0.6,
        "raiz": 0.5671432904097839,
        "doble": False,
        "dom_min": -np.inf,
        "rango": (-0.5, 1.5)
    },
    {
        "id": "f5_trigonometrica",
        "nombre": "cos(x) - x",
        "categoria": "Trigonométrica",
        "f": f5,
        "df": df5,
        "d2f": d2f5,
        "g": g5,
        "a": 0.0,
        "b": 1.0,
        "x0": 0.5,
        "x1": 0.6,
        "raiz": 0.7390851332151607,
        "doble": False,
        "dom_min": -np.inf,
        "rango": (-0.5, 1.5)
    },

    {
        "id": "f6_mixta",
        "nombre": "sqrt(x) - cos(x)",
        "categoria": "Mixta",
        "f": f6,
        "df": df6,
        "d2f": d2f6,
        "g": g6,
        "a": 0.1,
        "b": 1.0,
        "x0": 0.5,
        "x1": 0.6,
        "raiz": 0.6417143708728827,
        "doble": False,
        "dom_min": 1e-3,
        "rango": (0.05, 1.2)

    },
]