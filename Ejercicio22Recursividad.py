def usar_la_fuerza(mochila, indice=0):
    # Caso base: no quedan objetos
    if indice >= len(mochila):
        return False, indice

    # Caso base: se encuentra el sable de luz
    if mochila[indice].lower() == 'sable de luz':
        return True, indice + 1  

    # Caso recursivo: revisar el siguiente objeto
    return usar_la_fuerza(mochila, indice + 1)

# Vector que representa la mochila del Jedi
mochila = [
    "comida",
    "agua",
    "blaster",
    "sable de luz",
    "mapa",
    "radio"
]

encontro_sable, objetos_revisados = usar_la_fuerza(mochila)

if encontro_sable:
    print(f"Sable de luz encontrado tras sacar {objetos_revisados} objetos.")
else:
    print("No se encontró el sable de luz en la mochila.")
