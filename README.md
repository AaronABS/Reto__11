## Reto__11
# Las Matrices podrán ser cuadrículadas, pero a mi no me cuadran
### Punto 1. 
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```
# Solicitar las medidas de las matrices, columnas y filas
columna = int(input("Ingrese el numero de columnas para las matrices: "))
fila = int(input("Ingrese el numero de filas para las matrices: "))
# Se crea la matriz con las medidas dadas
# Solicitar las datos de la matriz
print("Ingrese los valores de la primera matriz:")
primeraMatriz = []
# Se crea un ciclo for para almacenar los valores de primeraMatriz
for i in range(fila):
    fila_primeraMatriz = []
    for j in range(columna):
        fila_primeraMatriz.append(int(input()))
# Se utiliza .append para agragar los valores a la fila_primeraMatriz
    primeraMatriz.append(fila_primeraMatriz)
# Se crea la segunda matriz con los mismos procedimientos
print("Ingrese los valores de la segunda matriz:")
segundaMatriz = []
for i in range(fila):
    fila_segundaMatriz = []
    for j in range(columna):
        fila_segundaMatriz.append(int(input()))
    segundaMatriz.append(fila_segundaMatriz)
# Se establece la suma o resta de las matrices
procedimiento = input("¿Quiere sumar o restar las matrices? ")
if procedimiento == "sumar":
    resultado = []
    for i in range(fila):
        fila_resultado = []
        for j in range(columna):
            fila_resultado.append(primeraMatriz[i][j] + segundaMatriz[i][j])
        resultado.append(fila_resultado)
    print("La suma de las matrices es:")
    for i in range(fila):
        print(resultado[i])
elif procedimiento == "restar":
    resultado = []
    for i in range(fila):
        fila_resultado = []
        for j in range(columna):
            fila_resultado.append(primeraMatriz[i][j] - segundaMatriz[i][j])
        resultado.append(fila_resultado)
    print("La resta de las matrices es:")
    for i in range(fila):
        print(resultado[i])
else:
    print("Procedimiento invalido. Por favor, ingrese 'sumar' o 'restar'.")
```

### Punto 2. 
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

### Punto 3. 
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

### Punto 4. 
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

### Punto 5. 
Desarrollar un programa que sume los elementos de una fila dada de una matriz.
