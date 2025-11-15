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
        
        return None # No encontrado

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
        for i in range(len(self.__elements)):
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
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.elements.pop()

        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index][0] < self.elements[father][0]: # Compara prioridad
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
                if self.elements[right_son][0] < self.elements[minor][0]: # Compara prioridad
                    minor = right_son

            if self.elements[index][0] > self.elements[minor][0]: # Compara prioridad
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
    
    # === MÉTODOS AÑADIDOS para Dijkstra ===
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
            self.other_values = other_values # Para el tipo de dispositivo
            self.visited = False
        
        def __str__(self):
            return f"{self.value} ({self.other_values})" # Muestra nombre y tipo
    
    class __nodeEdge:
        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value # Vértice destino
            self.weight = weight
            self.other_values = other_values
        
        def __str__(self):
            return f"Destino: {self.value} | Peso: {self.weight}"
    
    @staticmethod
    def _order_by_value(item):
        return item.value

    @staticmethod
    def _order_by_weight(item):
        return item.weight
    
    def __init__(self, is_directed=False):
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def show(self) -> None:
        print("Contenido del Grafo:")
        for vertex in self:
            print(f"Vértice: {vertex}")
            print("  Aristas:")
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
            # Si no es dirigido, añade la arista de vuelta
            if not self.is_directed and origin_vertex != destination_vertex:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print(f'Error: Vértice origen o destino no encontrado para arista ({origin_vertex}, {destination_vertex})')

    def delete_edge(self, origin, destination, key_value: str = 'value') -> Optional[Any]:
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            # Si no es dirigido, borra también la arista de vuelta
            if not self.is_directed and edge is not None:
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(self, value, key_value_vertex: str = 'value', key_value_edges: str = 'value') -> Optional[Any]:
        # Corregido: 'g.delete_value' debe ser 'self.delete_value'
        delete_value = self.delete_value(value, key_value_vertex)
        if delete_value is not None:
            for vertex in self:
                # No es necesario pasar key_value_edges, delete_edge usa 'value' por defecto
                self.delete_edge(vertex.value, value) 
        return delete_value

    def mark_as_unvisited(self) -> None:
        for vertex in self:
            vertex.visited = False

    def exist_path(self, origin, destination):
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.value, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result
        
        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result
    
    def deep_sweep(self, value) -> None: # DFS
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.search(edge.value, 'value')
                        if not graph[destination_edge_pos].visited:
                            __deep_sweep(graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)
        
    def amplitude_sweep(self, value)-> None: # BFS
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                queue_vertex.arrive(self[vertex_pos])
                while queue_vertex.size() > 0:
                    vertex = queue_vertex.attention()
                    print(vertex.value) # Imprime solo el nombre para claridad
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
            distance = 0 if vertex.value == origin else math.inf
            # [nombre, objeto_vertice, anterior]
            no_visited.arrive([vertex.value, vertex, None], distance)
            
        while no_visited.size() > 0:
            value = no_visited.attention() # [costo, [nombre, vertice_obj, anterior]]
            costo_nodo_actual = value[0]
            
            # [nombre, costo, anterior]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            
            edges = value[1][1].edges
            for edge in edges:
                pos = no_visited.search(edge.value) # Busca por nombre
                if pos is not None:
                    if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = value[1][0] # Actualiza anterior
                        no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path

    def kruskal(self):

        mst = Graph(is_directed=False) # El nuevo grafo MST
        
        forest = []
        edges = HeapMin()
        
        for vertex in self:
            forest.append({vertex.value}) # Cada vértice es un "bosque" (conjunto)
            mst.insert_vertex(vertex.value, vertex.other_values) # Añadir vértice al MST
            
            for edge in vertex.edges:
                # Añadir arista al heap solo una vez (v.value < e.value)
                if vertex.value < edge.value:
                    edges.arrive([vertex.value, edge.value], edge.weight)
        
        total_weight = 0
        
        while len(forest) > 1 and edges.size() > 0:
            edge_data = edges.attention() # [weight, [origin, dest]]
            weight = edge_data[0]
            origin_val = edge_data[1][0]
            dest_val = edge_data[1][1]

            # Buscar en qué bosque (conjunto) están el origen y el destino
            origin_set_idx = -1
            dest_set_idx = -1
            for i, vertex_set in enumerate(forest):
                if origin_val in vertex_set:
                    origin_set_idx = i
                if dest_val in vertex_set:
                    dest_set_idx = i
            
            # Si están en bosques diferentes, unirlos
            if origin_set_idx != dest_set_idx:
                # 1. Añadir arista al MST
                mst.insert_edge(origin_val, dest_val, weight)
                total_weight += weight
                
                # 2. Unir los bosques (conjuntos)
                # Pop del índice más alto primero para evitar errores de índice
                idx1, idx2 = max(origin_set_idx, dest_set_idx), min(origin_set_idx, dest_set_idx)
                set1 = forest.pop(idx1)
                set2 = forest.pop(idx2)
                forest.append(set1.union(set2))

        return mst, total_weight



