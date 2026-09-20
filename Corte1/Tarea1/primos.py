# Importa la libreria time para realizar mediciones de tiempo de ejecucion
import time

# Registra la hora/tiempo actual del sistema antes de iniciar los bucles
inicio = time.time()

# Bucle principal que evalua cada entero en el rango de 0 a 30
for i in range(0, 31):
    # Reinicia el contador de divisores exactos para el numero 'i'
    conta = 0
    
    # Evalua la divisibilidad de 'i' entre todos los numeros desde 1 hasta 'i'
    for n in range(1, i + 1):
        # Obtiene el residuo de la division entera entre 'i' y 'n'
        residue = i % n
        
        # Si el residuo es 0, significa que 'n' es divisor exacto de 'i'
        if residue == 0:
            # Incrementa el contador de divisores
            conta = conta + 1
            
    # Si un numero tiene exactamente dos divisores (1 y el mismo), es primo
    if conta == 2:
        # Imprime en consola que el numero evaluado es primo
        print(f'{i} es un primo')

# Registra el tiempo final tras completar todas las iteraciones
fin = time.time()

# Imprime la diferencia de tiempo convirtiendo el resultado de segundos a milisegundos
print("t = ", (fin - inicio) * 1000)