from stack import Stack

#Clase de datos: Personaje del MCU
class PersonajeMCU:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __str__(self):
        return f'{self.nombre} - {self.cantidad_peliculas} películas'


#Funciones solicitadas
def encontrar_posiciones(pila, nombres_busqueda):
    aux = Stack()
    posiciones = {nombre: None for nombre in nombres_busqueda}
    posicion = 1

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.nombre in nombres_busqueda and posiciones[personaje.nombre] is None:
            posiciones[personaje.nombre] = posicion
        aux.push(personaje)
        posicion += 1

    while aux.size() > 0:
        pila.push(aux.pop())

    for nombre in nombres_busqueda:
        if posiciones[nombre] is not None:
            print(f"{nombre} está en la posición {posiciones[nombre]} desde la cima.")
        else:
            print(f"{nombre} no se encuentra en la pila.")


def personajes_con_muchas_peliculas(pila, min_peliculas):
    aux = Stack()
    print(f"Personajes con más de {min_peliculas} películas:")
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.cantidad_peliculas > min_peliculas:
            print(f"{personaje.nombre} - {personaje.cantidad_peliculas} películas")
        aux.push(personaje)

    while aux.size() > 0:
        pila.push(aux.pop())


def buscar_participacion_personaje(pila, nombre_buscado):
    aux = Stack()
    cantidad = 0

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.nombre == nombre_buscado:
            cantidad = personaje.cantidad_peliculas
        aux.push(personaje)

    while aux.size() > 0:
        pila.push(aux.pop())

    print(f"{nombre_buscado} participó en {cantidad} películas.")


def mostrar_por_letras(pila, letras):
    aux = Stack()
    print(f"Personajes cuyos nombres comienzan con {', '.join(letras)}:")
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.nombre[0].upper() in letras:
            print(personaje)
        aux.push(personaje)

    while aux.size() > 0:
        pila.push(aux.pop())


#Bloque de prueba
if __name__ == "__main__":
    pila_personajes = Stack()

    # Cargar personajes en la pila
    pila_personajes.push(PersonajeMCU("Iron Man", 10))
    pila_personajes.push(PersonajeMCU("Capitan America", 9))
    pila_personajes.push(PersonajeMCU("Black Widow", 7))
    pila_personajes.push(PersonajeMCU("Hulk", 6))
    pila_personajes.push(PersonajeMCU("Doctor Strange", 4))
    pila_personajes.push(PersonajeMCU("Groot", 5))
    pila_personajes.push(PersonajeMCU("Rocket Raccoon", 5))
    pila_personajes.push(PersonajeMCU("Gamora", 6))
    pila_personajes.push(PersonajeMCU("Spider-Man", 3))
    pila_personajes.push(PersonajeMCU("Drax", 4))

    print("\n a) Posición de Rocket Raccoon y Groot")
    encontrar_posiciones(pila_personajes, ["Rocket Raccoon", "Groot"])

    print("\n b) Personajes con más de 5 películas")
    personajes_con_muchas_peliculas(pila_personajes, 5)

    print("\n c) ¿Cuántas películas participó Black Widow?")
    buscar_participacion_personaje(pila_personajes, "Black Widow")

    print("\n d) Personajes cuyos nombres comienzan con C, D o G")
    mostrar_por_letras(pila_personajes, ["C", "D", "G"])
