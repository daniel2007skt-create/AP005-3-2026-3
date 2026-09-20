#/ 9) Imprimir los números primos existentes entre 0 y 30
# Define el límite superior del rango de búsqueda de primos
tope_rango = 30

# Inicializa el contador del número a evaluar
n = 0

# Bandera para determinar si el número actual es primo
primo = True

# Bucle principal que evalúa cada número desde 0 hasta el límite superior
while (n < tope_rango):
    # Recorre divisores potenciales desde 2 hasta n - 1
    for div in range(2, n):
        # Si el número es divisible exactamente, no es primo
        if (n % div == 0):
            primo = False

    # Si conserva el valor True, imprime el número primo
    if (primo):
        print(n)
    else:
        # Reestablece la bandera para el siguiente número
        primo = True

    # Incrementa el número a evaluar
    n += 1


#/ 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
# Reinicia el contador del número a evaluar
n = 0

# Bandera para indicar si un número es primo
primo = True

# Bucle principal para evaluar números hasta tope_rango
while (n < tope_rango):
    # Prueba los divisores posibles para el número actual
    for div in range(2, n):
        # Si se encuentra un divisor exacto, se confirma que no es primo
        if (n % div == 0):
            primo = False
            # Rompe el bucle for de forma anticipada para evitar iteraciones innecesarias
            break

    # Imprime el número si no tuvo divisores
    if (primo):
        print(n)
    else:
        # Restablece la variable para la siguiente iteración
        primo = True

    # Avanza al siguiente número del rango
    n += 1


#/ 11) En los puntos 9 y 10, se diseñó un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
# Contador para registrar las iteraciones sin usar break
ciclos_sin_break = 0

# Reinicia la variable de control del número a evaluar
n = 0

# Estado inicial de la bandera de verificación
primo = True

# Bucle para medir iteraciones sin optimización
while (n < tope_rango):
    # Comprueba la divisibilidad recorriendo todo el rango sin detenerse
    for div in range(2, n):
        # Incrementa el contador de ciclos ejecutados
        ciclos_sin_break += 1

        # Evalúa si la división es exacta
        if (n % div == 0):
            primo = False

    # Muestra el número si la bandera continúa en True
    if (primo):
        print(n)
    else:
        # Restablece la bandera para la siguiente iteración
        primo = True

    # Pasa al siguiente entero
    n += 1

# Imprime el acumulado total de iteraciones sin interrupción
print('Cantidad de ciclos: ' + str(ciclos_sin_break))


# Contador para registrar las iteraciones utilizando la sentencia break
ciclos_con_break = 0

# Reinicia la variable de control del número
n = 0

# Estado inicial de la bandera
primo = True

# Bucle para medir iteraciones con optimización
while (n < tope_rango):
    # Comprueba divisibilidad interrumpiendo al hallar el primer divisor
    for div in range(2, n):
        # Incrementa el contador de ciclos ejecutados
        ciclos_con_break += 1

        # Si se halla un divisor, detiene la búsqueda inmediatamente
        if (n % div == 0):
            primo = False
            break

    # Imprime el entero si es primo
    if (primo):
        print(n)
    else:
        # Restablece la bandera
        primo = True

    # Pasa al siguiente entero
    n += 1

# Imprime el total de iteraciones optimizadas
print('Cantidad de ciclos: ' + str(ciclos_con_break))

# Muestra el porcentaje de iteraciones ejecutadas en comparación con el proceso sin break
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')


#/ 12) Si la cantidad de números que se evalúa es mayor a treinta, ¿esa optimización crece?
# Incrementa el límite superior del rango de números a evaluar
tope_rango = 100

# Inicializa el contador de ciclos sin optimización para el nuevo rango
ciclos_sin_break = 0

# Reinicia el entero a evaluar
n = 0

# Estado inicial de la bandera
primo = True

# Bucle para medir el rendimiento no optimizado hasta 100
while (n < tope_rango):
    # Evalúa divisibilidad recorriendo todos los valores hasta n - 1
    for div in range(2, n):
        # Suma una iteración al contador
        ciclos_sin_break += 1

        # Verifica el residuo de la división
        if (n % div == 0):
            primo = False

    # Muestra el valor si es primo
    if (primo):
        print(n)
    else:
        # Restablece la bandera de prueba
        primo = True

    # Siguiente número
    n += 1

# Muestra el total de iteraciones del método ineficiente
print('Cantidad de ciclos: ' + str(ciclos_sin_break))


# Inicializa el contador de ciclos optimizado para el nuevo rango
ciclos_con_break = 0

# Reinicia el entero a evaluar
n = 0

# Estado inicial de la bandera
primo = True

# Bucle para medir el rendimiento optimizado hasta 100
while (n < tope_rango):
    # Evalúa divisibilidad interrumpiendo el flujo con break
    for div in range(2, n):
        # Suma una iteración al contador
        ciclos_con_break += 1

        # Interrumpe la iteración tras encontrar cualquier divisor
        if (n % div == 0):
            primo = False
            break

    # Muestra el número primo encontrado
    if (primo):
        print(n)
    else:
        # Restablece la bandera
        primo = True

    # Siguiente número
    n += 1

# Muestra el total de iteraciones con break
print('Cantidad de ciclos: ' + str(ciclos_con_break))

# Muestra el porcentaje resultante para confirmar el incremento en la eficiencia
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')