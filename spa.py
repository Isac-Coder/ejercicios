from limpiar_pantalla import limpiar_pantalla
limpiar_pantalla()

servicio = input("Elija uno de estos servicios: (1: Masaje, 2: Facial, 3: Manicure)\n")

if servicio == "1" or servicio == "masaje":
    print("El servicio esta disponible")
elif servicio == "2" or servicio == "facial":
    print("El servicio esta disponible")
elif servicio == "3" or servicio == "manicure":
    print("El servicio esta disponible")
else:
    print("El servicio seleccionado no existe")