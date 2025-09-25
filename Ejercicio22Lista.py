from typing import Optional, Any
from Parcial.list_ import List


# ---- Datos de ejemplo ----
jedis = List([
    {"nombre": "Ahsoka Tano", "maestros": ["Anakin Skywalker"], 
     "colores": ["verde", "azul", "blanco"], "especie": "togruta"},
    {"nombre": "Kit Fisto", "maestros": ["Yoda"], 
     "colores": ["verde"], "especie": "nautolan"},
    {"nombre": "Luke Skywalker", "maestros": ["Yoda", "Obi-Wan Kenobi"], 
     "colores": ["verde", "azul"], "especie": "humano"},
    {"nombre": "Anakin Skywalker", "maestros": ["Obi-Wan Kenobi"], 
     "colores": ["azul"], "especie": "humano"},
    {"nombre": "Yoda", "maestros": [], 
     "colores": ["verde"], "especie": "desconocida"},
    {"nombre": "Qui-Gon Jinn", "maestros": ["Conde Dooku"], 
     "colores": ["verde"], "especie": "humano"},
    {"nombre": "Mace Windu", "maestros": ["Cyslin Myr"], 
     "colores": ["violeta"], "especie": "humano"},
    {"nombre": "Aayla Secura", "maestros": ["Quinlan Vos"], 
     "colores": ["azul"], "especie": "twi'lek"},
    {"nombre": "Rey", "maestros": ["Leia Organa", "Luke Skywalker"], 
     "colores": ["azul", "amarillo"], "especie": "humano"},
])

#Criterios de orden/búsqueda
jedis.add_criterion("nombre", lambda x: x["nombre"])
jedis.add_criterion("especie", lambda x: x["especie"])

# a. listado ordenado por nombre y por especie
print("a) Ordenados por nombre:")
jedis.sort_by_criterion("nombre")
jedis.show()

print("\na) Ordenados por especie:")
jedis.sort_by_criterion("especie")
jedis.show()

# b. información de Ahsoka Tano y Kit Fisto
print("\nb) Info de Ahsoka Tano y Kit Fisto:")
for j in jedis:
    if j["nombre"] in ("Ahsoka Tano", "Kit Fisto"):
        print("   -", j)

# c. mostrar todos los padawan de Yoda y Luke Skywalker
print("\nc) Padawans de Yoda y Luke Skywalker:")
padawans_yoda = [j["nombre"] for j in jedis if "Yoda" in j["maestros"]]
padawans_luke = [j["nombre"] for j in jedis if "Luke Skywalker" in j["maestros"]]
print("   De Yoda:", padawans_yoda)
print("   De Luke:", padawans_luke)

# d. Jedi de especie humana y twi'lek
print("\nd) Humanos y Twi'lek:")
for j in jedis:
    if j["especie"] in ("humano", "twi'lek"):
        print("   -", j["nombre"])

# e. Jedi que comienzan con A
print("\ne) Nombres que comienzan con A:")
for j in jedis:
    if j["nombre"].startswith("A"):
        print("   -", j["nombre"])

# f. Jedi que usaron sable de más de un color
print("\nf) Más de un color de sable:")
for j in jedis:
    if len(j["colores"]) > 1:
        print("   -", j["nombre"], j["colores"])

# g. Jedi que usaron sable amarillo o violeta
print("\ng) Con sable amarillo o violeta:")
for j in jedis:
    if "amarillo" in j["colores"] or "violeta" in j["colores"]:
        print("   -", j["nombre"], j["colores"])

# h. Padawans de Qui-Gon Jinn y Mace Windu
print("\nh) Padawans de Qui-Gon Jinn y Mace Windu:")
padawans_quigon = [j["nombre"] for j in jedis if "Qui-Gon Jinn" in j["maestros"]]
padawans_mace   = [j["nombre"] for j in jedis if "Mace Windu" in j["maestros"]]
print("   De Qui-Gon Jinn:", padawans_quigon if padawans_quigon else "ninguno")
print("   De Mace Windu :", padawans_mace   if padawans_mace   else "ninguno")
