from __future__ import annotations
import sys
from queue import Queue
from typing import Any, Optional

class BinaryTree:

    class __nodeTree:
        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value  
            self.other_values = other_values  
            self.left: Optional[BinaryTree.__nodeTree] = None
            self.right: Optional[BinaryTree.__nodeTree] = None
            self.hight = 0

    def __init__(self):
        self.root: Optional[BinaryTree.__nodeTree] = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)
            
            root = self.auto_balance(root)
            self.update_hight(root)
            return root

        self.root = __insert(self.root, value, other_values)

    def search(self, value: Any) -> Optional[__nodeTree]:
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value > value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)
            return None
        
        return __search(self.root, value)

    def by_level(self):
        """ Recorrido por nivel """
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.put(self.root)
            while tree_queue.qsize() > 0:
                node = tree_queue.get()
                print(f"  - {node.value}") 
                if node.left is not None:
                    tree_queue.put(node.left)
                if node.right is not None:
                    tree_queue.put(node.right)

    
    def hight(self, root: Optional[__nodeTree]) -> int:
        return root.hight if root else -1

    def update_hight(self, root: Optional[__nodeTree]):
        if root is not None:
            alt_left = self.hight(root.left)
            alt_right = self.hight(root.right)
            root.hight = max(alt_left, alt_right) + 1

    def simple_rotation(self, root: __nodeTree, control: bool) -> __nodeTree:
        if control: # RS Right
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # RS Left
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_hight(root)
        self.update_hight(aux)
        return aux

    def double_rotation(self, root: __nodeTree, control: bool) -> __nodeTree:
        if control: # RD Right
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: # RD Left
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def auto_balance(self, root: Optional[__nodeTree]) -> Optional[__nodeTree]:
        if root is not None:
            if self.hight(root.left) - self.hight(root.right) == 2:
                if self.hight(root.left.left) >= self.hight(root.left.right):
                    root = self.simple_rotation(root, True) # RS
                else:
                    root = self.double_rotation(root, True) # RD
            elif self.hight(root.right) - self.hight(root.left) == 2:
                if self.hight(root.right.right) >= self.hight(root.right.left):
                    root = self.simple_rotation(root, False) # LS
                else:
                    root = self.double_rotation(root, False) # LD
        return root


    def in_order_traversal(self, func):
        """ Función genérica para recorrer in-order y aplicar una función """
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                func(root)
                __in_order(root.right)
        __in_order(self.root)

    # b) Búsqueda por proximidad (contiene o comienza con)
    def search_by_proximity(self, value: str) -> list[dict]:
        """ 
        Recorre el árbol (in-order) y devuelve una lista de datos de Pokémon
        cuyos nombres (clave) contengan el 'value'.
        """
        results = []
        value_lower = value.lower()
        
        def check_proximity(node):
            key_lower = str(node.value).lower()
            if value_lower in key_lower:
                results.append(node.other_values)

        self.in_order_traversal(check_proximity)
        return results

    # e) Búsqueda por debilidad
    def get_pokemon_weak_to(self, attack_types: set) -> list[dict]:
        """ 
        Recorre el árbol y devuelve una lista de Pokémon que son débiles
        a CUALQUIERA de los tipos en 'attack_types'.
        """
        results = []
        
        def check_weakness(node):
            pokemon_data = node.other_values
            pokemon_weaknesses = set(pokemon_data["debilidades"])
            
            # Comprueba si hay intersección (si no son disjuntos)
            if not attack_types.isdisjoint(pokemon_weaknesses):
                results.append(pokemon_data)
        
        self.in_order_traversal(check_weakness)
        return results

    # g) y h) Conteo de Megaevolución y Gigamax
    def count_by_bool_field(self, field_name: str) -> int:
        """ 
        Cuenta cuántos Pokémon (nodos) tienen un campo booleano 
        específico en 'True'.
        """
        # Usamos una lista mutable (o un dict) para pasar por referencia
        counter = [0] 
        
        def count_field(node):
            if node.other_values.get(field_name) is True:
                counter[0] += 1

        self.in_order_traversal(count_field)
        return counter[0]


