numPositivos = 0
numNegativos = 0
num = int(input("Ingrese un número entero (0 para terminar): "))

while num != 0:
    if num > 0:
        numPositivos += 1
    elif num < 0:
        numNegativos += 1
    num = int(input("Ingrese un número entero (0 para terminar): "))

print("positivos: ", end="")
for i in range(numPositivos):
    print("*", end="")

print()

print("negativos: ", end="")
for i in range(numNegativos):
    print("*", end="")
