num = input("Ingrese un número: ")
numOriginal = num
numInvertido = 0

while int(num) > 0:
    digito = int(num) % 10
    numInvertido = numInvertido * 10 + digito
    num = int(num) // 10

if int(numOriginal) == numInvertido:
    print("El número es un palíndromo.")
else:
    print("El número no es un palíndromo.")
