# Al añadir un campo costo que tiene un valor aleatorio, lograr que el programa llegue del Estado Inicial
# al Estado Final es cuestión de suerte ya que si el valor de los costos resultan ser optimos, se puede
# llegar al Estado Final con muy pocos cálculos. Por otro lado si los costos no son optimos puede llegar
# al Estado Final en mucho más tiempo si es que no existieran los costos.
# Si dirigimos los valores de los costos para que resultemos en el caso optimo podría llevar muy poco
# tiempo resolverlo incluso si tenemos muchos digitos con los que trabajar

from Nodos import Nodo
import random

def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodos_frontera_ordenado = []
    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodos_frontera = sorted(nodos_frontera, key = lambda x : x.get_costo())
        nodos_frontera.reverse()
        for elemento in range(0, len(nodos_frontera)):
            print(nodos_frontera[elemento].get_costo(), nodos_frontera[elemento].get_estado())
        print("-----------------------------------------------")
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            conseguir_hijos(nodo_actual, nodos_visitados, nodos_frontera, nodos_frontera_ordenado)

def conseguir_hijos(padre, nodos_visitados, nodos_frontera, nodos_frontera_ordenado):
    cantidad_hijos = len(padre.get_estado().copy())-1
    for hijos_conseguidos in range (0,cantidad_hijos):
        hijo_n_datos = padre.get_estado().copy()
        temp = hijo_n_datos[hijos_conseguidos]    
        hijo_n_datos[hijos_conseguidos] = hijo_n_datos[hijos_conseguidos+1]
        hijo_n_datos[hijos_conseguidos+1] = temp
        hijo_n = Nodo(hijo_n_datos)
        if hijo_n.get_costo() == None:
            hijo_n.set_costo(random.randint(1,10))
        if not hijo_n.en_lista(nodos_visitados) and not hijo_n.en_lista(nodos_frontera):
            padre.set_hijo2(hijo_n)
            nodos_frontera.append(hijo_n)


if __name__ == "__main__":
    estado_inicial = [5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5]
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        # print(nodo_actual.get_costo())
        nodo_actual = nodo_actual.get_padre()
    
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
