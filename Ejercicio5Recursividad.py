def romano_a_decimal(romano):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Caso base: si la cadena está vacía, el valor es 0
    if not romano:
        return 0

    # Caso base: si la cadena tiene un solo carácter
    if len(romano) == 1:
        return valores[romano]

    # Si el valor del primer símbolo es menor que el del siguiente, se resta
    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + romano_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
    
#Ejemplos     
print(romano_a_decimal("III"))     # 3
print(romano_a_decimal("IX"))      # 9
print(romano_a_decimal("LVIII"))   # 58
print(romano_a_decimal("MCMXCIV")) # 1994 
