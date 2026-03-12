from limpiar_pantalla import limpiar_pantalla
limpiar_pantalla()

bajo = 0
medio = 0
alto = 0
i = 0

while i < 5:
    try:
        print("Persona", i + 1)

        nombre = input("Ingrese el nombre:\n#  ")
        if not nombre.isalpha():
            i = 0
            print("solo puede ingresar letras")
            input("Presione enter para continuar")
            limpiar_pantalla()
            continue
        else:
            i +=1
        print("")
        dias = int(input("Días asistidos en la semana:\n#  "))
        print("")
        minutos = int(input("Minutos promedio entrenados por día:\n#  "))
        limpiar_pantalla()

    except ValueError:
        print("Error, por favor ingrese un número válido.")

limpiar_pantalla()
print("RESUMEN")
if dias < 3:
    print(nombre, "tiene bajo compromiso")
    bajo += 1
elif dias >= 3 and dias <= 4:
    print(nombre, "tiene compromiso medio")
    medio += 1
else:
    print(nombre, "tiene compromiso alto\n")
    alto += 1

print("Bajo compromiso:", bajo)
print("Compromiso medio:", medio)
print("Compromiso alto:", alto)