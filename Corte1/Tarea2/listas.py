#/ #################LISTAS####################
#/ ###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#/ #input()
# Imprime la lista llamada my_lista
print(my_lista)
# Imprime el tipo de la variable my_lista
print(type(my_lista))
# Imprime el string que esta en la posicion 2
print(my_lista[2])

# Cuenta la cantidad de elementos de la lista
print("my_lista size: ", len(my_lista))
# Imprime el string que esta en desde el inicio de la lista hasta 2 sin incluirla
print(my_lista[0:2])
# Imprime el string que esta en desde el inicio de la lista hasta 2 sin incluirla
print(my_lista[:2])

# .append Agrega elemento al final de la lista
my_lista.append('Blanco')
# Imprime la lista con el nuevo elemento
print(my_lista)

# .insert inserta el elemento en el indice 3 sin remplazar solo empuja el siguiente elemento y se inserta
my_lista.insert(3, 'Negro')
# Imprime la lista con el nuevo elemento
print(my_lista)

# Extiende la lista con 2 nuevos elementos
my_lista.extend(['Marron', 'Gris'])
# Imprime la lista con los nuevos elementos
print(my_lista)

# .index sirve para saber el indice de el elemento en la lista
print(my_lista.index('Azul'))

#/ #my_lista.remove('Magenta')
# Sirve para remover el elemento de la lista
my_lista.remove('Marron')
# Imprime la lista con sin el elemento removido
print(my_lista)

# Se devuelve el elemento al pocision 8
my_lista.insert(8, 'Marron')
# Imprime la lista con los nuevos elementos
print(my_lista)

# Elimina el ultimo elemento de la lista y el print lo imprime
print(my_lista.pop())
# Mide la cantidad actual de elementos en my_lista
size = len(my_lista)
# Imprime size = y el numero de elementos de la lista
print("size = ", size)
#/ #print(my_lista.pop(size))

# Concatena la lista tres veces consecutivas
my_lista_3 = my_lista * 3
# Imprime la lista nueva
print("my_lista_3: ", my_lista_3)

# Imprime Sort:
print("Sort:")
# Salto de linea
print()
# Ordena alfabeticamente la lista pero no devuelve ningun valor
my_listaSort = my_lista.sort()
# Imprime la lista con la lista modificada
print(my_listaSort)

# Crea una nueva lista
my_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Imprime Ordering my_NumList:
print("Ordering my_NumList: ")
# Ordena los numeros de menor a mayor
my_NumList.sort()
# Imprime la lista con la lista modificada
print(my_NumList)
#/ #OrderedLList = my_NumList.sort()
#/ #print(my_listaSort)

#/ #Ordenando lista de mayor a menor
my_NumList.sort(reverse=True)
print("De menor a mayor: ", my_NumList)


#/ #################TUPLAS####################
#/ ###########################################
#/ # Corresponde a una estructura similar a las listas, la diferencia está
#/ # en que no se pueden modificar una vez creadas, es decir que son inmutables:

#/ #Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
# Genera una copia idéntica pero inmutable (que no se puede modificar)
my_tupla = tuple(my_lista)
# Salto de linea
print()
# Salto de linea
print()
# Imprime my_tuple: y la copia de la lista
print("my_tuple: ", my_tupla)

# Imprime lo que hay en el indice 0
print(my_tupla[0])
# Imprime lo que hay en el indice 2
print(my_tupla[2])


#/ #Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
# Muestra si rojo esta en my_tupla
print('Rojo' in my_tupla)
# Cuenta cuantas veces aparece Rojo e Imprime
print(my_tupla.count('Rojo'))

#/ #Tupla con un solo elemento
# Crea un string, NO una tupla (para tupla unitaria se necesita una coma: 'Blanco',)
my_tupla_unitaria = ('Blanco')
# Imprime el string 'Blanco'
print(my_tupla_unitaria)

#/ #Empaquetado de tupla, tupla sin paréntesis
# Empaqueta varios datos separados por comas en una sola tupla
my_tupla = 'Gaspar', 5, 8, 1999
# Imprime my_tupla
print(my_tupla)

#/ #Desempaquetado de tupla, se guardan los valores en orden de las variables
# Asigna cada elemento de la tupla a una variable individual según su orden
nombre, dia, mes, año = my_tupla
# Imprime nombre
print(nombre)
# Imprime dia
print(dia)
# Imprime mes
print(mes)
# Imprime año
print(año)

# Muestra en consola los valores de las variables intercalados con etiquetas
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#/ #Convertir una tupla en una lista
# Convierte la tupla en una lista mutable y la guarda en my_lista2
my_lista2 = list(my_tupla)
# Imprime la nueva lista con corchetes: ['Gaspar', 5, 8, 1999]
print(my_lista2)