# Recorre todos los numeros enteros en el rango desde 100 hasta 300 (inclusive)
for i in range(100, 301):
    # Evalua si el numero actual 'i' NO es divisible exactamente entre 12
    if (i % 12) != 0:
        # Omite el resto del codigo del bucle y pasa al siguiente numero
        continue
    # Imprime los numeros que si son divisibles entre 12
    print(i)