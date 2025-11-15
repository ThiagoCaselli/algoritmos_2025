import math
from typing import Any, Optional, List as PyList

class List(list):
    CRITERION_FUNCTIONS = {}
    def add_criterion(self, key_criterion: str, function):
        if not hasattr(self, 'CRITERION_FUNCTIONS'):
             self.CRITERION_FUNCTIONS = {}
        self.CRITERION_FUNCTIONS[key_criterion] = function
    def show(self) -> None:
        for element in self:
            print(f"  {element}")
    def delete_value(self, value, key_value: str = None) -> Optional[Any]:
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index
    def sort_by_criterion(self, criterion_key: str = None) -> None:
        if not hasattr(self, 'CRITERION_FUNCTIONS'):
            self.CRITERION_FUNCTIONS = {}
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)
        if criterion is not None:
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            pass 
    def search(self, search_value, search_key: str = None) -> Optional[int]:
        criterion = None
        if hasattr(self, 'CRITERION_FUNCTIONS'):
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
        for i, item in enumerate(self):
            value_to_compare = None
            if criterion:
                value_to_compare = criterion(item)
            elif search_key and hasattr(item, search_key):
                value_to_compare = getattr(item, search_key)
            elif not search_key and hasattr(item, 'value'):
                value_to_compare = item.value
            else:
                value_to_compare = item
            if value_to_compare == search_value:
                return i
        return None

class Queue:
    def __init__(self):
        self.__elements = []
    def arrive(self, value: Any) -> None:
        self.__elements.append(value)
    def attention(self) -> Optional[Any]:
        return (self.__elements.pop(0) if self.__elements else None)
    def size(self) -> int:
        return len(self.__elements)
    def on_front(self) -> Optional[Any]:
        return (self.__elements[0] if self.__elements else None)
    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    def show(self):
        for i in range(len(self.__elements)):
            print(self.move_to_end())

class Stack:
    def __init__(self):
        self.__elements = []
    def push(self, value: Any) -> None:
        self.__elements.append(value)
    def pop(self) -> Optional[Any]:
        return (self.__elements.pop() if self.__elements else None)
    def size(self) -> int:
        return len(self.__elements)
    def on_top(self) -> Optional[Any]:
        return (self.__elements[-1] if self.__elements else None)
    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())
    def to_list(self) -> PyList:
        return list(self.__elements)

class HeapMin:
    def __init__(self):
        self.elements = []
    def size(self) -> int:
        return len(self.elements)
    def add(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size()-1)
    def remove(self) -> Any:
        if self.size() == 0: return None
        if self.size() == 1: return self.elements.pop()
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value
    def float(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index][0] < self.elements[father][0]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2
    def sink(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1
            minor = left_son
            if right_son < self.size():
                if self.elements[right_son][0] < self.elements[minor][0]:
                    minor = right_son
            if self.elements[index][0] > self.elements[minor][0]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False
    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]
    def arrive(self, value: Any, priority: int) -> None:
        self.add([priority, value])
    def attention(self) -> Any:
        value = self.remove()
        return value
    def search(self, value: Any) -> Optional[int]:
        for i, (priority, item) in enumerate(self.elements):
            if item[0] == value:
                return i
        return None
    def change_priority(self, index: int, new_priority: int) -> None:
        old_priority = self.elements[index][0]
        self.elements[index][0] = new_priority
        if new_priority < old_priority:
            self.float(index)
        else:
            self.sink(index)

