from typing import Any, Optional
import difflib

class BinaryTree:

    class __nodeTree:
        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value                # nombre
            self.other_values = other_values  # True = héroe, False = villano
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # -------------------- INSERTAR --------------------
    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)
            return root
        self.root = __insert(self.root, value, other_values)

    # -------------------- RECORRIDOS --------------------
    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value)
                __pre_order(root.left)
                __pre_order(root.right)
        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value)
                __in_order(root.right)
        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)
        if self.root is not None:
            __post_order(self.root)

    # -------------------- BUSCAR (exacto) --------------------
    def search(self, value: Any):
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value > value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)
        return __search(self.root, value) if self.root is not None else None

    # -------------------- b. LISTAR VILLANOS ORDENADOS --------------------
    def listar_villanos(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                if root.other_values is False:
                    print(root.value)
                __in_order(root.right)
        __in_order(self.root)

    # -------------------- c. HÉROES QUE EMPIEZAN CON C --------------------
    def heroes_con_c(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                if root.other_values is True and root.value.upper().startswith("C"):
                    print(root.value)
                __in_order(root.right)
        __in_order(self.root)

    # -------------------- d. CONTAR HÉROES --------------------
    def contar_heroes(self) -> int:
        def __contar(root):
            if root is None:
                return 0
            return __contar(root.left) + __contar(root.right) + (1 if root.other_values else 0)
        return __contar(self.root)

    # -------------------- e. BÚSQUEDA POR PROXIMIDAD --------------------
    def buscar_proximidad(self, nombre: str, umbral: float = 0.7):
        """
        Devuelve una lista de nodos cuyo nombre es similar al buscado,
        usando la similitud de difflib (0..1). umbral por defecto 0.7
        """
        similares = []
        def __recorrer(root):
            if root is not None:
                score = difflib.SequenceMatcher(None, nombre.lower(), root.value.lower()).ratio()
                if score >= umbral:
                    similares.append((score, root))
                __recorrer(root.left)
                __recorrer(root.right)
        __recorrer(self.root)
        # ordena del más similar al menos similar
        similares.sort(key=lambda x: x[0], reverse=True)
        return [n for _, n in similares]

    def corregir_nombre_proximo(self, nombre_buscado: str, nombre_correcto: str, umbral: float = 0.7) -> bool:
        """
        Encuentra el nodo más parecido a 'nombre_buscado' y cambia su value a 'nombre_correcto'.
        Retorna True si corrigió algo.
        """
        candidatos = self.buscar_proximidad(nombre_buscado, umbral)
        if candidatos:
            candidatos[0].value = nombre_correcto
            return True
        return False

    # -------------------- f. HÉROES ORDENADOS DESCENDENTE --------------------
    def heroes_descendente(self):
        def __inverso(root):
            if root is not None:
                __inverso(root.right)
                if root.other_values:
                    print(root.value)
                __inverso(root.left)
        __inverso(self.root)

    # -------------------- g. GENERAR BOSQUE --------------------
    def generar_bosque(self):
        arbol_heroes = BinaryTree()
        arbol_villanos = BinaryTree()
        def __recorrer(root):
            if root is not None:
                if root.other_values:
                    arbol_heroes.insert(root.value, True)
                else:
                    arbol_villanos.insert(root.value, False)
                __recorrer(root.left)
                __recorrer(root.right)
        __recorrer(self.root)
        return arbol_heroes, arbol_villanos

    # -------------------- EXTRA: CONTAR NODOS --------------------
    def contar_nodos(self) -> int:
        def __contar(root):
            if root is None:
                return 0
            return 1 + __contar(root.left) + __contar(root.right)
        return __contar(self.root)


# ================== EJEMPLO DE USO ==================
if __name__ == "__main__":
    arbol = BinaryTree()
    arbol.insert("Iron Man", True)
    arbol.insert("Thanos", False)
    arbol.insert("Captain America", True)
    arbol.insert("Loki", False)
    arbol.insert("Doctro Strange", True)  # mal escrito
    arbol.insert("Hulk", True)
    arbol.insert("Ultron", False)

    print("\n--- b) Villanos ordenados ---")
    arbol.listar_villanos()

    print("\n--- c) Héroes que empiezan con C ---")
    arbol.heroes_con_c()

    print("\n--- d) Cantidad de héroes ---")
    print(arbol.contar_heroes())

    print("\n--- e) Corregir Doctor Strange por proximidad ---")
    if arbol.corregir_nombre_proximo("Doctor Strange", "Doctor Strange", umbral=0.7):
        print("Corregido.")
    else:
        print("No se encontró candidato.")
    arbol.in_order()

    print("\n--- f) Héroes ordenados descendente ---")
    arbol.heroes_descendente()

    print("\n--- g) Bosque de héroes y villanos ---")
    heroes, villanos = arbol.generar_bosque()
    print("Cantidad de héroes:", heroes.contar_nodos())
    print("Cantidad de villanos:", villanos.contar_nodos())

    print("\nHéroes (A-Z):")
    heroes.in_order()
    print("\nVillanos (A-Z):")
    villanos.in_order()
