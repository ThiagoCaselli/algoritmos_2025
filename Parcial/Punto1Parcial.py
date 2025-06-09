# Lista de 15 superhéroes
superheroes = [
    "Iron Man", "Spider-Man", "Hulk", "Thor", "Viuda Negra",
    "Ojo de Halcón", "Pantera Negra", "Doctor Strange", "Bruja Escarlata",
    "Ant-Man", "Wasp", "Falcon", "Capitán América", "Winter Soldier", "Vision"
]

def buscar_capitan_america(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Capitán América":
        return True
    return buscar_capitan_america(lista, indice + 1)

def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(lista[indice])
    listar_superheroes(lista, indice + 1)

# Buscar a Capitán América
en_lista = buscar_capitan_america(superheroes)
print("¿Está Capitán América en la lista?", "Sí" if en_lista else "No")

# Listar todos los superhéroes
print("Lista de superhéroes:")
listar_superheroes(superheroes)


