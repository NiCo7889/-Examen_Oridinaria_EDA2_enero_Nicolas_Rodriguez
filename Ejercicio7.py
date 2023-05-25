"""
El Profesor Oak le encarga desarrollar los algoritmos para organizar los Pokemon cumpliendo con las siguientes demandas:

Deberá generar 800 Pokemon siguiendo el formato del primer ejercicio contemplando los siguientes tipos:
- Agua, Fuego, Tierra, Electrico, Normal, Fantasma y los niveles generados de manera aleatoria;
Deberá cargar los Pokemon generados en dos tablas hash encadenadas, en la primera se deberá agrupar de acuerdo con los tres últimos dígitos del nivel y en la segunda a partir 
de las iniciales del tipo;
Determinar si el Pokemon Fantasma de nivel 187 está cargado para poder quitarlo porque es un traidor desertor.
Ahora obtenga todos los Pokemon terminados en 78 para asignarlos a una misión de asalto y a los terminados en 37 para una misión de exploración;
Ahora obtenga los Pokemon de tipo Tierra para que custodien al Profesor Oak en una misión de exploración al Bosque Verdanturf y los de tipo Fuego para una misión de 
exterminación en Cueva Lava.
"""


import random

class Pokemon:
    def __init__(self, tipo, nivel):
        self.tipo = tipo
        self.nivel = nivel
        self.vecinos = []

def generar_grafo_pokemon(n):
    tipos = ["Agua", "Fuego", "Tierra", "Electrico", "Normal", "Fantasma"]
    pokemon = [Pokemon(random.choice(tipos), random.randint(1, 1000)) for _ in range(n)]
    grafo = {}

    for i in range(n):
        grafo[i] = []
        for j in range(n):
            if i != j:
                if pokemon[i].tipo != pokemon[j].tipo and abs(pokemon[i].nivel - pokemon[j].nivel) > 100:
                    grafo[i].append(j)
    
    return pokemon, grafo

def obtener_pokemon_por_nivel(pokemon, nivel):
    return [p for p in pokemon if p.nivel % 100 == nivel]

def obtener_pokemon_por_tipo(pokemon, tipo):
    return [p for p in pokemon if p.tipo == tipo]

def eliminar_pokemon_fantasma(pokemon, grafo, nivel):
    for i in range(len(pokemon)):
        if pokemon[i].tipo == "Fantasma" and pokemon[i].nivel % 1000 == nivel:
            for vecino in grafo[i]:
                grafo[vecino].remove(i)
            del grafo[i]
            del pokemon[i]
            break

def obtener_pokemon_para_mision(pokemon, grafo, terminacion):
    terminacion = terminacion % 100
    indices = [i for i in range(len(pokemon)) if pokemon[i].nivel % 100 == terminacion]
    return [pokemon[i] for i in indices if len(grafo[i]) == 0]


if __name__ == "__main__":

    # Generar los Pokémon y el grafo
    n = 800
    pokemon, grafo = generar_grafo_pokemon(n)

    # Tabla hash para agrupar los Pokémon por los tres últimos dígitos del nivel
    hash_nivel = {}
    for i in range(n):
        nivel = pokemon[i].nivel % 1000
        if nivel not in hash_nivel:
            hash_nivel[nivel] = []
        hash_nivel[nivel].append(pokemon[i])

    # Tabla hash para agrupar los Pokémon por tipo
    hash_tipo = {}
    for i in range(n):
        tipo = pokemon[i].tipo
        if tipo not in hash_tipo:
            hash_tipo[tipo] = []
        hash_tipo[tipo].append(pokemon[i])

    # Eliminar el Pokémon Fantasma de nivel 187 si está presente
    eliminar_pokemon_fantasma(pokemon, grafo, 187)

    # Obtener los Pokémon para las misiones de asalto y exploración
    pokemon_asalto = obtener_pokemon_para_mision(pokemon, grafo, 78)
    pokemon_exploracion = obtener_pokemon_para_mision(pokemon, grafo, 37)

    # Obtener los Pokémon de tipo Tierra para la misión de exploración al Bosque Verdanturf
    pokemon_oak_exploracion = obtener_pokemon_por_tipo(pokemon, "Tierra")

    # Obtener los Pokémon de tipo Fuego para la misión de exterminación en Cueva Lava
    pokemon_oak_exterminacion = obtener_pokemon_por_tipo(pokemon, "Fuego")

    # Imprimir los resultados
    print("Pokémon para la misión de asalto:")
    for p in pokemon_asalto:
        print(p.tipo, p.nivel)

    print("")

    print("Pokémon para la misión de exploración:")
    for p in pokemon_exploracion:
        print(p.tipo, p.nivel)

    print("")

    print("Pokémon de tipo Tierra para la misión de exploración al Bosque Verdanturf:")
    for p in pokemon_oak_exploracion:
        print(p.tipo, p.nivel)

    print("")

    print("Pokémon de tipo Fuego para la misión de exterminación en Cueva Lava:")
    for p in pokemon_oak_exterminacion:
        print(p.tipo, p.nivel)

