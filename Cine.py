from limpiar_pantalla import limpiar_pantalla

limpiar_pantalla()

try:
    edad = int(input("Digite su edad para mostrar los precios de las entradas: "))

    if edad <= 0:
        print("Error. No puede ingresar 0 o números negativos.")
    
    elif edad < 12:
        print("El precio de la entrada es de $8.000")
    
    elif edad <= 59:
        print("El precio de la entrada es de $12.000")
    
    else:
        print("El precio de la entrada es de $9.000")

except ValueError:
    print("Error, por favor ingrese un número válido.")

input("\nPresione Enter para salir...")