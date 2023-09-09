print("Ingrese la cantidad de datos: ")
numDatos = int(input())

datos = []


for i in range(numDatos):
    print("Ingrese el dato", i + 1, ": ")
    dato = int(input())
    datos.append(dato)


maximo = datos[0]
minimo = datos[0]
i = 1

while i < numDatos:
    if datos[i] > maximo:
        maximo = datos[i]
    if datos[i] < minimo:
        minimo = datos[i]
    i += 1

rango = maximo - minimo
print("El rango de los datos ingresados es:", rango)