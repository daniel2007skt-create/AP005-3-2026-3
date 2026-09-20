# Solicita al usuario ingresar un valor por teclado y lo almacena como texto
a = input("Enter a number: ")

# Convierte la entrada de texto 'a' a un numero entero
a = int(a)

# Solicita al usuario ingresar un segundo valor por teclado
b = input("Enter b number: ")

# Convierte la entrada de texto 'b' a un numero decimal (flotante)
b = float(b)

# Realiza la suma de 'a' (entero) y 'b' (flotante), dando como resultado un flotante
c = a + b

# Compara si el valor numerico de 'a' es igual al valor numerico de 'b'
if a == b:
    # Imprime si los valores numericos son iguales
    print("equal")
else:
    # Imprime si los valores numericos son diferentes
    print("Different")

# Muestra en pantalla el tipo de dato de la variable 'a' (<class 'int'>)
print("Type of a is: ", type(a))

# Muestra en pantalla el tipo de dato de la variable 'b' (<class 'float'>)
print("Type of b is: ", type(b))

# Imprime el resultado almacenado en la variable 'c'
print("c = ", c)

# Compara si el tipo de dato de 'a' es exactamente igual al tipo de dato de 'b'
if type(a) == type(b):
    # Imprime si ambas variables comparten el mismo tipo de dato
    print("a and b are of the same type")
else:
    # Imprime si las variables son de tipos de datos distintos
    print("a and b are of different type")