# Importa la libreria time para realizar mediciones del tiempo de ejecucion
import time

# Registra la marca de tiempo inicial del sistema antes de comenzar el bucle
inicio = time.time()

# Recorre los numeros enteros en el rango de 1 a 30 (inclusive)
for i in range(1, 31):
    # Reinicia el contador de divisores exactos para el numero actual
    conta = 0
    
    # Evalua divisibilidad probando desde 1 hasta 'i'
    for n in range(1, i + 1):
        # Calcula el residuo de la division entre 'i' y 'n'
        residue = i % n
        
        # Si el residuo es cero, se confirma un divisor exacto
        if residue == 0:
            # Incrementa el contador de divisores
            conta = conta + 1
            
    # Si un numero tiene exactamente 2 divisores (1 y si mismo), se considera primo
    if conta == 2:
        # Imprime el numero identificado como primo
        print(f'{i} es un primo')
        # Imprime un salto de linea adicional
        print("\n")

# Registra la marca de tiempo final tras completar todas las iteraciones
fin = time.time()

# Calcula la diferencia de tiempo y la imprime convertida a milisegundos
print("t = ", (fin - inicio) * 1000)