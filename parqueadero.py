from limpiar_pantalla import limpiar_pantalla

limpiar_pantalla()
try:
    horas = int(input("Ingrese el número de horas que ha estado estacionado: "))

    tarifa = 5000

    if horas <= 1:
        tarifa = 5000
        print(f"El costo total es: $ {tarifa} pesos.")
    elif horas >= 2:
        tarifa = tarifa + 3000 * (horas)
        print(f"El costo total es: $ {tarifa} pesos.")

except ValueError:
    print("Error, por favor ingrese un número válido.")