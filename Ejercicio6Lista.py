from Parcial.list_ import List
from Parcial.super_heroes_data import superheroes
from typing import Optional

class Superhero:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villian):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villian = is_villian

    def __str__(self):
        return f"{self.name}, {self.real_name} - {'Villano' if self.is_villian else 'Héroe'}"

# Función de orden
def order_by_name(item):
    return item.name

# Crear lista y cargar datos
list_superhero = List()
list_superhero.add_criterion('name', order_by_name)

for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villian=superhero["is_villian"],
    )
    list_superhero.append(hero)

# A. Eliminar a Groot
print("A. Eliminar a Groot:")
print(list_superhero.delete_value('Groot', 'name'))
print()

# B. Año aparición Wolverine
print("B. Año aparición de Wolverine:")
index = list_superhero.search('Wolverine', 'name')
if index is not None:
    print(list_superhero[index].first_appearance)
else:
    print('El superhéroe no está en la lista')
print()

# C. Dr Strange de villano a héroe
print("C. Cambiar Dr Strange a héroe:")
index = list_superhero.search('Dr Strange', 'name')
if index is not None:
    list_superhero[index].is_villian = False
    print(f"Estado actual: {list_superhero[index].is_villian}")
else:
    print('El superhéroe no está en la lista')
print()

# D. Superhéroes que mencionan 'traje' o 'armadura'
print("D. Superhéroes con 'traje' o 'armadura':")
for superhero in list_superhero:
    bio = superhero.short_bio.lower()
    if 'traje' in bio or 'armadura' in bio or 'suit' in bio or 'armor' in bio:
        print(superhero)
print()

# E. Superhéroes con aparición antes de 1963
print("E. Superhéroes anteriores a 1963:")
for superhero in list_superhero:
    try:
        if int(superhero.first_appearance) < 1963:
            print(f"{superhero.name} - {superhero.alias}")
    except:
        continue
print()

# F. Casa de Capitana Marvel y Mujer Maravilla
print("F. Casa de Capitana Marvel y Mujer Maravilla:")
for nombre in ['Capitana Marvel', 'Mujer Maravilla']:
    index = list_superhero.search(nombre, 'name')
    if index is not None:
        print(f"{nombre}: {list_superhero[index].alias}")
    else:
        print(f"{nombre}: No encontrada")
print()

# G. Mostrar toda la info de Flash y Star-Lord
print("G. Info completa de Flash y Star-Lord:")
for nombre in ['Flash', 'Star-Lord']:
    index = list_superhero.search(nombre, 'name')
    if index is not None:
        hero = list_superhero[index]
        print(f"{hero.name} ({hero.real_name}) - {hero.alias}")
        print(f"  Aparición: {hero.first_appearance}")
        print(f"  Bio: {hero.short_bio}")
        print(f"  {'Villano' if hero.is_villian else 'Héroe'}")
        print()
    else:
        print(f"{nombre} no encontrado")
print()

# H. Superhéroes que comienzan con B, M o S
print("H. Superhéroes que comienzan con B, M o S:")
for superhero in list_superhero:
    if superhero.name[0].upper() in ['B', 'M', 'S']:
        print(superhero)
print()

# I. Contar cuántos superhéroes hay por casa
print("I. Cantidad por casa:")
conteo_casa = {}
for hero in list_superhero:
    casa = hero.alias
    conteo_casa[casa] = conteo_casa.get(casa, 0) + 1
for casa, cantidad in conteo_casa.items():
    print(f"{casa}: {cantidad}")


