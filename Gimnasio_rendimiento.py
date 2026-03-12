from limpiar_pantalla import limpiar_pantalla
limpiar_pantalla()

bajo = 0
medio = 0
alto = 0

for i in range(5):
    try:
        print("\nPersona", i + 1)

        nombre = input("Ingrese el nombre: ")
        dias = int(input("Días asistidos en la semana: "))
        minutos = int(input("Minutos promedio entrenados por día: "))

        if dias < 3:
            print(nombre, "tiene bajo compromiso")
            bajo += 1
        elif dias >= 3 and dias <= 4:
            print(nombre, "tiene compromiso medio")
            medio += 1
        else:
            print(nombre, "tiene compromiso alto")
            alto += 1
    except ValueError:
        print("Error, por favor ingrese un número válido.")

limpiar_pantalla()

print("\nRESUMEN")
print("Bajo compromiso:", bajo)
print("Compromiso medio:", medio)
print("Compromiso alto:", alto)