def obtener_camino_y_costo(dijkstra_stack: Stack, destination: str):

    
    # 1. Convertir la pila a un diccionario para búsqueda rápida
    #    Formato: { 'NombreVertice': (costo, vertice_anterior) }
    results = {}
    while dijkstra_stack.size() > 0:
        data = dijkstra_stack.pop() # [nombre, costo, anterior]
        results[data[0]] = (data[1], data[2]) 

    # 2. Obtener costo y verificar si se encontró un camino
    costo = results.get(destination, (math.inf, None))[0]
    
    if costo == math.inf:
        return None, math.inf # No hay camino

    # 3. Reconstruir el camino hacia atrás
    path = []
    curr = destination
    while curr is not None:
        path.append(curr)
        if curr not in results: # Caso borde: origen = destino
            break
        curr = results[curr][1] # Moverse al vértice anterior
        
    return list(reversed(path)), costo # Devolver camino (origen -> destino) y costo



# --- a. Cargar el grafo ---
# (h. Usar grafo no dirigido)
g = Graph(is_directed=False)

# Nodos (nombre, tipo)
nodos = [
    ('Manjaro', 'pc'), ('Switch 2', 'switch'), ('Parrot', 'pc'), ('MongoDB', 'servidor'),
    ('Arch', 'notebook'), ('Fedora', 'pc'), ('Router 3', 'router'), ('Guarani', 'servidor'),
    ('Router 2', 'router'), ('Red Hat', 'notebook'), ('Router 1', 'router'),
    ('Switch 1', 'switch'), ('Debian', 'notebook'), ('Ubuntu', 'pc'),
    ('Impresora', 'impresora'), ('Mint', 'pc')
]

for nodo, tipo in nodos:
    g.insert_vertex(nodo, tipo)

# Aristas (origen, destino, peso)
aristas = [
    ('Manjaro', 'Switch 2', 40), ('Parrot', 'Switch 2', 12), ('MongoDB', 'Switch 2', 5),
    ('Arch', 'Switch 2', 56), ('Fedora', 'Switch 2', 3), ('Router 3', 'Switch 2', 61),
    ('Guarani', 'Router 3', 9), ('Router 2', 'Router 3', 50), ('Router 1', 'Router 3', 43),
    ('Red Hat', 'Router 2', 25), ('Router 1', 'Router 2', 37),
    ('Switch 1', 'Router 1', 29), ('Debian', 'Switch 1', 17), ('Ubuntu', 'Switch 1', 18),
    ('Impresora', 'Switch 1', 22), ('Mint', 'Switch 1', 80)
]

for origen, destino, peso in aristas:
    g.insert_edge(origen, destino, peso)

print("Grafo cargado correctamente.")
# g.show() # Descomentar para ver el grafo completo

print("\n" + "="*40 + "\n")

# --- b. Barrido en profundidad y amplitud ---
print("b. Barridos DFS y BFS desde Red Hat, Debian, Arch")
print("-" * 40)

starters = ['Red Hat', 'Debian', 'Arch']
for start_node in starters:
    print(f"\n--- Barrido en Profundidad (DFS) desde {start_node} ---")
    g.deep_sweep(start_node)
    
    print(f"\n--- Barrido en Amplitud (BFS) desde {start_node} ---")
    g.amplitude_sweep(start_node)

print("\n" + "="*40 + "\n")

# --- c. Camino más corto a la impresora ---
print("c. Camino más corto a 'Impresora'")
print("-" * 40)

pcs_imprimir = ['Manjaro', 'Red Hat', 'Fedora']
destino_impresora = 'Impresora'