# DATOS DE EJEMPLO

pokemon_data = [
    {"nombre": "Bulbasaur", "numero": 1, "tipos": ["Planta", "Veneno"], "debilidades": ["Fuego", "Hielo", "Volador", "Psíquico"], "mega": False, "gigamax": True},
    {"nombre": "Ivysaur", "numero": 2, "tipos": ["Planta", "Veneno"], "debilidades": ["Fuego", "Hielo", "Volador", "Psíquico"], "mega": False, "gigamax": False},
    {"nombre": "Venusaur", "numero": 3, "tipos": ["Planta", "Veneno"], "debilidades": ["Fuego", "Hielo", "Volador", "Psíquico"], "mega": True, "gigamax": True},
    {"nombre": "Charmander", "numero": 4, "tipos": ["Fuego"], "debilidades": ["Agua", "Tierra", "Roca"], "mega": False, "gigamax": True},
    {"nombre": "Charizard", "numero": 6, "tipos": ["Fuego", "Volador"], "debilidades": ["Agua", "Eléctrico", "Roca"], "mega": True, "gigamax": True},
    {"nombre": "Pikachu", "numero": 25, "tipos": ["Eléctrico"], "debilidades": ["Tierra"], "mega": False, "gigamax": True},
    {"nombre": "Jolteon", "numero": 135, "tipos": ["Eléctrico"], "debilidades": ["Tierra"], "mega": False, "gigamax": False},
    {"nombre": "Gengar", "numero": 94, "tipos": ["Fantasma", "Veneno"], "debilidades": ["Tierra", "Psíquico", "Fantasma", "Siniestro"], "mega": True, "gigamax": True},
    {"nombre": "Steelix", "numero": 208, "tipos": ["Acero", "Tierra"], "debilidades": ["Fuego", "Agua", "Lucha", "Tierra"], "mega": True, "gigamax": False},
    {"nombre": "Lycanroc", "numero": 745, "tipos": ["Roca"], "debilidades": ["Agua", "Planta", "Lucha", "Tierra", "Acero"], "mega": False, "gigamax": False},
    {"nombre": "Tyrantrum", "numero": 697, "tipos": ["Roca", "Dragón"], "debilidades": ["Hielo", "Lucha", "Tierra", "Acero", "Dragón", "Hada"], "mega": False, "gigamax": False},
    {"nombre": "Bulbapedia", "numero": 1026, "tipos": ["Psíquico"], "debilidades": ["Bicho"], "mega": False, "gigamax": False},
]


# LÓGICA PRINCIPAL DEL EJERCICIO

