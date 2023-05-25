"""
Problema de los movimientos de un Abra en una red de Pokémon

Si se parte de la ruta 1, Abra puede teletransportarse a las rutas 6 y 8 (dos teletransportes); si se sale de la ruta 2, Abra puede llegar a las rutas 7 y 9 
(dos teletransportes más); iniciando desde la ruta 3, se puede arribar a las rutas 4 y 8 (se suman nuevamente dos); si se arranca desde la ruta 4, las posibilidades son 
las rutas 3, 9 y 0 (ahora se acumulan tres teletransportes); pero si la posición inicial es la ruta 5, Abra no puede teletransportarse a ningún lugar dado que no hay 
teletransportes válidos.

Sin embargo, aún restan varias posibilidades más para seguir probando; desde la ruta 6 se pueden alcanzar las rutas 1, 7 y 0 (nuevamente se agregan tres más); por su parte 
desde la ruta 7 se puede mover a Abra hasta las rutas 2 y 6 (la cantidad se incrementa en dos); si se toma la ruta 8 como inicio, se pueden alcanzar las rutas 1 y 3 
(se adicionan dos teletransportes); si se posiciona a Abra en la ruta 9, las opciones para teletransportarse son las rutas 2 y 4 (nuevamente se tienen dos teletransportes); 
y por último, si se sale desde la ruta 0, los teletransportes válidos son hacia las rutas 4 y 6 (se suman los últimos dos). En total, se pueden realizar veinte teletransportes 
válidos con Abra.

Ahora, diseña un algoritmo que permita calcular cuántos posibles teletransportes válidos puede realizar Abra, recibiendo como entrada la cantidad de teletransportes a 
realizar desde el inicio, partiendo de todas las rutas. Por ejemplo, como mostramos anteriormente, si la cantidad de teletransportes es uno, la cantidad de teletransportes 
válidos son veinte. Pero si la cantidad de teletransportes son dos y se sale de la ruta 1, se puede ir hasta las rutas 6 y 8 (un teletransporte), a continuación, a partir 
de la ruta 6 hasta las rutas 1, 7 y 0 (dos teletransportes de Abra), luego se sigue desde la ruta 8 hasta las rutas 1 y 3 (para alcanzar los dos teletransportes de Abra). 
En resumen, se tienen cinco posibles teletransportes válidos partiendo desde la ruta 1 (1-6-1, 1-6-7, 1-6-0, 1-8-1 y 1-8-3) a estos se deben sumar todos los teletransportes 
que resulten de partir de las demás rutas. En total, la cantidad de posibles teletransportes válidos para dos teletransportes son 46. Una vez desarrollado el algoritmo, 
completa la siguiente tabla.

Cantidad de movimientos -> Posibilidades válidas
1 -> 20
2 -> 46
3 -> 104
5 ->
6 ->
7 ->
8 ->
9 ->
10 ->
15 ->
18 ->
21 ->
23 ->
32 ->

"""


import random

class Nodo:
    def __init__(self, simbolo, frecuencia, izq=None, der=None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izq = izq
        self.der = der

def construir_arbol_huffman(simbolos):
    while len(simbolos) > 1:
        simbolos = sorted(simbolos, key=lambda x: x.frecuencia)
        izq = simbolos.pop(0)
        der = simbolos.pop(0)
        nodo = Nodo(None, izq.frecuencia + der.frecuencia, izq, der)
        simbolos.append(nodo)
    return simbolos[0]

def generar_codigos(nodo, prefijo='', codigo={}):
    if nodo is None:
        return
    if nodo.simbolo is not None:
        codigo[nodo.simbolo] = prefijo
    generar_codigos(nodo.izq, prefijo + '0', codigo)
    generar_codigos(nodo.der, prefijo + '1', codigo)
    return codigo

def codificar(mensaje, codigo):
    return ''.join([codigo[c] for c in mensaje])

def decodificar(mensaje_codificado, nodo):
    mensaje = ''
    n = len(mensaje_codificado)
    i = 0
    while i < n:
        nodo_actual = nodo
        while nodo_actual.simbolo is None:
            if mensaje_codificado[i] == '0':
                nodo_actual = nodo_actual.izq
            else:
                nodo_actual = nodo_actual.der
            i += 1
        mensaje += nodo_actual.simbolo
    return mensaje

def generar_frecuencias(simbolos):
    frecuencias = {}
    total = 0
    for simbolo in simbolos:
        frecuencia = random.uniform(0.01, 0.5)
        frecuencias[simbolo] = frecuencia
        total += frecuencia
    for simbolo in frecuencias:
        frecuencias[simbolo] /= total
    return frecuencias


if __name__ == "__main__":

    simbolos = ['T', 'O', 'A', 'E', 'H', 'S', 'P', 'M', 'N', 'C', 'D', 'Z', 'K', ',']
    frecuencias = generar_frecuencias(simbolos)

    nodos = []
    for simbolo in frecuencias:
        nodo = Nodo(simbolo, frecuencias[simbolo])
        nodos.append(nodo)

    arbol_huffman = construir_arbol_huffman(nodos)
    codigos = generar_codigos(arbol_huffman)

    mensaje = 'HAZTE,CON,TODOS,POKEMON'
    mensaje_codificado = codificar(mensaje, codigos)
    mensaje_decodificado = decodificar(mensaje_codificado, arbol_huffman)

    print("Frecuencias:", frecuencias)
    print("Mensaje original:", mensaje)
    print("Mensaje codificado:", mensaje_codificado)
    print("Mensaje decodificado:", mensaje_decodificado)
