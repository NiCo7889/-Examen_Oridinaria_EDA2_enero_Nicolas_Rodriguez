"""
Crea una clase llamada Pokemon.py que tenga los atributos nombre y tipo. Crea el constructor de la clase. Añadir en el constructor un print para informar de que el Pokemon 
se ha creado con éxito. Crear un método llamado clasificacion que clasifique a los Pokemon según su tipo de la siguiente manera:

los PS, el Ataque, la Defensa, el Ataque Especial, la Defensa Especial y la Velocidad.

1.2 Experimentación (0,5 Puntos)

Crea una lista con un numero arbitrario de objetos tipo Pokemon. Recorre los elementos de la lista, y prueba a ejecutar el método clasificacion de cada objeto que has creado.

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
        self.lista_pokemons = [
            Pokemon("Bulbasaur", "Planta"), 
            Pokemon("Charmander", "Fuego"), 
            Pokemon("Squirtle", "Agua"), 
            Pokemon("Pikachu", "Electrico"),
            # Añade tantos objetos Pokemon como desees aquí.
        ]

    def test_pokemon(self):
        for pokemon in self.lista_pokemons:
            pokemon.clasificacion()  # Llamar al método clasificacion para cada objeto Pokemon.

        # Aquí van tus pruebas de aserción. Por ejemplo:
        self.assertEqual(self.lista_pokemons[0].nombre, "Bulbasaur")
        self.assertEqual(self.lista_pokemons[0].tipo, "Planta")
        # Y así sucesivamente para los demás Pokémon.

if __name__ == "__main__":
    unittest.main()