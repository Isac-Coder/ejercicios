from limpiar_pantalla import limpiar_pantalla
limpiar_pantalla()

total_vendido = 0
clientes = 0

cono_total = 0
vaso_total = 0
banana_total = 0

while True:
    try:
        print("MENU\n")
        print("1. Cono = 3000")
        print("2. Vaso = 4000")
        print("3. Banana Split = 9000")
        print("4. Salir")

        opcion = int(input("Seleccione un producto: "))

        if opcion == 4:
            break

        cantidad = int(input("Ingrese la cantidad: "))

        if opcion == 1:
            total = cantidad * 3000
            cono_total += cantidad
        elif opcion == 2:
            total = cantidad * 4000
            vaso_total += cantidad
        elif opcion == 3:
            total = cantidad * 9000
            banana_total += cantidad
        else:
            print("Opción inválida")
            input("precione enter para continuar")
            limpiar_pantalla()
            continue

        print("Total a pagar:", total,"\n")
        input("precione enter para continuar")
        limpiar_pantalla()

        total_vendido += total
        clientes += 1
    except ValueError:
        print("Opcion no valida")
        input("precione enter para continuar")
        limpiar_pantalla()

if cono_total > vaso_total and cono_total > banana_total:
    mas_vendido = "Cono"
elif vaso_total > cono_total and vaso_total > banana_total:
    mas_vendido = "Vaso"
else:
    mas_vendido = "Banana Split"

limpiar_pantalla()
print("\nRESUMEN DEL DIA\n")
print("Total vendido:", total_vendido)
print("Clientes atendidos:", clientes)
print("Producto más pedido:", mas_vendido)