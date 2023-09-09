# Definición de funciones como variables
mi_print = print
mi_float = float
mi_len = len
mi_sorted = sorted
mi_input = input

numeros = []
entrada_usuario = mi_input("Ingrese los números ordenados (ingrese '.' para terminar): ")
while entrada_usuario != '.':
    numero = mi_float(entrada_usuario)
    numeros.append(numero)
    entrada_usuario = mi_input()

numeros_ordenados = mi_sorted(numeros)
cantidad_numeros = mi_len(numeros_ordenados)
mediana = 0

if cantidad_numeros % 2 == 0:
    indice1 = cantidad_numeros // 2 - 1
    indice2 = cantidad_numeros // 2
    mediana = (numeros_ordenados[indice1] + numeros_ordenados[indice2]) / 2
else:
    indice = cantidad_numeros // 2
    mediana = numeros_ordenados[indice]

mi_print("La mediana de los números es:", mediana)
