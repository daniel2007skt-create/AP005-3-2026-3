#/ ### Define un diccionario de habitaciones y sus temperaturas
#/ # sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
#/ ### Define un diccionario de zonas y su número de cámaras
#/ # num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

#/ ### Imprime el diccionario de sensores
#/ # print(sensors)
#/ ### Imprime el diccionario de cámaras
#/ # print(num_cameras)
#/ ### Define un diccionario de traducciones de palabras
#/ # translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
#/ ### Imprime el diccionario de traducciones
#/ # print(translations)

#/ ##Verifiying an error:
#/ ### Intenta usar listas como claves, lo cual genera un error porque las listas son mutables
#/ # powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
#/ ### Imprime la variable con error (comentado)
#/ # # print(powers)

#/ ### Define un diccionario donde las claves tienen como valor una lista
#/ # children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
#/ ### Imprime el diccionario con listas de nombres como valores
#/ # print(children)

#/ ### Crea un diccionario vacío sin elementos
#/ # my_empty_dictionary = {}
#/ ### Imprime el diccionario vacío
#/ # print(my_empty_dictionary)

#/ ### Define un diccionario de alimentos y sus precios
#/ # menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#/ ### Imprime el menú original antes de ser modificado
#/ # print("Before: ", menu)
#/ ### Agrega una nueva clave "cheesecake" con el valor 8 al diccionario
#/ # menu["cheesecake"] = 8
#/ ### Imprime el menú actualizado con el nuevo alimento
#/ # print("After", menu)
#/ ### Crea un diccionario inicial asignado a la variable
#/ # animals_in_zoo = {"dinosaurs": 0}
#/ ### Reasigna exactamente el mismo diccionario a la misma variable
#/ # animals_in_zoo = {"dinosaurs": 0}
#/ ### Sobrescribe toda la variable con un nuevo diccionario que contiene únicamente "horses"
#/ # animals_in_zoo = {"horses": 2}
#/ ### Imprime el último diccionario asignado a la variable
#/ # print(animals_in_zoo)


#/ ##Add multiple keys
#/ ### Define un diccionario de sensores con tres habitaciones
#/ # sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
#/ ### Imprime el diccionario inicial de sensores
#/ # print("Before", sensors)

#/ #If we wanted to add 3 new rooms, we could use:
#/ ### Agrega múltiples pares clave-valor al diccionario existente usando .update()
#/ # sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
#/ ### Imprime el diccionario de sensores actualizado con las nuevas habitaciones
#/ # print("After", sensors)

#/ ###
#/ ### Define un diccionario de nombres de usuario e identificadores
#/ # user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
#/ ### Imprime el diccionario de usuarios inicial
#/ # print(user_ids)
#/ ### Agrega dos nuevos usuarios con sus IDs usando .update()
#/ # user_ids.update({"theLooper": 138475, "stringQueen": 85739})
#/ ### Imprime el diccionario con los cuatro usuarios
#/ # print(user_ids)

#/ ## Overwrite Values ##
#/ #We know that we can add a key by using the following syntax:
#/ #menu["banana"] = 3
#/ ### Define el diccionario de menú inicial
#/ # menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#/ ### Imprime el menú original
#/ # print("Before: ", menu)
#/ ### Modifica el valor de la clave "oatmeal" existente cambiándolo de 3 a 5
#/ # menu["oatmeal"] = 5
#/ ### Imprime el menú con el valor actualizado
#/ # print("After", menu)

#/ ## Notice the value of "oatmeal" has now changed to 5.
#/ ### Define un diccionario de categorías y ganadores del Oscar
#/ # oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
#/ ### Imprime los ganadores originales
#/ # print("Before", oscar_winners)
#/ ### Imprime una línea en blanco
#/ # print()
#/ ### Agrega una nueva categoría que no existía en el diccionario
#/ # oscar_winners.update({"Supporting Actress": "Viola Davis"})
#/ ### Imprime el diccionario con la nueva categoría agregada
#/ # print("After1", oscar_winners)
#/ ### Imprime una línea en blanco
#/ # print()
#/ ### Modifica la clave "Best Picture" reemplazando "La La Land" por "Moonlight"
#/ # oscar_winners["Best Picture"] = "Moonlight"
#/ ### Imprime el diccionario con el ganador de mejor película corregido
#/ # print("After2", oscar_winners)


#/ ###Dict Comprehensions
#/ #Let’s say we have two lists that we want to combine into a 
#/ #dictionary, like a list of students and a list of their heights, 
#/ #in inches:

# Crea una lista con cuatro nombres de estudiantes
names = ['Jenny', 'Alexus', 'Sam', 'Grace']

# Crea una lista con cuatro estaturas correspondientes a los estudiantes
heights = [61, 70, 67, 64]

#/ #Python allows you to create a dictionary using 
#/ # a dict comprehension, with this syntax:

#/ ### Empareja los elementos de la lista de nombres y estaturas en tuplas
#/ # zipStudents = zip(names, heights)
#/ ### Imprime la referencia en memoria del objeto zip generado
#/ # print("zipStudents: ", zipStudents)

#/ ### Genera un diccionario mediante comprensión emparejando cada nombre con su estatura
#/ # students = {key:value for key, value in zip(names, heights)}
#/ # #students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
#/ ### Imprime el diccionario de estudiantes generado por la comprensión
#/ # print(students)

#/ # #zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:

#/ ### Crea una lista con nombres de bebidas
#/ # drinks = ["espresso", "chai", "decaf", "drip"]
#/ ### Crea una lista con los miligramos de cafeína correspondientes a cada bebida
#/ # caffeine = [64, 40, 0, 120]

#/ ### Empareja la lista de bebidas con la lista de contenido de cafeína
#/ # zipped_drinks = zip(drinks, caffeine)
#/ ### Imprime la referencia en memoria del iterador zip
#/ # print(zipped_drinks)

#/ ### Crea un diccionario asociando cada bebida con su nivel de cafeína usando comprensión
#/ # drinks_to_caffeine = {key:value for key, value in zipped_drinks}
#/ ### Imprime el diccionario de bebidas y su cafeína
#/ # print(drinks_to_caffeine)

# Crea una lista con títulos de canciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]

# Crea una lista con el número de reproducciones de cada canción
playcounts = [78, 29, 44, 21, 89, 5]

# Crea un diccionario mediante comprensión vinculando cada canción con sus reproducciones
plays = {key: value for key, value in zip(songs, playcounts)}

# Imprime el diccionario de reproducciones generado
print(plays)

# Agrega una nueva canción "Purple Haze" con 1 reproducción al diccionario usando .update()
plays.update({"Purple Haze": 1})

# Modifica las reproducciones de la canción "Respect" cambiándolas de 89 a 94 usando .update()
plays.update({"Respect": 94})

# Imprime el diccionario de reproducciones actualizado
print("After: ", plays)

# Crea un diccionario que contiene el diccionario 'plays' y otro diccionario vacío como valores
library = {"The Best Songs": plays, "Sunday Feelings": {}}

# Imprime el diccionario final de la biblioteca de música
print(library)