if __name__ == "__main__":
    
    # a) Creación de los tres árboles
    tree_by_name = BinaryTree()
    tree_by_number = BinaryTree()
    tree_by_type = BinaryTree()

    print("Cargando Pokémon en los árboles...")

    for pokemon in pokemon_data:
        # 1. Insertar en el árbol por nombre
        tree_by_name.insert(pokemon["nombre"], pokemon)
        
        # 2. Insertar en el árbol por número
        tree_by_number.insert(pokemon["numero"], pokemon)
        
        # 3. Insertar en el árbol por tipo 
        for tipo in pokemon["tipos"]:
            node = tree_by_type.search(tipo)
            if node is None:
                # Si el tipo no existe, lo insertamos con una nueva lista
                tree_by_type.insert(tipo, other_values=[pokemon])
            else:
                # Si el tipo ya existe, añadimos el pokémon a la lista existente
                node.other_values.append(pokemon)

    print("¡Carga completada!")

    
    # b) Búsquedas por número y nombre
    print()
    print("b) BÚSQUEDAS")
    

    # Por número (Búsqueda exacta)
    numero_buscar = 135
    print(f"\nBuscando Pokémon número {numero_buscar}:")
    node_num = tree_by_number.search(numero_buscar)
    if node_num:
        print(f"  Encontrado: {node_num.other_values}")
    else:
        print(f"  No se encontró el Pokémon {numero_buscar}")

    # Por nombre (Búsqueda por proximidad "bul")
    texto_buscar = "Bul"
    print(f"\nBuscando Pokémon por proximidad '{texto_buscar}':")
    resultados_prox = tree_by_name.search_by_proximity(texto_buscar)
    if resultados_prox:
        for p in resultados_prox:
            print(f"  Encontrado: {p}")
    else:
        print(f"  No se encontraron Pokémon que contengan '{texto_buscar}'")

    
    # c) Pokémon por tipo específico 
    print()
    print("c) POKÉMON POR TIPO (FANTASMA, FUEGO, ACERO, ELÉCTRICO)")


    tipos_a_mostrar = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
    for tipo in tipos_a_mostrar:
        print(f"\nPokémon de tipo: {tipo}")
        node_tipo = tree_by_type.search(tipo)
        if node_tipo:
            # node_tipo.other_values es la lista de pokémons
            for pokemon in node_tipo.other_values:
                print(f"  - {pokemon['nombre']}")
        else:
            print("  (Ninguno en la base de datos de ejemplo)")

            
    # d) Listados
    print()
    print("d) LISTADOS")
    

    # Listado ascendente por NÚMERO
    print("\nListado por Número (In-Order)")
    def print_by_number(node):
        print(f"  N°: {node.value} - Nombre: {node.other_values['nombre']}")
    tree_by_number.in_order_traversal(print_by_number)


    # Listado ascendente por NOMBRE
    print("\nListado por Nombre (In-Order)")
    def print_by_name(node):
        print(f"  Nombre: {node.value}")
    tree_by_name.in_order_traversal(print_by_name)


    # Listado por Nivel (del árbol de nombres)
    print("\nListado por Nivel (Árbol de Nombres)")
    tree_by_name.by_level()

    
    # e) Débiles frente a Jolteon, Lycanroc y Tyrantrum 
    print()
    print("e) DÉBILES CONTRA JOLTEON, LYCANROC Y TYRANTRUM")
    print()
    

    # 1. Obtenemos los tipos de ataque de esos Pokémon
    attack_types = set()
    for name in ["Jolteon", "Lycanroc", "Tyrantrum"]:
        node = tree_by_name.search(name)
        if node:
            attack_types.update(node.other_values["tipos"])

    print(f"Tipos de ataque considerados: {attack_types}")

    # 2. Recorremos el árbol (por nombre) y comprobamos debilidades
    pokemon_debiles = tree_by_name.get_pokemon_weak_to(attack_types)
    print("\nPokémon que son débiles a esos tipos:")
    if pokemon_debiles:
        for p in pokemon_debiles:
            print(f"  - {p['nombre']} (Débil a: {p['debilidades']})")
    else:
        print("  Ninguno.")

        
    # f) Conteo de todos los tipos 
    print()
    print("f) CONTEO DE POKÉMON POR TIPO")
    print()

    
    def print_type_count(node):
        # La clave (node.value) es el tipo
        # other_values (node.other_values) es la lista de pokémons
        print(f"  Tipo: {node.value}, Cantidad: {len(node.other_values)}")
    
    tree_by_type.in_order_traversal(print_type_count)

    
    # g) y h) Conteo de Megaevolución y Gigamax
    print()
    print("g) y h) CONTEO DE MEGAEVOLUCIÓN Y GIGAMAX")
    print()


    # Usamos el árbol por nombre (o por número) para el conteo
    count_mega = tree_by_name.count_by_bool_field("mega")
    count_gigamax = tree_by_name.count_by_bool_field("gigamax")

    print(f"Total de Pokémon con Megaevolución: {count_mega}")
    print(f"Total de Pokémon con forma Gigamax: {count_gigamax}")