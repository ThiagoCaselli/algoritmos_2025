from super_heroes_data import superheroes
from list_ import List
from cola import Queue

superheroes_list = List(superheroes) 

superheroes_list.add_criterion("name", lambda x: x["name"])
superheroes_list.add_criterion("real_name", lambda x: x["real_name"])
superheroes_list.add_criterion("first_appearance", lambda x: x["first_appearance"])

# 1. Listado ordenado de manera ascendente por nombre de los personajes
print("1. Personajes ordenados por nombre:")
superheroes_list.sort_by_criterion("name")
superheroes_list.show()

# 2. Determinar en que posición están The Thing y Rocket Raccoon
superheroes_list.sort_by_criterion("name")
thing_pos = superheroes_list.search("The Thing", "name")
raccoon_pos = superheroes_list.search("Rocket Raccoon", "name")
print(f"\n2. Posiciones:")
print(f"The Thing está en la posición: {thing_pos}")
print(f"Rocket Raccoon está en la posición: {raccoon_pos}")

# 3. Listar todos los villanos de la lista
print("\n3. Todos los villanos:")
villains = List([c for c in superheroes_list if c["is_villain"]])
villains.sort_by_criterion("name")
villains.show()

# 4. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980
villains_queue = Queue()
for villain in villains:
    villains_queue.arrive(villain)

print("\n4. Villanos que aparecieron antes de 1980:")
pre_1980_villains = List()
while villains_queue.size() > 0:
    villain = villains_queue.attention()
    if villain["first_appearance"] < 1980:
        pre_1980_villains.append(villain)
pre_1980_villains.sort_by_criterion("name")
pre_1980_villains.show()

# 5. Listar los superhéroes que comienzan con Bl, G, My, y W
prefixes = ["Bl", "G", "My", "W"]
print("\n5. Superhéroes que comienzan con Bl, G, My, W:")
filtered_heroes = List()
for c in superheroes_list:
    if not c["is_villain"]:
        for prefix in prefixes:
            if c["name"].startswith(prefix):
                filtered_heroes.append(c)
                break
filtered_heroes.sort_by_criterion("name")
filtered_heroes.show()

# 6. Listado de personajes ordenado por nombre real de manera ascendente
print("\n6. Personajes ordenados por nombre real:")
superheroes_list.sort_by_criterion("real_name")
superheroes_list.show()

# 7. Listado de superhéroes ordenados por fecha de aparición
print("\n7. Superhéroes ordenados por fecha de aparición:")
heroes = List([c for c in superheroes_list if not c["is_villain"]])
heroes.sort_by_criterion("first_appearance")
heroes.show()

# 8. Modificar el nombre real de Ant Man a Scott Lang
print("\n8. Modificando nombre real de Ant Man:")
for c in superheroes_list:
    if c["name"] == "Ant Man":
        c["real_name"] = "Scott Lang"
        print(f"Nombre real cambiado de Hank Pym a {c['real_name']}")
        break

# 9. Mostrar los personajes que en su biografía incluyan la palabra time-traveling o suit
print("\n9. Personajes con 'time-traveling' o 'suit' en su biografía:")
keywords = ["time-traveling", "suit"]
filtered_chars = List()
for c in superheroes_list:
    bio = c["short_bio"].lower()
    if any(keyword in bio for keyword in keywords):
        filtered_chars.append(c)
filtered_chars.sort_by_criterion("name")
filtered_chars.show()

# 10. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista
print("\n10. Eliminando Electro y Baron Zemo:")
electro = superheroes_list.delete_value("Electro", "name")
if electro:
    print("Electro eliminado:")
    print(electro)
else:
    print("Electro no encontrado")

baron_zemo = superheroes_list.delete_value("Baron Zemo", "name")
if baron_zemo:
    print("Baron Zemo eliminado:")
    print(baron_zemo)
else:
    print("Baron Zemo no encontrado")