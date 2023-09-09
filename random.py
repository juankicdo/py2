import random

numeroAleatorio = random.randint(0, 100)
intentos = 0
correcto = False

print("¡Bienvenido al juego de adivinar el número!")
print("Intenta adivinar un número entre 0 y 100.")

while not correcto:
    idea = int(input("Ingresa tu suposición: "))
    intentos += 1

    if idea < numeroAleatorio:
        print("El número es mayor.")
    elif idea > numeroAleatorio:
        print("El número es menor.")
    else:
        correcto = True
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")