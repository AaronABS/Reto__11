## Reto__11
# Las Matrices podrán ser cuadrículadas, pero a mi no me cuadran
### Punto 1. 
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```
columna = int(input("Ingrese el numero de columnas para las matrices: ")) # Solicitar las medidas de las matrices, columnas y filas
fila = int(input("Ingrese el numero de filas para las matrices: "))
print("Ingrese los valores de la primera matriz:") # Solicitar los datos de la matriz
primeraMatriz = []
for i in range(fila): # Se crea un ciclo for para almacenar los valores de primeraMatriz
    fila_primeraMatriz = []
    for j in range(columna):
        fila_primeraMatriz.append(int(input()))
    primeraMatriz.append(fila_primeraMatriz) # Se utiliza .append para agregar los valores a la primera matriz
print("Ingrese los valores de la segunda matriz:") # Se crea la segunda matriz con los mismos procedimientos
segundaMatriz = []
for i in range(fila):
    fila_segundaMatriz = []
    for j in range(columna):
        fila_segundaMatriz.append(int(input()))
    segundaMatriz.append(fila_segundaMatriz)
procedimiento = input("¿Quiere sumar o restar las matrices? ") # Se establece el procedimiento de la suma o de la resta para las matrices
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
    print("Procedimiento invalido. Por favor, ingrese 'sumar' o 'restar'.") # Se establece una condición en caso de que no sea posible la resta o la suma 
```

### Punto 2. 
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```

```

### Punto 3. 
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

### Punto 4. 
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

### Punto 5. 
Desarrollar un programa que sume los elementos de una fila dada de una matriz.
