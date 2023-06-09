"""
Eres uno de los líderes de gimnasio (Gym Leader) de una importante organización Pokémon internacional. Uno de los altos miembros del Alto Mando te informa que el Campeón de 
la Liga Pokémon ha viajado desde EEUU a Barcelona y ha convocado un torneo de alto nivel para esta tarde a las 19:30 en Barcelona. Han consultado la lista de vuelos desde 
Madrid (donde estás tú) y han llegado a la conclusión de que tienes que tomar un vuelo que parte de Madrid dentro de 2 horas y cierra su facturación 20 minutos antes.

¿Qué duración mínima tiene la misión? ¿Llega el líder a facturar a tiempo dentro de los 100 minutos disponibles? Si no es así, revisa las dependencias, seguro que estás 
indicando relaciones basadas en las restricciones de los recursos.

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

Ahora que tienes una lista de tareas y sus respectivas duraciones, necesitas decidir el camino más corto para completarlas todas. Considera cada tarea como un nodo y la 
duración como el peso de la arista que conecta las tareas. Algunas tareas deben completarse antes que otras, lo que implica que los nodos no están todos conectados entre sí.

Determinar la secuencia óptima de tareas. Recuerda que estos algoritmos son útiles para encontrar el árbol de expansión mínima en un grafo, lo que en este caso representaría
la secuencia de tareas con el tiempo total mínimo.
¿Cuál algoritmo elegirías en este caso y por qué? Desarrolla y describe el proceso que utilizarías para aplicar este algoritmo al conjunto de tareas.
"""


class Tarea:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.tareas_siguientes = []
        self.tiempo_inicio_temprano = 0
        self.tiempo_final_tardio = 0

    def añadir_tarea_siguiente(self, tarea):
        self.tareas_siguientes.append(tarea)

class Grafo:
    def __init__(self):
        self.tareas = []

    def añadir_tarea(self, tarea):
        self.tareas.append(tarea)

    def forward_pass(self):
        for tarea in self.tareas:
            for tarea_siguiente in tarea.tareas_siguientes:
                tarea_siguiente.tiempo_inicio_temprano = max(tarea_siguiente.tiempo_inicio_temprano, tarea.tiempo_inicio_temprano + tarea.duracion)

    def backward_pass(self):
        for tarea in reversed(self.tareas):
            if not tarea.tareas_siguientes:
                tarea.tiempo_final_tardio = tarea.tiempo_inicio_temprano + tarea.duracion
            for tarea_siguiente in tarea.tareas_siguientes:
                tarea.tiempo_final_tardio = min(tarea.tiempo_final_tardio, tarea_siguiente.tiempo_final_tardio - tarea.duracion)

    def encontrar_camino_critico(self):
        camino_critico = [tarea for tarea in self.tareas if tarea.tiempo_inicio_temprano == tarea.tiempo_final_tardio]
        camino_critico.sort(key=lambda x: x.tiempo_inicio_temprano)
        return camino_critico


if __name__ == "__main__":

    tareas_nombres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    tareas_duraciones = [20, 5, 40, 10, 5, 10, 20, 25, 35, 25, 15, 5, 25]

    grafo = Grafo()

    tareas = {nombre: Tarea(nombre, duracion) for nombre, duracion in zip(tareas_nombres, tareas_duraciones)}

    for tarea in tareas.values():
        grafo.añadir_tarea(tarea)

    for i in range(len(tareas_nombres) - 1):
        tareas[tareas_nombres[i]].añadir_tarea_siguiente(tareas[tareas_nombres[i+1]])

    grafo.forward_pass()
    grafo.backward_pass()
    camino_critico = grafo.encontrar_camino_critico()

    tiempo_total = sum(tarea.duracion for tarea in camino_critico)

    print(f'Tiempo total necesario: {tiempo_total} minutos')
    print(f'Camino crítico: {", ".join(tarea.nombre for tarea in camino_critico)}')
