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

class Nodo:
    def __init__(self, tipo, nivel, izq=None, der=None):
        self.tipo = tipo
        self.nivel = nivel
        self.izq = izq
        self.der = der

# Definir los tipos de Pokémon
tipos = ["Agua", "Fuego", "Tierra", "Electrico", "Normal", "Fantasma"]

# Generar los Pokémon
pokemon = [Nodo(random.choice(tipos), random.randint(1, 1000)) for _ in range(800)]

# Crear las tablas hash
hash_nivel = {i: None for i in range(1000)}
hash_tipo = {t: None for t in tipos}

# Rellenar las tablas hash
for p in pokemon:
    nivel = p.nivel % 1000
    if hash_nivel[nivel] is None:
        hash_nivel[nivel] = p
    else:
        nodo_actual = hash_nivel[nivel]
        while nodo_actual.der is not None:
            nodo_actual = nodo_actual.der
        nodo_actual.der = p

    tipo = p.tipo
    if hash_tipo[tipo] is None:
        hash_tipo[tipo] = p
    else:
        nodo_actual = hash_tipo[tipo]
        while nodo_actual.der is not None:
            nodo_actual = nodo_actual.der
        nodo_actual.der = p

# Encontrar y eliminar el Pokémon Fantasma de nivel 187
nodo_actual = hash_nivel[187]
if nodo_actual is not None and nodo_actual.tipo == "Fantasma":
    hash_nivel[187] = nodo_actual.der
else:
    while nodo_actual is not None and nodo_actual.der is not None:
        if nodo_actual.der.tipo == "Fantasma":
            nodo_actual.der = nodo_actual.der.der
            break
        nodo_actual = nodo_actual.der

# Obtener los Pokémon para las misiones
pokemon_asalto = []
nodo_actual = hash_nivel[78]
while nodo_actual is not None:
    pokemon_asalto.append(nodo_actual)
    nodo_actual = nodo_actual.der

pokemon_exploracion = []
nodo_actual = hash_nivel[37]
while nodo_actual is not None:
    pokemon_exploracion.append(nodo_actual)
    nodo_actual = nodo_actual.der

# Obtener los Pokémon para las misiones del Profesor Oak
pokemon_oak_exploracion = []
nodo_actual = hash_tipo["Tierra"]
while nodo_actual is not None:
    pokemon_oak_exploracion.append(nodo_actual)
    nodo_actual = nodo_actual.der

pokemon_oak_exterminacion = []
nodo_actual = hash_tipo["Fuego"]
while nodo_actual is not None:
    pokemon_oak_exterminacion.append(nodo_actual)
    nodo_actual = nodo_actual.der
