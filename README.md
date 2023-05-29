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
def primeraMatriz(columnas, filas) -> list: # Se define una función donde se establece la primera matriz
    matriz = []  
    for i in range(filas):  # Se crea un ciclo para obtener una matriz en forma de lista 
        fila = []  
        for j in range(columnas):  
            datos = float(input("Ingrese los valores de la primera matriz: "))   
            fila.append(datos)  # Se anexan los datos introducidos
        matriz.append(fila)  
    return matriz  # Retorna la matriz 

def segundaMatriz(filas, columnas) -> list: # Se define una función donde se establece la segunda matriz bajo el mismo procedimiento que la primera matriz
    matriz2 = []  
    for i in range(filas): 
        fila = [] 
        for j in range(columnas): 
            datos = float(input("Ingrese los valores de la segunda matriz: ")) 
            fila.append(datos) 
        matriz2.append(fila)
    return matriz2 # Devuelve la segunda matriz completa como una lista de listas
    

def producto(matriz1, matriz2) -> list:   # Se define una función para realizar la multiplicación
    filasMatriz1 = len(matriz1)  # Se obtiene la cantidad de filas y columnas de la primera matriz y de las columnas de la segunda matriz
    columnasMatriz1 = len(matriz1[0])   
    columnasMatriz2 = len(matriz2[0])  

    solucion = []  # Para almacenar la solucion del producto se crea esta lista vacia

    for i in range(filasMatriz1):  # Se crea un ciclo sobre las filas de la primera matriz
        fila = []  
        for j in range(columnasMatriz2):  
            numeral = 0  
            for k in range(columnasMatriz1):  
                numeral += matriz1[i][k] * matriz2[k][j]  # Se acumula y multiplica el resultado en el numeral
            fila.append(numeral)  # Se agregan los datos respectivamente al numeral y posteriormente a la fila
        solucion.append(fila)  

    return solucion  # Devuelve la solucion del producto como una matriz



filas = int(input("Ingrese el numero de filas: "))  # Se pide el numero de filas de ambas matrices
columnas = int(input("Ingrese el numero de columnas: "))  # Se pide el numero de  columnas de ambas matrices
matriz1 = primeraMatriz(filas, columnas)  
print("La primera matriz es: " + str(matriz1))  # Se imprime la matriz 1
matriz2 = segundaMatriz(filas, columnas)  # 
print("La segunda matriz es: " + str(matriz2))  # Se imprime la matriz 2
productoDeMatrices = producto(matriz1, matriz2)  
print("El resultado de la multiplicación de las matrices es:", str(productoDeMatrices))  # Se imprime el productod de las matrices
```

### Punto 3. 
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

### Punto 4. 
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

### Punto 5. 
Desarrollar un programa que sume los elementos de una fila dada de una matriz.
