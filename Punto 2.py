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
