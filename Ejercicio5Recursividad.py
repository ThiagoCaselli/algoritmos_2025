def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    anterior = 0

    for letra in reversed(romano.upper()):
        valor = valores.get(letra, 0)
        if valor < anterior:
            total -= valor
        else:
            total += valor
            anterior = valor

    return total

# Ejemplos de uso
print(romano_a_decimal("III"))     # 3
print(romano_a_decimal("IX"))      # 9
print(romano_a_decimal("LVIII"))   # 58
print(romano_a_decimal("MCMXCIV")) # 1994
