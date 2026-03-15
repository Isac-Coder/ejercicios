from limpiar_pantalla import limpiar_pantalla

limpiar_pantalla()
print("Bienvenido al gimnasio.")

try:
    EDAD = int(input("Ingrese su edad: "))

    if EDAD < 0:
        print("Error: La edad no puede ser negativa.")
    elif EDAD < 13:
        print("Lo siento, no puedes ingresar al gimnasio.")
    elif 13 <= EDAD <= 17:
        print("Usted pertenece al grupo JUVENIL.")
    elif 18 <= EDAD <= 59:
        print("Usted pertenece al grupo GENERAL.")
    else:
        print("Usted pertenece al grupo SENIOR.")

except ValueError:
    print("Error: Debe ingresar un número entero válido.")

input("\nPresione Enter para salir...")