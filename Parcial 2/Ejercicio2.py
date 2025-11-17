from __future__ import annotations
from typing import Any, Optional
from math import inf

class List(list):
    
    def __init__(self, *args, **kwargs):
        # Llama al __init__ de la clase base (list)
        super().__init__(*args, **kwargs) 
        
        self.CRITERION_FUNCTIONS = {}

    def add_criterion(
        self,
        key_criterion: str,
        function,
    ):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(self) -> None:
        for element in self:
            print(element)

    def delete_value(
        self,
        value,
        key_value: str = None,
    ) -> Optional[Any]:
        index = self.search(value, key_value)
        # Devuelve el valor popeado si lo encuentra, o None si no.
        return self.pop(index) if index is not None else None

    def sort_by_criterion(
        self,
        criterion_key: str = None,
    ) -> None:
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search(
        self,
        search_value,
        search_key: str = None,
    ) -> Optional[int]:
        """
        Devuelve el ÍNDICE de la primera ocurrencia de search_value,
        o None si no se encuentra.
        """
        criterion = self.CRITERION_FUNCTIONS.get(search_key)

        for index, element in enumerate(self):
            value_to_compare = None
            if criterion:
                value_to_compare = criterion(element)
            elif hasattr(element, 'value'):
                # Intenta usar .value por defecto (común en tus clases)
                value_to_compare = element.value 
            else:
                # Compara el elemento directamente (para listas simples)
                value_to_compare = element
            
            if value_to_compare == search_value:
                return index
        
        return None # No se encontró


class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]:
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    
    def show(self):
        for _ in range(len(self.__elements)):
            print(self.move_to_end())


class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())


