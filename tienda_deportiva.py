from limpiar_pantalla import limpiar_pantalla
limpiar_pantalla()

contador = 0
contador2 = 0
no_admitido = 0

for i in range(5):
    try:
        precio = int(input("Ingrese el precio del producto: "))

        if precio > 100000:
            contador += 1
        else:
            contador2 += 1
    except ValueError:
        no_admitido += 1
        print("Error, lo que ha ingresado no es admitido.")

limpiar_pantalla()
print("Cantidad de productos que cuestan más de 100000:", contador)
print("Cantidad de productos que cuestan menos de 100000:", contador2)
print("Cantidad de productos que no fueron admitido:", no_admitido)