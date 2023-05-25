"""
Copia el ejercicio anterior y realicemos la siguiente modificación:

Junto al método init y clasificacion, sobrescriba el método especial de Python, el método str, que tiene el siguiente formato:

def __str__(self):
return "Lo que quiero mostrar"
Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto pokemon1 creado y realizamos print(pokemon1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

2.2 Experimentación (0,5 puntos)
Implementa el método str y haz que muestre el nombre y el tipo del Pokemon. Crea una lista con un numero arbitrario de objetos tipo Pokemon. Recorre los elementos de la lista, y utiliza el método print de esos objetos para visualizar por pantalla la información del str.
"""


import random

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.PS = random.randint(50, 100)
        self.ataque = random.randint(50, 100)
        self.defensa = random.randint(50, 100)
        self.ataque_especial = random.randint(50, 100)
        self.defensa_especial = random.randint(50, 100)
        self.velocidad = random.randint(50, 100)
        print(f'El Pokemon {self.nombre} se ha creado con éxito.')
        
    def clasificacion(self):
        if self.tipo == "Agua":
            return f'{self.nombre} es un Pokemon de agua.'
        elif self.tipo == "Fuego":
            return f'{self.nombre} es un Pokemon de fuego.'
        elif self.tipo == "Planta":
            return f'{self.nombre} es un Pokemon de planta.'
        else:
            return f'{self.nombre} es un Pokemon de tipo {self.tipo}.'
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Tipo: {self.tipo}, PS: {self.PS}, Ataque: {self.ataque}, Defensa: {self.defensa}, Ataque Especial: {self.ataque_especial}, Defensa Especial: {self.defensa_especial}, Velocidad: {self.velocidad}'

class NodoArbol:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.izq = None
        self.der = None

    def insertar(self, pokemon):
        if pokemon.nombre < self.pokemon.nombre:
            if self.izq is None:
                self.izq = NodoArbol(pokemon)
            else:
                return self.izq.insertar(pokemon)
        else:
            if self.der is None:
                self.der = NodoArbol(pokemon)
            else:
                return self.der.insertar(pokemon)

    def buscar(self, nombre):
        if nombre < self.pokemon.nombre:
            if self.izq is None:
                return None
            else:
                return self.izq.buscar(nombre)
        elif nombre > self.pokemon.nombre:
            if self.der is None:
                return None
            else:
                return self.der.buscar(nombre)
        else:
            return self.pokemon


import unittest

class TestEjercicios(unittest.TestCase):

    def setUp(self):
                    # Creando la lista de Pokemons
            self.lista_pokemons = [
                Pokemon("Bulbasaur", "Planta"), 
                Pokemon("Charmander", "Fuego"), 
                Pokemon("Squirtle", "Agua"), 
                Pokemon("Pikachu", "Electrico")
                            ]

            # Imprimiendo la información de cada Pokemon
            for pokemon in self.lista_pokemons:
                print(pokemon)

    def test_calificacion(self):
        for pokemon in self.lista_pokemons:
            print(pokemon.clasificacion())
        

if __name__ == "__main__":
    unittest.main()