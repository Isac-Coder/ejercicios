from limpiar_pantalla import limpiar_pantalla

print("Bienvenido al gimnasio.: \n")
EDAD = input("Ingrese su edad: \n")

limpiar_pantalla()
if EDAD != int:
    print("Edad no válida. Intente nuevamente.")
elif EDAD < 13 and EDAD >= 0:
    print("Lo siento, no puedes ingresar al gimnasio.")
elif EDAD >= 13 and EDAD <= 17:
    print("Usted pertenece al grupo JUVENIL.")
elif EDAD >= 18 and EDAD <= 59:
    print("Usted pertenece al grupo GENERAL.")
elif EDAD >= 60:
    print("Usted pertenece al grupo SENIOR.")

else:
    print("Edad no válida. Intente nuevamente.")