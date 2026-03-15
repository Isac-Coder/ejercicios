from limpiar_pantalla import limpiar_pantalla
limpiar_pantalla()

bajo = 0
medio = 0
alto = 0

print("--- RENDIMIENTO GIMNASIO ---")

for i in range(1, 6):
    print(f"\n--- Persona {i}/5 ---")
    nombre = input("Ingrese el nombre: ")

    dias = 0
    while True:
        try:
            dias = int(input("Días asistidos en la semana: "))
            if 0 <= dias <= 7:
                break
            print("Los días deben ser entre 0 y 7.")
        except ValueError:
            print("Error: Ingrese un número válido.")
            
    while True:
        try:
            minutos = int(input("Minutos promedio entrenados por día: "))
            if minutos >= 0:
                break
            print("El tiempo no puede ser negativo.")
        except ValueError:
            print("Error: Ingrese un número válido.")

    if dias < 3:
        print(f"Resultado: {nombre} tiene BAJO compromiso.")
        bajo += 1
    elif 3 <= dias <= 4:
        print(f"Resultado: {nombre} tiene COMPROMISO MEDIO.")
        medio += 1
    else:
        print(f"Resultado: {nombre} tiene ALTO compromiso.")
        alto += 1

limpiar_pantalla()

print("\nRESUMEN")
print(f"Bajo compromiso:   {bajo}")
print(f"Compromiso medio:  {medio}")
print(f"Compromiso alto:   {alto}")
input("\nPresione Enter para terminar...")