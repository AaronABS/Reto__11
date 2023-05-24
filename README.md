## Reto__11
# Las Matrices podrán ser cuadrículadas, pero a mi no me cuadran
### Punto 1. 
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```
# Se solicita las medidas de la matriz
fila = int(input("Ingrese el numero de filas para las matrices: "))
columna = int(input("Ingrese el numero de columnas para las matrices: "))
# Se crea la primera matriz
print("Ingrese los valores de la primera matriz:")
matriz1 = []
for i in range(fila):
    fila_matriz1 = []
    for j in range(columna):
        fila_matriz1.append(int(input()))
    matriz1.append(fila_matriz1)
# Se crea la segunda matriz
print("Ingrese los valores de la segunda matriz:")
matriz2 = []
for i in range(fila):
    fila_matriz2 = []
    for j in range(columna):
        fila_matriz2.append(int(input()))
    matriz2.append(fila_matriz2)
# Se determinan las operaciones entre las matrices
operacion = input("¿Desea sumar o restar las matrices? ")
if operacion == "sumar":
    resultado = []
    for i in range(fila):
        fila_resultado = []
        for j in range(columna):
            fila_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila_resultado)
    print("El resultado de la suma de las matrices es:")
    for i in range(fila):
        print(resultado[i])
elif operacion == "restar":
    resultado = []
    for i in range(fila):
        fila_resultado = []
        for j in range(columna):
            fila_resultado.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila_resultado)
    print("El resultado de la resta de las matrices es:")
    for i in range(fila):
        print(resultado[i])
# Especificación de las únicas dos operaciones posibles        
else:
    print("Operacion no valida. Por favor, ingrese 'sumar' o 'restar'.")
```

### Punto 2. 
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

### Punto 3. 
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

### Punto 4. 
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

### Punto 5. 
Desarrollar un programa que sume los elementos de una fila dada de una matriz.
