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

# Definir los tipos de Pokémon
tipos = ["Agua", "Fuego", "Tierra", "Electrico", "Normal", "Fantasma"]

# Generar los Pokémon
pokemon = [{"tipo": random.choice(tipos), "nivel": random.randint(1, 1000)} for _ in range(800)]

# Crear las tablas hash
hash_nivel = {i: [] for i in range(1000)}
hash_tipo = {t: [] for t in tipos}

# Rellenar las tablas hash
for p in pokemon:
    hash_nivel[p["nivel"] % 1000].append(p)
    hash_tipo[p["tipo"]].append(p)

# Encontrar y eliminar el Pokémon Fantasma de nivel 187
if 187 in hash_nivel:
    hash_nivel[187] = [p for p in hash_nivel[187] if p["tipo"] != "Fantasma"]

# Obtener los Pokémon para las misiones
pokemon_asalto = hash_nivel[78]
pokemon_exploracion = hash_nivel[37]

# Obtener los Pokémon para las misiones del Profesor Oak
pokemon_oak_exploracion = hash_tipo["Tierra"]
pokemon_oak_exterminacion = hash_tipo["Fuego"]
