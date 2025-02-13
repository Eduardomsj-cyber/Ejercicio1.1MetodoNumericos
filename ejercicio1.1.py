#   Codigo que implementa un esquema numerico 
#   para determinar la precision de una maquina
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025
#

# Explicación Detallada del Código


## **Código Original**

import numpy as np  # Importa la librería NumPy (no se usa en este código)

epsilon = 1.0  # Inicializa epsilon con un valor de 1.0
iteracion = 0  # Contador para el número de iteraciones

# Bucle para encontrar la precisión de máquina
while 1.0 + epsilon != 1.0:  # Mientras la suma siga siendo distinta de 1.0
    epsilon /= 2  # Divide epsilon entre 2 en cada iteración
    iteracion = iteracion + 1  # Incrementa el contador de iteraciones
    print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}")  # Imprime la iteración y el valor de epsilon

# Se multiplica por 2 para obtener el último valor significativo
epsilon *= 2
print(f"Precisión de máquina: {epsilon}")  # Muestra la precisión de máquina final
```

## **Explicación línea por línea**

### **1. Importación de librerías**
```python
import numpy as np
```
Esta línea importa la librería NumPy, aunque en este código no se utiliza y podría eliminarse sin afectar su funcionamiento.

### **2. Inicialización de variables**
```python
epsilon = 1.0  # Inicializa epsilon con 1.0
iteracion = 0  # Inicializa el contador de iteraciones en 0
```
- `epsilon`: Representa un valor pequeño que se usará para calcular la precisión de máquina.
- `iteracion`: Contador de cuántas veces se ha dividido `epsilon`.

### **3. Inicio del bucle `while`**
```python
while 1.0 + epsilon != 1.0:
```
- Se ejecuta mientras `1.0 + epsilon` sea distinto de `1.0`.
- Cuando `epsilon` es muy pequeño, la suma `1.0 + epsilon` se redondea a `1.0` debido a la precisión limitada de los números en coma flotante.
- El objetivo es encontrar el menor `epsilon` que aún haga que `1.0 + epsilon` sea diferente de `1.0`.

### **4. Reducción progresiva de `epsilon`**
```python
epsilon /= 2
```
- `epsilon` se divide entre `2` en cada iteración para encontrar el valor más pequeño que todavía afecte la suma con `1.0`.

### **5. Contador de iteraciones**
```python
iteracion = iteracion + 1
```
- Se incrementa `iteracion` para contar cuántas veces se ha dividido `epsilon`.

### **6. Imprimir el valor actual de `epsilon`**
```python
print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}")
```
- Muestra en pantalla el número de iteración y el valor actual de `epsilon`.

### **7. Finalización del bucle y corrección de `epsilon`**
```python
epsilon *= 2
```
- Cuando el bucle termina, `epsilon` es demasiado pequeño para afectar la suma.
- Se multiplica por `2` para recuperar el último valor que sí afectaba la suma.

### **8. Imprimir el resultado final**
```python
print(f"Precisión de máquina: {epsilon}")
```
- Se imprime el valor final de `epsilon`, que representa la **precisión de máquina**.

## **Ejemplo de salida**

Si ejecutamos el código, podríamos obtener un resultado como este:

```
Iteracion: 1, Precisión de máquina: 0.5
Iteracion: 2, Precisión de máquina: 0.25
...
Iteracion: 52, Precisión de máquina: 2.220446049250313e-16
Precisión de máquina: 2.220446049250313e-16
```

## **Conclusión**

Este código encuentra la **precisión de máquina** en números de punto flotante de 64 bits (doble precisión, IEEE 754). El valor obtenido (~`2.22e-16`) indica el número más pequeño que, sumado a `1.0`, aún produce un cambio en la representación numérica de la computadora.

