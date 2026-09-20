# Importa el modulo random para la generacion de numeros aleatorios
import random

# Importa la libreria pyplot de matplotlib para la creacion de graficos
from matplotlib import pyplot as plt

#/ Add your code below:
# Genera una secuencia de numeros enteros desde 1 hasta 12
numbers_a = range(1, 13)

# Crea una lista de 12 numeros enteros aleatorios elegidos entre 1 y 1000
numbers_b = [random.randint(1, 1000) for i in range(12)]

# Traza la grafica de linea utilizando numbers_a como eje X y numbers_b como eje Y
plt.plot(numbers_a, numbers_b)

# Muestra la ventana con la grafica generada en pantalla
plt.show()