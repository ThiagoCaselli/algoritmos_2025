from Parcial.cola import Queue
from stack import Stack


# Función principal para resolver los puntos del enunciado
def procesar_mcu(cola: Queue):
    n = cola.size()
    
    # Variables para almacenar resultados
    personaje_capitana_marvel = None
    superheroes_femeninos = []
    personajes_masculinos = []
    superhero_scott_lang = None
    nombres_con_s = []
    carol_encontrada = None

    for _ in range(n):
        dato = cola.attention()

        personaje = dato["personaje"]
        heroe = dato["superheroe"]
        genero = dato["genero"]

        # a) Capitana Marvel → personaje
        if heroe == "Capitana Marvel":
            personaje_capitana_marvel = personaje

        # b) Superhéroes femeninos
        if genero == "F":
            superheroes_femeninos.append(heroe)

        # c) Personajes masculinos
        if genero == "M":
            personajes_masculinos.append(personaje)

        # d) Superhéroe de Scott Lang
        if personaje == "Scott Lang":
            superhero_scott_lang = heroe

        # e) Nombres que comienzan con S
        if personaje.startswith("S") or heroe.startswith("S"):
            nombres_con_s.append(dato)

        # f) Buscar Carol Danvers
        if personaje == "Carol Danvers":
            carol_encontrada = heroe

        # Reinsertamos en la cola
        cola.arrive(dato)

    # Mostrar resultados
    print("a) Nombre del personaje de la superheroe Capitana Marvel:", personaje_capitana_marvel)
    print("b) Superhéroes femeninos:", superheroes_femeninos)
    print("c) Personajes masculinos:", personajes_masculinos)
    print("d) Superhéroe de Scott Lang:", superhero_scott_lang)
    print("e) Personajes/superhéroes que comienzan con 'S':")
    for item in nombres_con_s:
        print("   ", item)
    print("f) Carol Danvers está en la cola:", "Sí, es " + carol_encontrada if carol_encontrada else "No se encuentra")

# Ejemplo de uso
if __name__ == "__main__":
    cola = Queue()
    cola.arrive({"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
    cola.arrive({"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
    cola.arrive({"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
    cola.arrive({"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
    cola.arrive({"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})
    cola.arrive({"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"})
    cola.arrive({"personaje": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"})
    cola.arrive({"personaje": "Shuri", "superheroe": "Shuri", "genero": "F"})

    procesar_mcu(cola)
