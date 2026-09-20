# Importa el modulo time para manejar pausas en la ejecucion
import time

# Define la cadena de texto a recorrer
cadena = 'Python'

# Bucle for que itera a traves de cada caracter de la cadena
for letra in cadena:
    # Evalua si el caracter actual es la letra 't'
    if letra == 't':
        # Salta la iteracion actual y avanza directamente al siguiente caracter
        continue
    # Imprime la letra actual si no fue omitida por la sentencia continue
    print(letra)
    # Pausa la ejecucion del programa durante 1 segundo antes de la siguiente iteracion
    time.sleep(1)