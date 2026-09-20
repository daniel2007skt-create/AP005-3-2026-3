# ==============================================================================
# DICCIONARIOS EN PYTHON: OPERACIONES FUNDAMENTALES Y MÉTODOS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ACCESO DIRECTO A VALORES MEDIANTE CLAVES (Get a Key)
# ------------------------------------------------------------------------------

# Define un diccionario donde la clave es el rascacielos y el valor su altura en metros
building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3,
}

# Accede directamente al valor de la clave 'Burj Khalifa' e imprime 828
print(building_heights["Burj Khalifa"])

# Accede directamente al valor de la clave 'Ping An' e imprime 599
print(building_heights["Ping An"])

# Define un diccionario cuyas claves son elementos y sus valores son listas de signos
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"],
}

# Accede a la lista asociada a la clave 'earth' e imprime la lista completa
print(zodiac_elements["earth"])

# Accede a la lista asociada a la clave 'fire' e imprime la lista completa
print(zodiac_elements["fire"])


# ------------------------------------------------------------------------------
# 2. VALIDACIÓN DE CLAVES PARA EVITAR ERRORES (Get an Invalid Key)
# ------------------------------------------------------------------------------

# NOTA: Acceder a una clave que no existe (ej. building_heights["Landmark 81"])
# generaría un error de tipo KeyError y detendría la ejecución.

# Variable con la clave que queremos verificar antes de acceder
key_to_check = "Landmark 81"

# El operador 'in' verifica si la clave existe en el diccionario antes de consultar
if key_to_check in building_heights:
    # Esta línea solo se ejecuta si la clave está presente
    print(building_heights["Landmark 81"])

# Asigna o crea una nueva clave 'energy' con su valor en el diccionario
zodiac_elements["energy"] = "Not a Zodiac element"

# Comprueba si la clave 'energy' fue agregada correctamente
if "energy" in zodiac_elements:
    # Imprime "Not a Zodiac element"
    print(zodiac_elements["energy"])


# ------------------------------------------------------------------------------
# 3. ACCESO SEGURO A CLAVES CON EL MÉTODO .get() (Safely Get a Key)
# ------------------------------------------------------------------------------

# .get() busca la clave: si existe devuelve su valor (632), si no existe devuelve None sin fallar
building_heights.get("Shanghai Tower")

# Al no existir la clave 'My House', .get() retorna None de forma segura
building_heights.get("My House")

# Diccionario que mapea nombres de usuario con sus IDs numéricos
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384,
}

# Consulta de forma segura el ID de 'teraCoder'
user_ids.get("teraCoder")

# Estructura condicional para validar la existencia de la clave y asignar un valor por defecto
if user_ids.get("teraCoder") == None:
    # Si la clave diera None, asignaría este valor predeterminado
    tc_id = 1000
else:
    # Como 'teraCoder' existe, asigna su valor real (100019)
    tc_id = user_ids.get("teraCoder")

# Imprime 100019
print(tc_id)

# Valida si un usuario no registrado devuelve None
if user_ids.get("superStackSmash") == None:
    # Como la clave no existe, entra al bloque y asigna el ID por defecto 100000
    stack_id = 100000

# Imprime 100000
print(stack_id)


# ------------------------------------------------------------------------------
# 4. EXTRACCIÓN Y ELIMINACIÓN DE CLAVES CON .pop() (Delete a Key)
# ------------------------------------------------------------------------------

# Diccionario que asocia números de boleto con premios de rifa
raffle = {
    223842: "Teddy Bear",
    872921: "Concert Tickets",
    320291: "Gift Basket",
    412123: "Necklace",
    298787: "Pasta Maker",
}

# .pop(clave, valor_defecto) remueve la clave del diccionario y retorna su valor ("Gift Basket")
print(raffle.pop(320291, "No Prize"))

# Muestra el diccionario actualizado (ya no contiene el boleto 320291)
print(raffle)

# Al buscar el boleto 100000 que no existe, .pop() devuelve el valor por defecto "No Prize"
print(raffle.pop(100000, "No Prize"))

# Confirma que el diccionario no sufrió modificaciones tras el intento fallido
print(raffle)

# Remueve la clave 872921 y retorna "Concert Tickets"
print(raffle.pop(872921, "No Prize"))

# Imprime el diccionario resultante tras la segunda eliminación
print(raffle)

# Ejemplo práctico: uso de .pop() para consumir ítems de un inventario
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30,
}

# Inicializa los puntos de vida base
health_points = 20

# Extrae 'stamina grains' (15 pts), lo borra del inventario y lo suma a la vida
health_points += available_items.pop("stamina grains", 0)

# Extrae 'power stew' (30 pts), lo borra del inventario y lo suma a la vida
health_points += available_items.pop("power stew", 0)

# Intenta extraer 'mystic bread'; como no existe, devuelve 0 y no altera la vida
health_points += available_items.pop("mystic bread", 0)

# Muestra el inventario actualizado sin los ítems consumidos
print(available_items)

# Imprime el total de puntos acumulados (20 + 15 + 30 = 65)
print(health_points)


# ------------------------------------------------------------------------------
# 5. OBTENER TODAS LAS CLAVES CON .keys() (Get All Keys)
# ------------------------------------------------------------------------------

# Diccionario con estudiantes y sus listas de calificaciones
test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75],
}

# Convierte las claves del diccionario en una lista de Python e imprime los nombres
print(list(test_scores))

# Bucle for que itera explícitamente sobre cada clave obtenida con .keys()
for student in test_scores.keys():
    # Imprime el nombre de cada estudiante en una línea diferente
    print(student)

# Diccionario con temas de programación y cantidad de ejercicios
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18,
}

# Guarda la vista iterable de las claves del diccionario de usuarios
users = user_ids.keys()

# Guarda la vista iterable de las claves del diccionario de lecciones
lessons = num_exercises.keys()

# Imprime el objeto dict_keys con las claves de usuarios
print(users)

# Imprime el objeto dict_keys con las claves de lecciones
print(lessons)


# ------------------------------------------------------------------------------
# 6. OBTENER TODOS LOS VALORES CON .values() (Get All Values)
# ------------------------------------------------------------------------------

# Recorre únicamente los valores (listas de notas) ignorando los nombres de los alumnos
for score_list in test_scores.values():
    # Imprime cada lista de notas individualmente
    print(score_list)

# Acumulador para calcular la suma total de ejercicios
total_exercises = 0

# Recorre directamente los números almacenados como valores en el diccionario
for exercises in num_exercises.values():
    # Suma la cantidad de ejercicios de la lección actual al total
    total_exercises += exercises

# Imprime el total de ejercicios del curso (115)
print(total_exercises)


# ------------------------------------------------------------------------------
# 7. OBTENER CLAVE Y VALOR SIMULTÁNEAMENTE CON .items() (Get All Items)
# ------------------------------------------------------------------------------

# Diccionario de marcas y su valoración en miles de millones de dólares
biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8,
}

# .items() descompone cada elemento en una tupla (clave, valor) en cada iteración
for company, value in biggest_brands.items():
    # Imprime una cadena formateada concatenando el nombre y el valor financiero
    print(company + " has a value of " + str(value) + " billion dollars. ")

# Diccionario con estadísticas de participación laboral femenina por sector
pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9,
}

# Desempaqueta la profesión en 'occupation' y el porcentaje numérico en 'percentage'
for occupation, percentage in pct_women_in_occupation.items():
    # Imprime la frase formateada con los datos desempaquetados
    print(
        "Women make up "
        + str(percentage)
        + " percent of "
        + occupation
        + "s."
    )