class Graph(List):
    class __nodeVertex:
        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            self.visited = False
        def __str__(self):
            return f"{self.value}" # Simplificado para este problema
    
    class __nodeEdge:
        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values
        def __str__(self):
            return f"Destino: {self.value} | Peso: {self.weight}m"
    
    @staticmethod
    def _order_by_value(item): return item.value
    @staticmethod
    def _order_by_weight(item): return item.weight
    
    def __init__(self, is_directed=False):
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def show(self) -> None:
        print("Contenido del Grafo (Layout de la Casa):")
        for vertex in self:
            print(f"Vértice: {vertex.value}")
            print("  Conexiones (Aristas):")
            vertex.edges.show()
            print("-" * 20)

    def insert_vertex(self, value: Any, other_values: Optional[Any] = None) -> None:
        node_vertex = Graph.__nodeVertex(value, other_values)
        self.append(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            if not self.is_directed and origin_vertex != destination_vertex:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print(f'Error: Vértice origen o destino no encontrado.')

    def mark_as_unvisited(self) -> None:
        for vertex in self:
            vertex.visited = False

    def dijkstra(self, origin):
        no_visited = HeapMin()
        path = Stack()
        for vertex in self:
            distance = 0 if vertex.value == origin else math.inf
            no_visited.arrive([vertex.value, vertex, None], distance)
        while no_visited.size() > 0:
            value = no_visited.attention()
            costo_nodo_actual = value[0]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges
            for edge in edges:
                pos = no_visited.search(edge.value)
                if pos is not None:
                    if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = value[1][0]
                        no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path

    def kruskal(self):
        mst = Graph(is_directed=False)
        forest = []
        edges = HeapMin()
        for vertex in self:
            forest.append({vertex.value})
            mst.insert_vertex(vertex.value, vertex.other_values)
            for edge in vertex.edges:
                if vertex.value < edge.value:
                    edges.arrive([vertex.value, edge.value], edge.weight)
        
        total_weight = 0
        while len(forest) > 1 and edges.size() > 0:
            edge_data = edges.attention()
            weight = edge_data[0]
            origin_val = edge_data[1][0]
            dest_val = edge_data[1][1]
            
            origin_set_idx = -1
            dest_set_idx = -1
            for i, vertex_set in enumerate(forest):
                if origin_val in vertex_set: origin_set_idx = i
                if dest_val in vertex_set: dest_set_idx = i
            
            if origin_set_idx != dest_set_idx:
                mst.insert_edge(origin_val, dest_val, weight)
                total_weight += weight
                idx1, idx2 = max(origin_set_idx, dest_set_idx), min(origin_set_idx, dest_set_idx)
                set1 = forest.pop(idx1)
                set2 = forest.pop(idx2)
                forest.append(set1.union(set2))
        return mst, total_weight


def obtener_camino_y_costo(dijkstra_stack: Stack, destination: str):
    results = {}
    while dijkstra_stack.size() > 0:
        data = dijkstra_stack.pop()
        results[data[0]] = (data[1], data[2]) 
    
    costo = results.get(destination, (math.inf, None))[0]
    
    if costo == math.inf:
        return None, math.inf

    path = []
    curr = destination
    while curr is not None:
        path.append(curr)
        if curr not in results: break
        curr = results[curr][1]
        
    return list(reversed(path)), costo


if __name__ == "__main__":
    
    # --- a. Definir ambientes (vértices) ---
    ambientes = [
        'cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2',
        'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio'
    ]

    # --- b. Cargar aristas (distancias en metros) ---
    # Se cumple: 
    # 1. Al menos 3 aristas por vértice.
    # 2. Vértices con 5+ aristas: 'comedor', 'patio', 'sala de estar', 'terraza'
    
    aristas = [
        # (Ambiente 1, Ambiente 2, Distancia en Metros)
        ('cochera', 'patio', 4),
        ('cochera', 'cocina', 3),
        ('cochera', 'comedor', 5),
        
        ('patio', 'quincho', 5),
        ('patio', 'cocina', 2),
        ('patio', 'comedor', 3),
        ('patio', 'baño 1', 6),
        
        ('quincho', 'baño 1', 1),
        ('quincho', 'cocina', 4),
        
        ('cocina', 'comedor', 3),
        
        ('comedor', 'sala de estar', 2),
        ('comedor', 'habitación 1', 4),
        ('comedor', 'terraza', 6),
        
        ('sala de estar', 'habitación 2', 3),
        ('sala de estar', 'terraza', 3),
        ('sala de estar', 'baño 2', 1),
        ('sala de estar', 'habitación 1', 4), # Conexión extra
        
        ('baño 1', 'habitación 1', 3),
        
        ('baño 2', 'habitación 2', 1),
        ('baño 2', 'terraza', 3), # Conexión extra
        
        ('habitación 1', 'terraza', 2),
        ('habitación 2', 'terraza', 2)
    ]

    # --- Instanciar y cargar el grafo (no dirigido) ---
    g = Graph(is_directed=False)

    print("Cargando vértices (ambientes)...")
    for amb in ambientes:
        g.insert_vertex(amb)

    print("Cargando aristas (distancias)...")
    for origen, destino, peso in aristas:
        g.insert_edge(origen, destino, peso)

    print("Grafo de la casa cargado.")
    #g.show() # Descomentar para ver el grafo completo
    
    print("\n" + "="*50 + "\n")

    # --- c. Obtener Árbol de Expansión Mínima (Kruskal) ---
    print("c. 🔌 Cálculo de cableado mínimo (Árbol de Expansión Mínima)")
    print("-" * 50)
    
    mst, costo_total_cable = g.kruskal()
    
    print("El Árbol de Expansión Mínima (MST) es:")
    mst.show()
    print(f"\nResultado (c): Se necesitan {costo_total_cable} metros de cable para conectar todos los ambientes.")

    print("\n" + "="*50 + "\n")

    # --- d. Obtener Camino más Corto (Dijkstra) ---
    print("d. 💻 Cálculo de cable de red (Camino más corto)")
    print("-" * 50)
    
    origen = 'habitación 1'
    destino = 'sala de estar'
    
    dijkstra_stack = g.dijkstra(origen)
    camino, costo_cable_red = obtener_camino_y_costo(dijkstra_stack, destino)
    
    if camino:
        print(f"Camino más corto de '{origen}' a '{destino}':")
        print(f"  Ruta: {' -> '.join(camino)}")
        print(f"\nResultado (d): Se necesitan {costo_cable_red} metros de cable de red para el Smart TV.")
    else:
        print(f"No se encontró ruta entre '{origen}' y '{destino}'.")

    print("\n" + "="*50 + "\n")