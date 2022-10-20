# Autor Josué Beltetón
# Contacto josuebelteton@icloud.com
# Licencia Creative Commons

import math

class Vertice:
   """Clase que define los vértices de los gráficas"""

   def __init__(self, i):
       """Método que inicializa el vértice con sus atributos
     id = identificador
     vecinos = lista de los vértices con los que está conectado por una arista
     visitado = flag para saber si fue visitado o no
     padre = vértice visitado un paso antes
     costo = valor que tiene recorrerlo"""
       self.id = i
       self.vecinos = []
       self.visitado = False
       self.padre = None
       self.costo = float('inf')

   def agregarVecino(self, v, p):
       """Método que agrega los vertices que se encuentre conectados por una arista a la lista de vecinos
     de un vertice, revisando si éste aún no se encuentra en la lista de vecinos"""
       if v not in self.vecinos:
           self.vecinos.append([v, p])


class Grafica:
   """Clase que define los vértices de las gráficas"""

   def __init__(self):
       """vertices = diccionario con los vertices de la grafica"""
       self.vertices = {}

   def agregarVertice(self, id):
       """Método que agrega vértices, recibiendo el índice y la heuristica (para A* puede que no se reciba) revisando si éste no existe en el diccionario
     de vértices"""
       if id not in self.vertices:
           self.vertices[id] = Vertice(id)

   def agregarArista(self, a, b, p):
       """Método que agrega aristas, recibiendo el índice de dos vertices y revisando si existen estos en la lista
     de vertices, además de recibir el peso de la arista , el cual se asigna a ambos vértices por medio del método
     agregar vecino"""
       if a in self.vertices and b in self.vertices:
           self.vertices[a].agregarVecino(b, p)
           self.vertices[b].agregarVecino(a, p)

   def imprimirGrafica(self):
       """Método que imprime el gráfo completo arista por arista con todas sus características(incluye heurística)"""
       for v in self.vertices:
           print("El costo del vértice " + str(self.vertices[v].id) + " es " + str(
               self.vertices[v].costo) + " llegando desde " + str(self.vertices[v].padre))

   def camino(self, a, b):
       """Método que va guardando en la lista llamada 'camino' los nodos en el orden que sean visitados y actualizando dicha
     lista con los vértices con el menor costo"""
       camino = []
       actual = b
       while actual != None:
           camino.insert(0, actual)
           actual = self.vertices[actual].padre
       return [camino, self.vertices[b].costo]

   def minimo(self, l):
       """Método que recibe la lista de los vertices no visitados, revisa si su longitud es mayor a cero(indica que
     aún hay vértices sin visitar), y realiza comparaciones de los costos de cada vértice en ésta lista para encontrar
     el de menor costo"""
       if len(l) > 0:
           m = self.vertices[l[0]].costo
           v = l[0]
           for e in l:
               if m > self.vertices[e].costo:
                   m = self.vertices[e].costo
                   v = e
           return v
       return None

   def dijkstra(self, a):
       """Método que sigue el algortimo de Dijkstra
     1. Asignar a cada nodo una distancia tentativa: 0 para el nodo inicial e infinito para todos los nodos restantes. Predecesor nulo para todos.
     2. Establecer al nodo inicial como nodo actual y crear un conjunto de nodos no visitados.
     3. Para el nodo actual, considerar a todos sus vecinos no visitados con peso w.
        a) Si la distancia del nodo actual sumada al peso w es menor que la distancia tentativa actual de ese vecino,
        sobreescribir la distancia con la suma obtenida y guardar al nodo actual como predecesor del vecino
     4. Cuando se termina de revisar a todos los vecino del nodo actual, se marca como visitado y se elimina del conjunto no  visitado
     5. Continúa la ejecución hasta vaciar al conjunto no visitado
     6. Seleccionar el nodo no visitado con menor distancia tentativa y marcarlo como el nuevo nodo actual. Regresar al punto 3
     """
       if a in self.vertices:
           # 1 y 2
           self.vertices[a].costo = 0
           actual = a
           noVisitados = []

           for v in self.vertices:
               if v != a:
                   self.vertices[v].costo = float('inf')
               self.vertices[v].padre = None
               noVisitados.append(v)

           while len(noVisitados) > 0:
               # 3
               for vec in self.vertices[actual].vecinos:
                   if self.vertices[vec[0]].visitado == False:
                       # 3.a
                       if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
                           self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
                           self.vertices[vec[0]].padre = actual

               # 4
               self.vertices[actual].visitado = True
               noVisitados.remove(actual)

               # 5 y 6
               actual = self.minimo(noVisitados)
       else:
           return False


class main:

   g = Grafica()
   g.agregarVertice(1)  # A
   g.agregarVertice(2)  # B
   g.agregarVertice(3)  # C
   g.agregarVertice(4)  # D
   g.agregarVertice(5)  # E
   g.agregarVertice(6)  # F
   g.agregarArista(1, 2, 6)  # A->B
   g.agregarArista(1, 3, 10)  # A->C
   g.agregarArista(2, 4, 2)  # B->D
   g.agregarArista(2, 3, 4)  # B->C
   g.agregarArista(3, 4, 2)  # C->D
   g.agregarArista(3, 5, 8)  # C->E
   g.agregarArista(3, 6, 14)  # C->F
   g.agregarArista(4, 5, 10)  # D->E
   g.agregarArista(5, 6, 6)  # E->F


   print("\n\nLa ruta más rápida por Dijkstra junto con su costo es:")
   g.dijkstra(1)
   print(g.camino(1, 6))
   print("\nLos valores finales de la gráfica son los siguientes:")
   g.imprimirGrafica()
