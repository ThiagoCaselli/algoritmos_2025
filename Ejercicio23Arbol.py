from collections import Counter
from tree import BinaryTree

# Cargar criaturas en el árbol

arbol = BinaryTree()

criaturas = [
    ("Ceto", None),
    ("Tifón", "Zeus"),
    ("Equidna", "Argos Panoptes"),
    ("Dino", None),
    ("Pefredo", None),
    ("Enio", None),
    ("Escila", None),
    ("Caribdis", None),
    ("Euríale", None),
    ("Esteno", None),
    ("Medusa", "Perseo"),
    ("Ladón", "Heracles"),
    ("Águila del Cáucaso", None),
    ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"),
    ("Dragón de la Cólquida", None),
    ("Cerbero", None),
    ("Cerda de Cromión", "Teseo"),
    ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"),
    ("Jabalí de Calidón", "Atalanta"),
    ("Carcinos", None),
    ("Gerión", "Heracles"),
    ("Cloto", None),
    ("Láquesis", None),
    ("Átropos", None),
    ("Minotauro de Creta", "Teseo"),
    ("Harpías", None),
    ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", None),
    ("Talos", "Medea"),
    ("Sirenas", None),
    ("Pitón", "Apolo"),
    ("Cierva de Cerinea", None),
    ("Basilisco", None),
    ("Jabalí de Erimanto", None)
]

for criatura, derrotado in criaturas:
    arbol.insert(
        criatura,
        {
            "derrotado_por": derrotado,
            "descripcion": "",
            "capturada": None
        }
    )


# Funciones auxiliares para resolver incisos

def inorden_con_derrotado(arbol):
    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            print(root.value, "→ derrotado por:", root.other_values["derrotado_por"], 
                  "| capturado:", root.other_values["capturada"])
            __inorden(root.right)
    __inorden(arbol.root)

def top_3_heroes(arbol):
    counter = Counter()
    def __recorrer(root):
        if root:
            if root.other_values["derrotado_por"]:
                counter[root.other_values["derrotado_por"]] += 1
            __recorrer(root.left)
            __recorrer(root.right)
    __recorrer(arbol.root)
    return counter.most_common(3)

def criaturas_derrotadas_por(arbol, heroe):
    def __recorrer(root):
        if root:
            if root.other_values["derrotado_por"] == heroe:
                print(root.value)
            __recorrer(root.left)
            __recorrer(root.right)
    __recorrer(arbol.root)

def no_derrotadas(arbol):
    def __recorrer(root):
        if root:
            if root.other_values["derrotado_por"] is None:
                print(root.value)
            __recorrer(root.left)
            __recorrer(root.right)
    __recorrer(arbol.root)

def capturadas_por(arbol, heroe):
    def __recorrer(root):
        if root:
            if root.other_values["capturada"] == heroe:
                print(root.value)
            __recorrer(root.left)
            __recorrer(root.right)
    __recorrer(arbol.root)


# Ejecución

print("\na) Listado inorden")
inorden_con_derrotado(arbol)

print("\nb) Cargar descripción de Medusa")
nodo = arbol.search("Medusa")
if nodo:
    nodo.other_values["descripcion"] = "Gorgona con serpientes por cabello."
    print(nodo.value, nodo.other_values)

print("\nc) Mostrar información de Talos")
nodo = arbol.search("Talos")
if nodo:
    print(nodo.value, nodo.other_values)

print("\nd) Top 3 héroes o dioses")
print(top_3_heroes(arbol))

print("\ne) Criaturas derrotadas por Heracles")
criaturas_derrotadas_por(arbol, "Heracles")

print("\nf) Criaturas no derrotadas")
no_derrotadas(arbol)

print("\ng+h) Capturadas por Heracles")
for criatura in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]:
    nodo = arbol.search(criatura)
    if nodo:
        nodo.other_values["capturada"] = "Heracles"
capturadas_por(arbol, "Heracles")

print("\ni) Búsqueda por coincidencia ('C')")
arbol.proximity_search("C")

print("\nj) Eliminar Basilisco y Sirenas")
arbol.delete("Basilisco")
arbol.delete("Sirenas")
inorden_con_derrotado(arbol)

print("\nk) Modificar Aves del Estínfalo")
nodo = arbol.search("Aves del Estínfalo")
if nodo:
    nodo.other_values["derrotado_por"] = "Heracles"
inorden_con_derrotado(arbol)

print("\nl) Renombrar Ladón a Dragón Ladón")
val, other = arbol.delete("Ladón")
if val:
    arbol.insert("Dragón Ladón", other)
inorden_con_derrotado(arbol)

print("\nm) Listado por nivel")
arbol.by_level()

print("\nn) Criaturas capturadas por Heracles")
capturadas_por(arbol, "Heracles")
