# Bucle infinito para solicitar entradas continuamente hasta que el usuario decida detener el programa
while True:

    # Solicita al usuario un numero por teclado y lo convierte directamente a entero
    value = int(input("Enter a positive integer value: "))
    
    # Imprime el valor ingresado por el usuario
    print("Value: ", value)
    
    # Comprueba si la variable 'value' es de tipo entero y almacena el resultado booleano en 'a'
    a = isinstance(value, int)
    
    # Evalua si 'value' es un entero y ademas es un numero estrictamente mayor a 0
    if a == True and value > 0:
        # Inicializa el acumulador para el calculo del factorial en 1
        fact = 1
        
        # Bucle for que itera desde 1 hasta 'value' (inclusive)
        for i in range (1, value + 1):
            # Multiplica el acumulador acumulado por el numero 'i' de la iteracion actual
            fact = fact * i            
            
        # Imprime el resultado del factorial calculado
        print(f'The factorial of {value} is: ', fact)
    else:
        # Imprime un mensaje de advertencia si el numero no es entero positivo
        print("Please, enter a positive integer number")