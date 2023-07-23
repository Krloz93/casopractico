import random 


valorfilas = 0
valorcolumnas = 0
listafila = []
listacolumna = []
matriz = []

# Introduce dimensión
try: 
    n = int(input('ingrese el numero de fila: '))

    while n < 2:
        print('valor no valido')
        n = int(input('ingrese el numero de fila: '))
#exepcion de tipo de datos 
except ValueError:
    print('valor incorrecto')


#crea una matriz nxn con numeros aleatorios
for i in range(n):  
    matriz.append([])
    for j in range(n):
         matriz[i].append(random.randint(0, 9))


#Imprime la matriz
print('\nMatriz aleatoria:')
for fila in matriz:
    print(" ".join(map(str, fila)))

# Funciones para sumar filas y columnas
def suma_columna(mtx, columna):
    rows = len(mtx)
    _ = len(mtx[0])
    suma = 0

    for fila in range(0, rows):
        suma += mtx[fila][columna]
        
    return suma 

def suma_fila(mtx, fila):
    _ = len(mtx)
    cols = len(mtx[0])
    suma = 0

    for columna in range(0, cols):
        suma += mtx[fila][columna]
        
    return suma 

#calcula la suma de cada fila y columna 
for idx in range(0, n):
    listafila.append(suma_fila(matriz, idx))
    listacolumna.append(suma_columna(matriz, idx))

print('\nSuma por filas:', listafila)
print('Suma por columnas:', listacolumna)

# test unitario 
def test_calcular_sumas():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sumas_filas = []
    sumas_columnas = []
    for idx in range(0, 3):
        sumas_filas.append(suma_fila(matriz, idx))
        sumas_columnas.append(suma_columna(matriz, idx))
    assert sumas_filas == [6, 15, 24]
    assert sumas_columnas == [12, 15, 18]

test_calcular_sumas()    


