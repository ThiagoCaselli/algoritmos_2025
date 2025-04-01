def potencia_recursiva(base, exponente):

    #a^b=axa^b-1
   
    if exponente == 0:
        return 1  
    if exponente > 0:
        return base * potencia_recursiva(base, exponente - 1)  
    else:
        return 1 / potencia_recursiva(base, -exponente) 

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Calcular la potencia
resultado = potencia_recursiva(base, exponente)
print(f"{base}^{exponente} = {resultado}")
