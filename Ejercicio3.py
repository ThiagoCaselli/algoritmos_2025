def producto_recursivo(a, b):

   # a×b=a+a+a+⋯+a
    if b == 0:
        return 0  
    if b > 0:
        return a + producto_recursivo(a, b - 1)  
    else:
        return -producto_recursivo(a, -b)  

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

resultado = producto_recursivo(num1, num2)
print(f"El producto de {num1} y {num2} es: {resultado}")
