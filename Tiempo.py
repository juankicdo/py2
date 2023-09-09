tiempo_total = 0
tiempo_tramo = 1

while tiempo_tramo != 0:
    try:
        tiempo_tramo = int(input("Ingrese el tiempo del tramo en minutos (0 para terminar): "))
        tiempo_total += tiempo_tramo
    except ValueError:
        print("Por favor, ingrese un valor válido.")

horas = tiempo_total // 60
minutos = tiempo_total % 60

print("El tiempo total de viaje es:", horas, "horas", minutos, "minutos")
