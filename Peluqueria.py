from limpiar_pantalla import limpiar_pantalla

limpiar_pantalla()
try:
    print("Bienvenido a la peluquería")
    hora = int(input("Ingrese la hora de llegada (en formato 24 horas): "))

    if hora >= 6 and hora <= 11:
        print("Usted ha llegado en la mañana.")
    elif hora >= 12 and hora <= 17:
        print("Usted ha llegado en la tarde.")
    elif hora >= 18 and hora <= 22:
        print("Usted ha llegado en la noche.")
    else:
        print("Hora no válida. Por favor ingrese una hora entre 6 y 22.")
except ValueError:
    print("Error, por favor ingrese un número válido.")