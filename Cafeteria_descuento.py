café = 4000
capuchino = 7000
pastel = 6000
compra = 0
from limpiar_pantalla import limpiar_pantalla

limpiar_pantalla()
print("Bienvenido a la cafetería. \n")
bebida = input("Ingrese lo que desea comprar (1 = café, 2 = capuchino, 3 = pastel): \n").lower()
if bebida not in ["1", "2", "3", "café", "capuchino", "pastel"]:
    print("Bebida no válida. Intente nuevamente.")
    exit()

unidades = input("Ingrese la cantidad de unidades que desea: \n")

if unidades != int:
    print("Cantidad no válida. Intente nuevamente.")
elif int(unidades) <= 0:
    print("Cantidad no válida. Intente nuevamente.")
