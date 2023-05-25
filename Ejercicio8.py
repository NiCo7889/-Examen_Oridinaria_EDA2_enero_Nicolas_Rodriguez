"""
Ash Ketchum, líder del equipo de entrenadores Pokemon, tiene dificultades para transmitir los mensajes al Centro Pokemon, dado que los mismos son muy largos y los satélites 
espías del Equipo Rocket los interceptan, en un lapso muy corto desde que se transmiten. Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los mensajes 
para enviarlos más rápido y no puedan ser interceptados. Contemplando los siguientes requerimientos, implementar un algoritmo que pueda crear un árbol de Huffman a partir 
de la siguiente tabla y desarrollar las funciones para comprimir y descomprimir un mensaje.

Símbolo	Frecuencia
T	0.15
O	0.15
A	0.12
E	0.10
H	0.09
S	0.07
P	0.07
M	0.07
N	0.06
C	0.06
D	0.05
Z	0.04
K	0.03
,	0.03

Descubre el mensaje cifrado
"""


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

def generar_codigos(nodo, prefijo='', codigo={}, invertir_codigo={}):
    if nodo is None:
        return
    if nodo.simbolo is not None:
        codigo[nodo.simbolo] = prefijo
        invertir_codigo[prefijo] = nodo.simbolo
    generar_codigos(nodo.izq, prefijo + '0', codigo, invertir_codigo)
    generar_codigos(nodo.der, prefijo + '1', codigo, invertir_codigo)
    return codigo, invertir_codigo

def codificar(mensaje, codigo):
    return ''.join([codigo[c] for c in mensaje])

def decodificar(mensaje_codificado, invertir_codigo):
    mensaje = ''
    codigo_actual = ''
    for bit in mensaje_codificado:
        codigo_actual += bit
        if codigo_actual in invertir_codigo:
            mensaje += invertir_codigo[codigo_actual]
            codigo_actual = ''
    return mensaje


frecuencia = {'T': 0.15, 'O': 0.15, 'A': 0.12, 'E': 0.10, 'H': 0.09, 'S': 0.07, 'P': 0.07, 'M': 0.07, 'N': 0.06, 'C': 0.06, 'D': 0.05, 'Z': 0.04, 'K': 0.03, ',': 0.03}


if __name__ == "__main__":

    arbol_huffman = construir_arbol_huffman([Nodo(simbolo, frecuencia) for simbolo, frecuencia in frecuencia.items()])
    codigos, invertir_codigos = generar_codigos(arbol_huffman)

    texto = 'HAZTE,CON,TODOS,POKEMON'
    texto_comprimido = codificar(texto, codigos)
    print('Texto comprimido:', texto_comprimido)

    texto_descomprimido = decodificar(texto_comprimido, invertir_codigos)
    print('Texto descomprimido:', texto_descomprimido)
