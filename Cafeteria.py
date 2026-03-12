café = 4000
té = 3500
jugo = 5000
from limpiar_pantalla import limpiar_pantalla

limpiar_pantalla()
print("Bienvenido a la cafetería. \n")
bebida = input("Ingrese la bebida que desea (1 = café, 2 = té, 3 = jugo): \n").lower()
if bebida not in ["1", "2", "3", "café", "té", "jugo"]:
    print("Bebida no válida. Intente nuevamente.")
    exit()

unidades = input("Ingrese la cantidad de unidades que desea: \n")

if unidades != int:
    print("Cantidad no válida. Intente nuevamente.")
elif int(unidades) <= 0:
    print("Cantidad no válida. Intente nuevamente.")

if bebida == "1" or bebida == "café":
    print(f"El precio del café es: {café} pesos.")
    café = café * int(unidades)
elif bebida == "2" or bebida == "té":
    print(f"El precio del té es: {té} pesos.")
    té = té * int(unidades)
elif bebida == "3" or bebida == "jugo":
    print(f"El precio del jugo es: {jugo} pesos.")
    jugo = jugo * int(unidades)
else:
    print("Bebida no válida. Intente nuevamente.")
    
if bebida in ["1", "2", "3"]:
    total = café + té + jugo
    print(f"El total a pagar por {unidades} unidades de {bebida} es: {total} pesos.")