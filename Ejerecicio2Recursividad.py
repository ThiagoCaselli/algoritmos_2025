def suma(n):
    if n < 0: 
        return "El numero de debe ser positivo"
    
    suma = 0 
    for i in range(n + 1):
        suma += i 
    return suma 

n = 10
print(f"La suma de los numeros de 0 hasta {n} es: {suma(n)}")    