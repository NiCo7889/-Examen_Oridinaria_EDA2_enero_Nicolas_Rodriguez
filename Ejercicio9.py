"""
Eres uno de los líderes de gimnasio (Gym Leader) de una importante organización Pokémon internacional. Uno de los altos miembros del Alto Mando te informa que el Campeón de la Liga Pokémon ha viajado desde EEUU a Barcelona y ha convocado un torneo de alto nivel para esta tarde a las 19:30 en Barcelona. Han consultado la lista de vuelos desde Madrid (donde estás tú) y han llegado a la conclusión de que tienes que tomar un vuelo que parte de Madrid dentro de 2 horas y cierra su facturación 20 minutos antes.

¿Qué duración mínima tiene la misión? ¿Llega el líder a facturar a tiempo dentro de los 100 minutos disponibles? Si no es así, revisa las dependencias, seguro que estás indicando relaciones basadas en las restricciones de los recursos.

Coloca primero la ruta crítica y sus recursos necesarios. A continuación, coloca y reajusta el resto de las actividades dentro de su holgura y define quién hará qué actividad.


Aquí tienes la tabla generada a partir de los datos proporcionados:

TAREA / DESCRIPCIÓN / DURACIÓN
A / Llamar a la agencia de viajes, reservar una plaza y recibir la conformidad. / 20'
B / Llamar a casa para que preparen a los Pokémon. / 5'

C / Preparar a los Pokémon. / 40'

D / La agencia de viajes prepara el billete. / 10'

E / Ir desde el gimnasio a la agencia de viajes a recoger los billetes. / 5'

F / Recoger los billetes de la agencia y llevarlos al gimnasio. / 10'

G / Ir desde el gimnasio a casa a recoger a los Pokémon. / 20'

H / Recoger a los Pokémon y llevarlos al gimnasio. / 25'

I / Conversar con los colaboradores para obtener información sobre qué Pokémon llevar en este viaje. / 35'

J / Seleccionar los Pokémon más fuertes y dejar instrucciones para el tiempo de la ausencia. / 25'

K / Reunir los objetos más importantes para llevar en este viaje. / 15'

L / Organizar los objetos. / 5'

M / Viajar al aeropuerto y facturar. / 25'
"""


tareas = {
    'A': 20,
    'B': 5,
    'C': 40,
    'D': 10,
    'E': 5,
    'F': 10,
    'G': 20,
    'H': 25,
    'I': 35,
    'J': 25,
    'K': 15,
    'L': 5,
    'M': 25,
}

secuencias = [
    ['A', 'D', 'E', 'F'],
    ['B', 'C', 'G', 'H'],
    ['I', 'J'],
    ['K', 'L'],
    ['M']
]

def tiempo_total(secuencia):
    return sum(tareas[tarea] for tarea in secuencia)

def tarea_mas_larga(secuencia):
    return max(secuencia, key=lambda tarea: tareas[tarea])

for secuencia in secuencias:
    print(f"Secuencia {secuencia}:")
    print(f"  Tiempo total: {tiempo_total(secuencia)} minutos")
    print(f"  Tarea más larga: {tarea_mas_larga(secuencia)}")


def tiempo_total_todas_las_tareas():
    return sum(tareas.values())

print(f"Tiempo total para todas las tareas: {tiempo_total_todas_las_tareas()} minutos")
