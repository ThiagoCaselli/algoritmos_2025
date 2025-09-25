from typing import Any, Optional
from cola import Queue
from tree import BinaryTree


# Funciones auxiliares para los incisos

def heroes_starting_with_C(tree: BinaryTree):
    results = []
    def _traverse(root):
        if root is None:
            return
        _traverse(root.left)
        if root.other_values and root.other_values.get("is_villain") is False:
            if root.value.startswith("C"):
                results.append(root.value)
        _traverse(root.right)
    _traverse(tree.root)
    for name in results:
        print(name)
    return results

def proximity_modify(tree: BinaryTree, prefix: str, new_value: str):
    modified = False
    def _search_and_modify(root):
        nonlocal modified
        if root is None or modified:
            return
        _search_and_modify(root.left)
        if not modified:
            if isinstance(root.value, str) and root.value.startswith(prefix):
                print("Nodo encontrado (antes):", root.value)
                root.value = new_value
                print("Nodo modificado (después):", root.value)
                modified = True
                return
        _search_and_modify(root.right)
    _search_and_modify(tree.root)
    return modified

def list_heroes_desc(tree: BinaryTree):
    results = []
    def _reverse_in_order(root):
        if root is None:
            return
        _reverse_in_order(root.right)
        if root.other_values and root.other_values.get("is_villain") is False:
            results.append(root.value)
        _reverse_in_order(root.left)
    _reverse_in_order(tree.root)
    for name in results:
        print(name)
    return results

def count_nodes(tree: BinaryTree):
    def _count(root):
        if root is None:
            return 0
        return 1 + _count(root.left) + _count(root.right)
    return _count(tree.root)

def in_order_collect(tree: BinaryTree):
    res = []
    def _in(root):
        if root is None:
            return
        _in(root.left)
        res.append(root.value)
        _in(root.right)
    _in(tree.root)
    return res


# Construcción del árbol MCU de ejemplo

def build_mcu_tree():
    t = BinaryTree()
    personajes = [
        ("Iron Man", {"is_villain": False}),
        ("Captain America", {"is_villain": False}),
        ("Captain Marvel", {"is_villain": False}),
        ("Black Widow", {"is_villain": False}),
        ("Hulk", {"is_villain": False}),
        ("Thor", {"is_villain": False}),
        ("Dr Strange", {"is_villain": False}),  # mal cargado a propósito
        ("Scarlet Witch", {"is_villain": False}),
        ("Loki", {"is_villain": True}),
        ("Thanos", {"is_villain": True}),
        ("Ultron", {"is_villain": True}),
        ("Red Skull", {"is_villain": True}),
        ("Ghost", {"is_villain": True}),
        ("Crossbones", {"is_villain": True}),
        ("Cable", {"is_villain": False}),
        ("Cat", {"is_villain": False}),
    ]
    for nombre, info in personajes:
        t.insert(nombre, info)
    return t


# Programa principal

if __name__ == "__main__":
    tree = build_mcu_tree()

    print("b) Villanos ordenados")
    tree.villain_in_order()

    print("\nc) Héroes que empiezan con 'C'")
    heroes_starting_with_C(tree)

    print("\nd) Cantidad de héroes")
    print(tree.count_heroes())

    print("\ne) Corregir Doctor Strange")
    proximity_modify(tree, "Dr", "Doctor Strange")

    print("\nf) Héroes descendente")
    list_heroes_desc(tree)

    print("\ng) Bosque héroes / villanos")
    tree_heroes = BinaryTree()
    tree_villains = BinaryTree()
    tree.divide_tree(tree_heroes, tree_villains)

    print("g.I) Nodos héroes:", count_nodes(tree_heroes),
          " | Nodos villanos:", count_nodes(tree_villains))
    print()

    print("g.II) Héroes en orden alfabético:")
    for n in in_order_collect(tree_heroes):
        print(n)
    print()
        
    print("g.II) Villanos en orden alfabético:")
    for n in in_order_collect(tree_villains):
        print(n)
