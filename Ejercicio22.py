def usar_la_fuerza(mochila, contador=0):

    # Caso base: mochila vacía
    if not mochila:
        print("La mochila está vacía. No se encontró el Sable de luz.")
        return False, contador

    objeto = mochila[0]
    print(f"Usando la fuerza... Qui-Gon sacó: {objeto}")

    # Si encuentra el sable de luz
    if objeto == "Sable de luz":
        print("Qui-Gon encontró el Sable de luz")
        return True, contador + 1

    # Llamada recursiva con el resto de la mochila
    return usar_la_fuerza(mochila[1:], contador + 1)


mochila = ["Comunicador", "Comida", "Botiquín", "Sable de luz", "Blaster", "Linterna"]

encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
    print(f"Qui-Gon encontró el Sable de luz tras sacar {objetos_sacados} objetos.")
else:
    print("Qui-Gon no encontró el sable de luz.")

