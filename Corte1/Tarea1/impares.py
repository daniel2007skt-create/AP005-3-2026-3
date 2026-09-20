#/ for i in range (1,21):
#/     residual = i%2
#/     if residual == 0:
#/         print(f'{i} is even')
#/     else:
#/         #print(f'{i} is odd')
#/         print(str(i) + ' is odd')

#/ for i in range (0,6):
#/     result = i**3
#/     print(result)

# Solicita al usuario ingresar el numero de repeticiones mediante entrada de texto
times = input("Enter a number of times: ")

# Convierte primero la entrada de texto a un numero de tipo flotante (decimal)
times = float(times)

# Convierte el valor flotante a un numero entero cortando la parte decimal
times = int(times)

# Muestra en consola el tipo de dato de la variable times (class 'int')
print(type(times))

# Imprime el valor numerico entero almacenado en la variable times
print(times)

# Evalua si el valor ingresado es igual a 0
if times == 0:
    # Si es 0, imprime un mensaje indicando que no se realizara ninguna accion
    print("Don't do anything")
else:
    # Si es mayor a 0, ejecuta un bucle for que itera desde 1 hasta times (inclusive)
    for i in range(1, times + 1):
        # Imprime el valor actual del contador de la iteracion
        print("i = ", i)