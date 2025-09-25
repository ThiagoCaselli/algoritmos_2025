from typing import Optional, Any
from Parcial.list_ import List


# ---- Datos de ejemplo ----
superheroes = List([
    {"nombre": "Linterna Verde", "anio": 1940, "casa": "DC",
     "bio": "Usa un anillo de poder y un traje verde"},
    {"nombre": "Wolverine", "anio": 1974, "casa": "Marvel",
     "bio": "Mutante con garras de adamantium"},
    {"nombre": "Dr. Strange", "anio": 1963, "casa": "DC",
     "bio": "Hechicero supremo"},
    {"nombre": "Iron Man", "anio": 1963, "casa": "Marvel",
     "bio": "Genio millonario que usa armadura de alta tecnología"},
    {"nombre": "Capitana Marvel", "anio": 1968, "casa": "Marvel",
     "bio": "Poder cósmico"},
    {"nombre": "Mujer Maravilla", "anio": 1941, "casa": "DC",
     "bio": "Guerrera amazona con traje especial"},
    {"nombre": "Flash", "anio": 1940, "casa": "DC",
     "bio": "El hombre más rápido del mundo"},
    {"nombre": "Star-Lord", "anio": 1976, "casa": "Marvel",
     "bio": "Líder de los Guardianes de la Galaxia"},
    {"nombre": "Batman", "anio": 1939, "casa": "DC",
     "bio": "Usa traje de murciélago para combatir el crimen"},
    {"nombre": "Spider-Man", "anio": 1962, "casa": "Marvel",
     "bio": "Héroe con traje rojo y azul"},
])

# Criterios para búsqueda/orden
superheroes.add_criterion("nombre", lambda x: x["nombre"])
superheroes.add_criterion("anio", lambda x: x["anio"])


# a. Eliminar el nodo que contiene la información de Linterna Verde
superheroes.delete_value("Linterna Verde", "nombre")
print("Lista después de eliminar a Linterna Verde:")
superheroes.show()         
print()

# b. Mostrar el año de aparición de Wolverine
for s in superheroes:
    if s["nombre"] == "Wolverine":
        print("b) Año de aparición de Wolverine:", s["anio"])
print()        

# c. Cambiar la casa de Dr. Strange a Marvel
for s in superheroes:
    if s["nombre"] == "Dr. Strange":
        s["casa"] = "Marvel"

print("c)")
superheroes.show()
print()
# d. Mostrar nombre de los superhéroes cuya biografía mencione “traje” o “armadura”
print("d) Con 'traje' o 'armadura':")
for s in superheroes:
    bio_lower = s["bio"].lower()
    if "traje" in bio_lower or "armadura" in bio_lower:
        print("   -", s["nombre"])
print()        


# e. Nombre y casa de superhéroes con fecha de aparición anterior a 1963
print("e) Anterior a 1963:")
for s in superheroes:
    if s["anio"] < 1963:
        print(f"   - {s['nombre']} ({s['casa']})")
print()        


# f. Casa de Capitana Marvel y Mujer Maravilla
for s in superheroes:
    if s["nombre"] in ("Capitana Marvel", "Mujer Maravilla"):
        print(f"f) {s['nombre']} pertenece a {s['casa']}")
print()        

# g. Toda la información de Flash y Star-Lord
print("g) Info de Flash y Star-Lord:")
for s in superheroes:
    if s["nombre"] in ("Flash", "Star-Lord"):
        print("   -", s)
print()        

# h. Listar los superhéroes que comienzan con B, M y S
print("h) Comienzan con B, M o S:")
for s in superheroes:
    if s["nombre"].startswith(("B", "M", "S")):
        print("   -", s["nombre"])
print()        

# i. Determinar cuántos superhéroes hay de cada casa
conteo = {}
for s in superheroes:
    conteo[s["casa"]] = conteo.get(s["casa"], 0) + 1
print("i) Cantidad por casa:", conteo)