class HeapMin:
    def __init__(self):
        self.elements = []
    
    def size(self) -> int:
        return len(self.elements)

    def add(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size()-1)
    
    def search(self, value):
        for index, element in enumerate(self.elements):
            # Asume la estructura [priority, [value, data, prev]]
            if element[1][0] == value:
                return index

    def remove(self) -> Any:
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index] < self.elements[father]:
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
                if self.elements[right_son] < self.elements[minor]:
                    minor = right_son
            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False

    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        # El 'priority' es la clave principal para el orden
        self.add([priority, value])
    
    def attention(self) -> Any:
        # Devuelve la tupla [priority, value]
        value = self.remove()
        return value

    def change_priority(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.sink(index)
            elif new_priority < previous_priority:
                self.float(index)


class Graph(List):

    class __nodeVertex:
        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List() # Usa la List corregida
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values # Usado para (f)
            self.visited = False
        
        def __str__(self):
            return f"{self.value} (Datos: {self.other_values})"
    
    class __nodeEdge:
        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values
        
        def __str__(self):
            return f'Destino: {self.value}, Peso: {self.weight}'
    
    def __init__(self, is_directed=False):
        super().__init__()
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    @staticmethod
    def _order_by_value(item):
        return item.value

    @staticmethod
    def _order_by_weight(item):
        return item.weight
    
    def show(self) -> None:
        for vertex in self:
            print(f"\n--- Vértice: {vertex.value} ---")
            print("Datos:", vertex.other_values)
            print("Aristas:")
            for edge in vertex.edges:
                print(f"  -> {edge}") 

    def insert_vertex(self, value: Any, other_values: Optional[Any] = None) -> None:
        node_vertex = Graph.__nodeVertex(value, other_values)
        self.append(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            
            if not self.is_directed and origin != destination: 
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print(f'No se puede insertar arista: Vértice no encontrado ({origin_vertex} o {destination_vertex})')

    def delete_edge(
        self, origin, destination, key_value: str = 'value',
    ) -> Optional[Any]:
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            
            if not self.is_directed and edge is not None:
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(
        self, value, key_value_vertex: str = 'value', key_value_edges: str = 'value',
    ) -> Optional[Any]:
        delete_value = self.delete_value(value, key_value_vertex) 
        
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    def mark_as_unvisited(self) -> None:
        for vertex in self:
            vertex.visited = False

    def amplitude_sweep(self, value)-> None:
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                queue_vertex.arrive(self[vertex_pos])
                
                while queue_vertex.size() > 0:
                    vertex = queue_vertex.attention()
                    print(vertex.value)
                    
                    for edge in vertex.edges:
                        destination_edge_pos = self.search(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                queue_vertex.arrive(self[destination_edge_pos])

    def dijkstra(self, origin):
        no_visited = HeapMin() 
        path = Stack() 
        
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            # [valor_vertice, objeto_vertice, previo]
            no_visited.arrive([vertex.value, vertex, None], distance) 
        
        while no_visited.size() > 0:
            # value = [costo, [valor_vertice, objeto_vertice, previo]]
            value = no_visited.attention() 
            costo_nodo_actual = value[0]
            # data = [valor_vertice, objeto_vertice, previo]
            data = value[1]
            
            # [valor_vertice, costo, previo]
            path.push([data[0], costo_nodo_actual, data[2]]) 
            
            edges = data[1].edges
            for edge in edges:
                pos = no_visited.search(edge.value)
                if pos is not None:
                    nuevo_costo = costo_nodo_actual + edge.weight
                    if nuevo_costo < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = data[0] # Actualiza el 'previo'
                        no_visited.change_priority(pos, nuevo_costo)
        return path

    def kruskal(self) -> list:
        """ Devuelve una lista de aristas que forman el MST """
        
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
            return None
                
        forest = []
        edges = HeapMin()
        mst_edges = [] # Lista para guardar el MST
        
        for vertex in self:
            forest.append(vertex.value)
            # Evita duplicados en Kruskal para grafos no dirigidos
            for edge in vertex.edges:
                if vertex.value < edge.value: # "A" < "B"
                    edges.arrive([vertex.value, edge.value], edge.weight)
        
        while len(forest) > 1 and edges.size() > 0:
            # edge = [weight, [origin_val, dest_val]]
            edge = edges.attention()
            weight = edge[0]
            origin_val = edge[1][0]
            dest_val = edge[1][1]
            
            origin_tree_idx = search_in_forest(forest, origin_val)
            dest_tree_idx = search_in_forest(forest, dest_val)
            
            if origin_tree_idx is not None and dest_tree_idx is not None:
                if origin_tree_idx != dest_tree_idx:
                    # Une los árboles (conjuntos)
                    if origin_tree_idx > dest_tree_idx:
                        origin_tree_idx, dest_tree_idx = dest_tree_idx, origin_tree_idx
                    
                    tree_origin = forest.pop(origin_tree_idx)
                    tree_dest = forest.pop(dest_tree_idx - 1)
                    
                    forest.append(tree_origin + ';' + tree_dest)
                    mst_edges.append(f"{origin_val} - {dest_val} (Peso: {weight})")
        
        return mst_edges



def find_max_shared_episodes(graph: Graph):
    """ (Punto c) Encuentra la arista con el mayor peso """
    max_weight = -1
    pairs = []
    processed_edges = set() # Para evitar duplicados (A-B y B-A)

    for vertex in graph:
        for edge in vertex.edges:
            pair_key = tuple(sorted((vertex.value, edge.value)))
            
            if pair_key not in processed_edges:
                if edge.weight > max_weight:
                    max_weight = edge.weight
                    pairs = [pair_key] # Inicia nueva lista
                elif edge.weight == max_weight:
                    pairs.append(pair_key)
                
                processed_edges.add(pair_key)

    return max_weight, pairs

def find_characters_by_episode_count(graph: Graph, count: int):
    """ (Punto f) Busca en other_values de los vértices """
    characters = []
    for vertex in graph:
        if vertex.other_values and vertex.other_values.get('episodes') == count:
            characters.append(vertex.value)
    return characters

def get_shortest_path(dijkstra_stack: Stack, destination: str):
    """ (Punto e) Reconstruye el camino desde el Stack de Dijkstra """
    
    paths_info = {}
    while dijkstra_stack.size() > 0:
        data = dijkstra_stack.pop() # [nombre, costo, previo]
        paths_info[data[0]] = data

    if destination not in paths_info:
        return None, inf

    path = []
    current = destination
    while current is not None:
        path.append(current)
        if current not in paths_info: # Si el origen no es alcanzable
            break
        current = paths_info[current][2] # Vamos al 'previo'
    
    cost = paths_info[destination][1]
    return list(reversed(path)), cost


# BLOQUE PRINCIPAL: 

if __name__ == "__main__":
    
    # Creamos un grafo NO dirigido
    g = Graph(is_directed=False)

    # d) Carga de personajes (Vértices)
    print("d) Cargando personajes...")
    characters = [
        ('Luke Skywalker', {'episodes': 6}),
        ('Darth Vader', {'episodes': 6}),
        ('Yoda', {'episodes': 6}),
        ('Boba Fett', {'episodes': 4}),
        ('C-3PO', {'episodes': 9}),
        ('Leia', {'episodes': 6}),
        ('Rey', {'episodes': 3}),
        ('Kylo Ren', {'episodes': 3}),
        ('Chewbacca', {'episodes': 7}),
        ('Han Solo', {'episodes': 5}),
        ('R2-D2', {'episodes': 9}),
        ('BB-8', {'episodes': 3}),
    ]
    for name, data in characters:
        g.insert_vertex(name, data)

    # a) Carga de aristas (Episodios juntos) 
    print("a) Cargando aristas (episodios juntos)...")
    edges = [
        ('Luke Skywalker', 'Darth Vader', 4),
        ('Luke Skywalker', 'Leia', 5),
        ('Luke Skywalker', 'Han Solo', 5),
        ('Luke Skywalker', 'C-3PO', 6),
        ('Luke Skywalker', 'R2-D2', 6),
        ('Luke Skywalker', 'Yoda', 4),
        ('Darth Vader', 'Yoda', 1),
        ('Han Solo', 'Leia', 5),
        ('Han Solo', 'Chewbacca', 6),
        ('C-3PO', 'R2-D2', 9), # El máximo
        ('C-3PO', 'Leia', 6),
        ('C-3PO', 'Han Solo', 5),
        ('R2-D2', 'Leia', 6),
        ('Rey', 'Kylo Ren', 3),
        ('Rey', 'BB-8', 3),
        ('Rey', 'Han Solo', 1),
        ('Boba Fett', 'Darth Vader', 2)
    ]
    for origin, dest, weight in edges:
        g.insert_edge(origin, dest, weight)

    print()
    # b) Árbol de expansión mínimo
    print("b) ÁRBOL DE EXPANSIÓN MÍNIMO (KRUSKAL)")
    print()

    mst = g.kruskal()
    print("Aristas del Árbol de Expansión Mínimo:")
    for edge in mst:
        print(f"  - {edge}")
    
    print()
    # c) Máximo número de episodios compartidos
    print("c) MÁXIMO DE EPISODIOS COMPARTIDOS")
    print()
    max_w, max_pairs = find_max_shared_episodes(g)
    print(f"El número máximo de episodios compartidos es: {max_w}")
    print("Pares que coinciden con ese número:")
    for p1, p2 in max_pairs:
        print(f"  - {p1} y {p2}")

    print()
    # e) Camino más corto (Dijkstra) 
    print("e) CAMINO MÁS CORTO (DIJKSTRA)")
    print()
    
    # Camino 1: C-3PO a R2-D2
    stack_c3po = g.dijkstra('C-3PO')
    path_c3po, cost_c3po = get_shortest_path(stack_c3po, 'R2-D2')
    print(f"Camino más corto C-3PO -> R2-D2 (Costo: {cost_c3po}):")
    print(f"  {' -> '.join(path_c3po)}")

    # Camino 2: Yoda a Darth Vader
    stack_yoda = g.dijkstra('Yoda')
    path_yoda, cost_yoda = get_shortest_path(stack_yoda, 'Darth Vader')
    print(f"\nCamino más corto Yoda -> Darth Vader (Costo: {cost_yoda}):")
    print(f"  {' -> '.join(path_yoda)}")
    

    print()
    # f) Personajes en 9 episodios
    print("f) PERSONAJES EN LOS 9 EPISODIOS")
    print()
    en_9_episodios = find_characters_by_episode_count(g, 9)
    print("Los personajes que aparecieron en 9 episodios son:")
    for char in en_9_episodios:
        print(f"  - {char}")