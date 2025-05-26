from cola import Queue
from stack import Stack


# a) Eliminar todas las notificaciones de Facebook
def eliminar_notificaciones_facebook(cola: Queue):
    n = cola.size()
    for _ in range(n):
        notificacion = cola.attention()
        if notificacion["app"] != "Facebook":
            cola.arrive(notificacion)


# b) Mostrar notificaciones de Twitter que contienen 'Python'
def mostrar_twitter_con_python(cola: Queue):
    n = cola.size()
    for _ in range(n):
        notificacion = cola.attention()
        if notificacion["app"] == "Twitter" and "Python" in notificacion["mensaje"]:
            print(notificacion)
        cola.arrive(notificacion)


# c) Apilar notificaciones entre 11:43 y 15:57 y contarlas
def en_rango(hora: str, inicio: str, fin: str) -> bool:
    return inicio <= hora <= fin

def almacenar_en_pila_rango(cola: Queue, inicio="11:43", fin="15:57") -> int:
    pila = Stack()
    n = cola.size()
    for _ in range(n):
        notificacion = cola.attention()
        if en_rango(notificacion["hora"], inicio, fin):
            pila.push(notificacion)
        cola.arrive(notificacion)
    return pila.size()


# === EJEMPLO DE USO ===
if __name__ == "__main__":
    cola = Queue()
    cola.arrive({"hora": "10:00", "app": "Facebook", "mensaje": "Like en tu foto"})
    cola.arrive({"hora": "12:00", "app": "Twitter", "mensaje": "Python es increíble"})
    cola.arrive({"hora": "13:30", "app": "Instagram", "mensaje": "Nueva historia"})
    cola.arrive({"hora": "14:50", "app": "Twitter", "mensaje": "Aprendé Python ahora"})
    cola.arrive({"hora": "16:00", "app": "Facebook", "mensaje": "Te mencionaron"})

    print("Cola original:")
    cola.show()

    print("\nEliminando notificaciones de Facebook...")
    eliminar_notificaciones_facebook(cola)

    print("\nCola después de eliminar Facebook:")
    cola.show()

    print("\nNotificaciones de Twitter con 'Python':")
    mostrar_twitter_con_python(cola)

    cantidad = almacenar_en_pila_rango(cola)
    print(f"\nCantidad de notificaciones entre 11:43 y 15:57: {cantidad}")

