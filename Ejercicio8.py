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



# Primero, definimos la clase Nodo
class Nodo:
    def __init__(self, simbolo, frecuencia, izq=None, der=None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izq = izq
        self.der = der

# Luego, creamos la función para construir el árbol de Huffman
def construir_arbol_huffman(simbolos):
    while len(simbolos) > 1:
        # Ordenamos los símbolos por frecuencia
        simbolos = sorted(simbolos, key=lambda x: x.frecuencia)
        # Creamos un nuevo nodo con los dos nodos de menor frecuencia
        izq = simbolos.pop(0)
        der = simbolos.pop(0)
        nodo = Nodo(None, izq.frecuencia + der.frecuencia, izq, der)
        simbolos.append(nodo)
    return simbolos[0]  # El último nodo es la raíz del árbol

# Creamos una función para generar los códigos Huffman a partir del árbol
def generar_codigos(nodo, prefijo='', codigo={}):
    if nodo is None:
        return
    if nodo.simbolo is not None:
        codigo[nodo.simbolo] = prefijo
    generar_codigos(nodo.izq, prefijo + '0', codigo)
    generar_codigos(nodo.der, prefijo + '1', codigo)
    return codigo

# Finalmente, creamos las funciones para codificar y decodificar el mensaje
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

# Ahora podemos usar estas funciones para construir el árbol de Huffman y codificar y decodificar mensajes
frecuencias = {
    'T': 0.15,
    'O': 0.15,
    'A': 0.12,
    'E': 0.10,
    'H': 0.09,
    'S': 0.07,
    'P': 0.07,
    'M': 0.07,
    'N': 0.06,
    'C': 0.06,
    'D': 0.05,
    'Z': 0.04,
    'K': 0.03,
    ',': 0.03,
    'B': 0.02,  # Añade la frecuencia para 'B'
    'R': 0.02   # Añade la frecuencia para 'R'
}

nodos = [Nodo(s, f) for s, f in frecuencias.items()]
arbol_huffman = construir_arbol_huffman(nodos)
codigos_huffman = generar_codigos(arbol_huffman)


if __name__ == "__main__":

    mensaje = "SE,PASA"
    mensaje_codificado = codificar(mensaje, codigos_huffman)
    mensaje_decodificado = decodificar(mensaje_codificado, arbol_huffman)
    mensaje_cifrado = "001101110110100110011010"

    print("Mensaje original: ", mensaje)
    print("Mensaje codificado: ", mensaje_codificado)
    print("Mensaje decodificado: ", mensaje_decodificado)
    print("Mensaje cifrado: ", decodificar(mensaje_cifrado, arbol_huffman))
