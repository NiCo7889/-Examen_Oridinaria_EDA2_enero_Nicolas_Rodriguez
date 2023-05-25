"""
Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-PokéBolas. Este problema consiste en ubicar 
n Pokémon en una red de gimnasios de tamaño n x n, sin que los mismos se enfrenten. Recuerda que un Pokémon puede moverse de manera horizontal, vertical y diagonal, además 
podemos ver una solución al problema de los 4 Pokémon. Nótese que una parte importante para resolver un problema es de qué manera representar la solución, para este caso 
particular usamos un vector de n posiciones (gimnasios) y el valor almacenado representa la fila donde se ubica dicho Pokémon.

 
Cuando hayas entendido el problema y tengas una solución en mente, desarrolla un algoritmo que permita hallar al menos una solución para distintas cantidades de Pokémon, 
y luego completa la siguiente tabla.

n-pokeballs / Soluciones distintas / Todas las soluciones / Una solución
1 / 1 / 1 / [0]
2 / 0 / 0 / [NA]
3 / 0 / 0 / [NA]
4 / 1 / 2 / [1, 4, 0, 3]
5 / 2 / 10 / [0, 0, 1, 3, 0]
6 / 1 / 4 / []
7 / 6 / 40 / []
8 / 12 / 92 / []
9 / 46 / 352 / []
10 / 92 / 724 / []
15 / 285 053 / 2 279 184 / []
"""


class Nodo:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.adyacentes = []

    def agregar_adyacente(self, nodo):
        self.adyacentes.append(nodo)

def isSafe(pokemons, fila, columna):
    for pokemon in pokemons:
        if (
            pokemon.fila == fila or
            pokemon.columna == columna or
            abs(pokemon.fila - fila) == abs(pokemon.columna - columna)
        ):
            return False
    return True

def encontrar_soluciones(n):
    soluciones_distintas = 0
    todas_soluciones = []
    una_solucion = []

    def backtrack(fila):
        nonlocal soluciones_distintas, todas_soluciones, una_solucion

        if fila == n:
            soluciones_distintas += 1
            todas_soluciones.append([(p.fila, p.columna) for p in una_solucion])
        else:
            for columna in range(n):
                if isSafe(una_solucion, fila, columna):
                    nodo = Nodo(fila, columna)
                    for p in una_solucion:
                        nodo.agregar_adyacente(p)
                    una_solucion.append(nodo)
                    backtrack(fila + 1)
                    una_solucion.pop()

    backtrack(0)

    return soluciones_distintas, todas_soluciones

# tabla = {
#     1: (1, [[(0, 0)]]),
#     2: (0, []),
#     3: (0, []),
#     4: (1, [[(0, 1), (1, 3), (2, 0), (3, 2)]]),
#     5: (2, [
#         [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)],
#         [(0, 0), (1, 3), (2, 1), (3, 4), (4, 2)]
#     ]),
#     6: (1, [[(0, 0), (1, 2), (2, 4), (3, 1), (4, 3), (5, 5)]]),
#     7: (6, [
#         [(0, 0), (1, 2), (2, 4), (3, 6), (4, 1), (5, 3), (6, 5)],
#         [(0, 0), (1, 3), (2, 6), (3, 2), (4, 5), (5, 1), (6, 4)],
#         [(0, 0), (1, 4), (2, 1), (3, 5), (4, 2), (5, 6), (6, 3)],
#         [(0, 0), (1, 5), (2, 3), (3, 1), (4, 6), (5, 4), (6, 2)],
#         [(0, 0), (1, 6), (2, 2), (3, 5), (4, 1), (5, 4), (6, 0)],
#         [(0, 0), (1, 6), (2,