for pc in pcs_imprimir:
    dijkstra_results = g.dijkstra(pc)
    path, cost = obtener_camino_y_costo(dijkstra_results, destino_impresora)
    
    if path:
        print(f"Camino de {pc} a {destino_impresora} (Costo: {cost}):")
        print(f"  Ruta: {' -> '.join(path)}")
    else:
        print(f"No hay ruta de {pc} a {destino_impresora}.")

print("\n" + "="*40 + "\n")

# --- d. Árbol de expansión mínima ---
print("d. Árbol de Expansión Mínima (Kruskal)")
print("-" * 40)

mst, total_weight = g.kruskal()
print("Aristas del Árbol de Expansión Mínima:")
mst.show()
print(f"Costo total del MST: {total_weight}")

print("\n" + "="*40 + "\n")

# --- e. PC (no notebook) más cercana a "Guaraní" ---
print("e. PC (no notebook) con camino más corto a 'Guarani'")
print("-" * 40)

target_server_e = 'Guarani'
shortest_cost_e = math.inf
shortest_pc_e = None
shortest_path_e = []

for vertex in g:
    if vertex.other_values == 'pc': # Solo 'pc', no 'notebook'
        dijkstra_results = g.dijkstra(vertex.value)
        path, cost = obtener_camino_y_costo(dijkstra_results, target_server_e)
        
        if cost < shortest_cost_e:
            shortest_cost_e = cost
            shortest_pc_e = vertex.value
            shortest_path_e = path

if shortest_pc_e:
    print(f"La PC (no notebook) más cercana a {target_server_e} es: {shortest_pc_e}")
    print(f"  Costo: {shortest_cost_e}")
    print(f"  Ruta: {' -> '.join(shortest_path_e)}")
else:
    print(f"No se encontró camino desde ninguna PC a {target_server_e}.")

print("\n" + "="*40 + "\n")

# --- f. Computadora de Switch 1 más cercana a "MongoDB" ---
print("f. Computadora de 'Switch 1' con camino más corto a 'MongoDB'")
print("-" * 40)

target_server_f = 'MongoDB'
computadoras_switch1 = []

# Encontrar nodos conectados a Switch 1
pos_switch1 = g.search('Switch 1', 'value')
if pos_switch1 is not None:
    for edge in g[pos_switch1].edges:
        pos_device = g.search(edge.value, 'value')
        if pos_device is not None:
            device_type = g[pos_device].other_values
            if device_type in ['pc', 'notebook']:
                computadoras_switch1.append(g[pos_device].value)

print(f"Computadoras conectadas a Switch 1: {computadoras_switch1}")

shortest_cost_f = math.inf
shortest_comp_f = None
shortest_path_f = []

for comp in computadoras_switch1:
    dijkstra_results = g.dijkstra(comp)
    path, cost = obtener_camino_y_costo(dijkstra_results, target_server_f)
    
    if cost < shortest_cost_f:
        shortest_cost_f = cost
        shortest_comp_f = comp
        shortest_path_f = path

if shortest_comp_f:
    print(f"La computadora (de Switch 1) más cercana a {target_server_f} es: {shortest_comp_f}")
    print(f"  Costo: {shortest_cost_f}")
    print(f"  Ruta: {' -> '.join(shortest_path_f)}")
else:
    print(f"No se encontró camino desde computadoras en Switch 1 a {target_server_f}.")

print("\n" + "="*40 + "\n")

# --- g. Cambiar conexión de Impresora y repetir punto b ---
print("g. Mover 'Impresora' a 'Router 2' y repetir barridos")
print("-" * 40)

# 1. Borrar la arista vieja (Impresora <-> Switch 1)
g.delete_edge('Impresora', 'Switch 1')
print("Arista 'Impresora' <-> 'Switch 1' eliminada.")

# 2. Añadir la arista nueva (Impresora <-> Router 2)
#    Usamos el peso original (22) como referencia
g.insert_edge('Impresora', 'Router 2', 22)
print("Arista 'Impresora' <-> 'Router 2' (peso 22) añadida.")

print("\n--- Repitiendo barridos (punto b) con grafo modificado ---")
for start_node in starters:
    print(f"\n--- Barrido en Profundidad (DFS) desde {start_node} (Modificado) ---")
    g.deep_sweep(start_node)
    
    print(f"\n--- Barrido en Amplitud (BFS) desde {start_node} (Modificado) ---")
    g.amplitude_sweep(start_node)

print("\n" + "="*40 + "\n")
print("Proceso completado.")