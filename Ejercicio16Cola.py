from heapp import HeapMax
from heapp import HeapMin


# Inicializamos la cola de impresión como un HeapMax
cola_impresion = HeapMax()

# a. cargue tres documentos de empleados
print("a. Cargando 3 documentos de empleados (Prioridad 1)")
cola_impresion.arrive("Doc_Empleado_A", 1)
cola_impresion.arrive("Doc_Empleado_B", 1)
cola_impresion.arrive("Doc_Empleado_C", 1)
print(f"Estado de la cola (Prioridad, Documento): {cola_impresion.elements}") # Muestra los elementos en el arreglo interno del heap
print()

# b. imprima el primer documento de la cola
print("b. Imprimiendo el primer documento de la cola (más alta prioridad)")
documento_impreso = cola_impresion.attention()
if documento_impreso:
    print(f"Documento impreso: {documento_impreso[1]} (Prioridad: {documento_impreso[0]})")
print(f"Estado actual de la cola: {cola_impresion.elements}")
print()

# c. cargue dos documentos del staff de TI
print("c. Cargando 2 documentos de Staff de TI (Prioridad 2)")
cola_impresion.arrive("Doc_TI_X", 2)
cola_impresion.arrive("Doc_TI_Y", 2)
print(f"Estado de la cola: {cola_impresion.elements}")
print()

# d. cargue un documento del gerente
print("d. Cargando 1 documento de Gerente (Prioridad 3)")
cola_impresion.arrive("Doc_Gerente_1", 3)
print(f"Estado de la cola: {cola_impresion.elements}")
print()

# e. imprima los dos primeros documentos de la cola.
print("e. Imprimiendo los dos primeros documentos de la cola")
for i in range(2):
    documento_impreso = cola_impresion.attention()
    if documento_impreso:
        print(f"Documento impreso {i+1}: {documento_impreso[1]} (Prioridad: {documento_impreso[0]})")
    else:
        print("La cola está vacía.")
        break
print(f"Estado actual de la cola: {cola_impresion.elements}")
print()

# f. cargue dos documentos de empleados y uno de gerente.
print("f. Cargando 2 documentos de Empleados (P1) y 1 de Gerente (P3)")
cola_impresion.arrive("Doc_Empleado_D", 1)
cola_impresion.arrive("Doc_Empleado_E", 1)
cola_impresion.arrive("Doc_Gerente_2", 3)
print(f"Estado de la cola: {cola_impresion.elements}")
print()

# g. imprima todos los documentos de la cola de impresión.
print("g. Imprimiendo todos los documentos restantes de la cola")
i = 1
while cola_impresion.size() > 0:
    documento_impreso = cola_impresion.attention()
    print(f"Documento impreso {i}: {documento_impreso[1]} (Prioridad: {documento_impreso[0]})")
    i += 1
print(f"Estado final de la cola: {cola_impresion.elements}")