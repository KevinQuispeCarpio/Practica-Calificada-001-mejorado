def convertirEntero_a_Decimal(numero, base):
    valores = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
               8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if (numero < base):
        return valores[numero]
    else:
        return convertirEntero_a_Decimal(numero//base, base) + valores[numero % base]


n = int(input('Ingrese el número: '))
p = int(input('Ingrese la base: '))
print(convertirEntero_a_Decimal(n, p))
