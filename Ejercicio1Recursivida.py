def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1 
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 5
print(f"El valor de la sucesion de fibonacci del numero {n} es: {fibonacci(n)}")