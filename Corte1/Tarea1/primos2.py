# Inicializa la variable de control para mantener activo el bucle while
a = 1

# Solicita al usuario ingresar un valor limite inicial
value = input('Ingrese un valor')

# Convierte el valor ingresado por teclado de texto a numero entero
value = int(value)

# Bucle principal que se ejecuta mientras la variable 'a' sea igual a 1
while a == 1:
    # Recorre cada entero desde 1 hasta el valor limite ingresado (inclusive)
    for i in range(1, value + 1):
        # Reinicia el contador de divisores exactos para el numero 'i'
        conta = 0
        
        # Prueba la divisibilidad de 'i' entre todos los numeros desde 1 hasta 'i'
        for n in range(1, i + 1):
            # Calcula el residuo de la division entre 'i' y 'n'
            residue = i % n
            
            # Si el residuo es cero, se encontró un divisor exacto
            if residue == 0:
                # Incrementa el contador de divisores exactos
                conta = conta + 1
            
            #/ print("i = ", i)
            #/ print("n = ", n)
            #/ print("residue = ", residue)
            #/ print("conta = ", conta)
            
    # Evaluacion fuera del bucle 'for': se verifica si el ultimo valor de 'i' tuvo solo 2 divisores
    if conta == 2:
        # Imprime si el numero evaluado es primo
        print(f'{i} es un primo')
        print("\n")
    else:
        # Imprime si el numero evaluado no es primo
        print(f'{i} NOOO es un primo')
        print("\n")

    # Pregunta al usuario si desea realizar otra iteracion del programa
    print('Do you want to continue?. Press 1 to do that')
    
    # Lee la respuesta ingresada por teclado
    a = input()
    
    # Convierte la respuesta a entero
    a = int(a)

    # Si la respuesta es distinta de 1, interrumpe la ejecucion del bucle while
    if a != 1:
        break

    # Solicita un nuevo numero limite para la siguiente iteracion del bucle
    value = input('Ingrese un valor')
    
    # Convierte el nuevo limite ingresado a entero
    value = int(value)