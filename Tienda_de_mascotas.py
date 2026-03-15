from limpiar_pantalla import limpiar_pantalla
limpiar_pantalla()

print("Elija una mascota")
print("1. Perro")
print("2. Gato")
print("3. Conejo\n")
mascota = input("Ingrese el nombre o numero de la mascota: ").lower

if mascota == "perro" or mascota == "1":
    print("¡Tienes un perro! Te recomiendo el Dog Chow, es muy nutritivo para ellos.")
elif mascota == "gato" or mascota == "2":
    print("¡Tienes un gato! Te recomiendo el Purina Cat Chow, es perfecto para su dieta.")
elif mascota == "conejo" or mascota == "3":
    print("¡Tienes un conejo! Te recomiendo el Bunny Nature, es ideal para su alimentación.")
else:
    print("Ingrese un nombre valido o numero")