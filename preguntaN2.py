# Implemente un rograma para convertir un número decimal a hexadecimal
def convertirDecimal_a_Hexadecimal(numero):
    valores = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
               8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if (numero < 16):
        return valores[numero]
    else:
        return convertirDecimal_a_Hexadecimal(numero//16)+valores[numero % 16]


numero = int(input('Ingrese el número que desea convertir: '))
print("Si convertimos el", numero, "a Hexadecimal seria:",
      convertirDecimal_a_Hexadecimal(numero))  # Si le damos el valor a número de 8642 nos da como resultado 21c2
print('________________________________________________________________________________')
print("Si resolvemos el ejemplo brindado del numero 8642 nos da:",
      convertirDecimal_a_Hexadecimal(8642))
