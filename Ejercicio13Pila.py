from stack import Stack

#Clase de datos
class TrajeIronMan:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f'{self.modelo} - {self.pelicula} - {self.estado}'


#Funciones que operan sobre la pila de trajes
def buscar_mark_xliv(pila):
    aux = Stack()
    peliculas = []

    while pila.size() > 0:
        traje = pila.pop()
        if traje.modelo == "Mark XLIV":
            peliculas.append(traje.pelicula)
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

    if peliculas:
        print("El modelo Mark XLIV fue usado en:")
        for peli in peliculas:
            print("-", peli)
    else:
        print("No se usó el modelo Mark XLIV.")


def mostrar_danados(pila):
    aux = Stack()
    print("Modelos dañados:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje.estado == "Dañado":
            print(traje)
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())


def eliminar_destruidos(pila):
    aux = Stack()
    print("Eliminando modelos destruidos:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje.estado == "Destruido":
            print(traje.modelo)
        else:
            aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())


def agregar_modelo(pila, nuevo_traje):
    aux = Stack()
    repetido = False

    while pila.size() > 0:
        traje = pila.pop()
        if traje.modelo == nuevo_traje.modelo and traje.pelicula == nuevo_traje.pelicula:
            repetido = True
        aux.push(traje)

    if not repetido:
        aux.push(nuevo_traje)

    while aux.size() > 0:
        pila.push(aux.pop())


def mostrar_por_pelicula(pila, peliculas_objetivo):
    aux = Stack()
    print("Trajes utilizados en películas seleccionadas:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje.pelicula in peliculas_objetivo:
            print(traje.modelo)
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())


#Bloque principal de prueba
if __name__ == "__main__":
    pila_trajes = Stack()
    pila_trajes.push(TrajeIronMan("Mark XLIV", "Avengers: Age of Ultron", "Dañado"))
    pila_trajes.push(TrajeIronMan("Mark L", "Avengers: Infinity War", "Destruido"))
    pila_trajes.push(TrajeIronMan("Mark XLIV", "Iron Man 3", "Impecable"))
    pila_trajes.push(TrajeIronMan("Mark XL", "Iron Man 3", "Dañado"))
    pila_trajes.push(TrajeIronMan("Mark LXXXV", "Avengers: Endgame", "Impecable"))

    buscar_mark_xliv(pila_trajes)
    mostrar_danados(pila_trajes)
    eliminar_destruidos(pila_trajes)
    agregar_modelo(pila_trajes, TrajeIronMan("Mark LXXXV", "Avengers: Endgame", "Impecable"))  
    mostrar_por_pelicula(pila_trajes, ["Spider-Man: Homecoming", "Capitan America: Civil War"])
