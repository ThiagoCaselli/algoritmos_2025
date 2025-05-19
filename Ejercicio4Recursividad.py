def potencia(base, exponente):

    if exponente == 0:         
        return 1
    elif exponente > 0: 
        return base * potencia(base, exponente - 1)
    else:
        return 1 / potencia(base, -exponente)
    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)

print (f"{base} elevado a la {exponente} es: {resultado}")