# Lista de valores de entrada (X) para entrenar el modelo
inputs = [1, 2, 3, 4]

# Lista de valores reales/deseados (Y) que el modelo debe aprender a predecir
targets = [2, 4, 6, 8]

# Peso inicial de la red (parámetro ejecutable/configurable, arranca en 0.1)
w = 0.1

# Tasa de aprendizaje (controla qué tan grandes son los pasos al actualizar el peso)
learning_rate = 0.1

# Definición de la función de predicción (hipótesis lineal: y = w * x)
def predict(i):
  return w*i  # Multiplica la entrada 'i' por el peso actual 'w'

# Bloque de entrenamiento de la red
for _ in range(30):  # Ejecuta 30 épocas (iteraciones de entrenamiento)
  
  # Genera predicciones para todas las entradas usando la comprensión de listas
  pred = [predict(i) for i in inputs]
  
  # Calcula el error de cada muestra restando el valor real (t) menos la predicción (p)
  errors = [t - p for p, t in zip(pred, targets)]
  
  # Calcula el error promedio (costo) sumando los errores y dividiendo entre la cantidad de datos
  cost = sum(errors)/len(targets)
  
  # Imprime la lista de valores reales esperados
  print(f"Targets: ", targets)
  
  # Imprime la lista de predicciones hechas por el modelo en la iteración actual
  print(f"Predictions: ", pred)
  
  # Imprime la lista de errores individuales de cada entrada
  print(f"Errors: ", errors)
  
  # Imprime el valor actual del peso 'w' (con 10 decimales) y el costo promedio (con 6 decimales)
  print(f"Weight: {w: .10f}, Cost: {cost:.6f}")
  
  # Actualiza el peso 'w' en dirección al gradiente para reducir el error en la siguiente época
  w += learning_rate*cost

# Bloque de prueba/evaluación de la red con datos nuevos
test_inputs = [5, 6]    # Nuevas entradas que el modelo no vio en el entrenamiento
test_targets = [10, 12]  # Resultados reales esperados para esas nuevas entradas

# Calcula las predicciones del modelo usando el peso 'w' final ajustado
pred = [predict(i) for i in test_inputs]

# Recorre las entradas, objetivos y predicciones en paralelo usando zip() para mostrar los resultados
for i, t, p in zip(test_inputs, test_targets, pred):
  # Imprime cada caso de prueba con la entrada, el valor real y la predicción (con 4 decimales)
  print(f"input:{i}, target:{t}, pred:{p:.4f}")
