from limpiar_pantalla import limpiar_pantalla

limpiar_pantalla()
print("--- CONTROL DE SALA DE CINE ---")

capacidad = 0
while True:
    try:
        capacidad = int(input("Ingrese la capacidad total de la sala: "))
        if capacidad > 0:
            break
        print("La capacidad debe ser mayor a 0.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

contador_personas = 0
ninos = 0
adultos = 0
adultos_mayores = 0
sala_llena = False

while contador_personas < capacidad:
    limpiar_pantalla()
    print(f"Ocupación: {contador_personas}/{capacidad}")
    print("Ingrese la edad de la persona o escriba 'fin' para terminar antes.")
    
    entrada = input(">> ")
    
    if entrada.lower() == 'fin':
        break
        
    try:
        edad = int(entrada)
        if edad < 0:
            print("La edad no puede ser negativa.")
            input("Enter para continuar...")
            continue
            
        contador_personas += 1
        
        if edad < 12:
            ninos += 1
            print("Registrado como: NIÑO")
        elif edad >= 60:
            adultos_mayores += 1
            print("Registrado como: ADULTO MAYOR")
        else:
            adultos += 1
            print("Registrado como: ADULTO")
            
        input("Persona registrada. Presione Enter...")
        
    except ValueError:
        print("Error: Ingrese una edad válida.")
        input("Enter para continuar...")

if contador_personas == capacidad:
    sala_llena = True

limpiar_pantalla()
print("--- RESUMEN DE SALA ---")
print(f"Total personas ingresadas: {contador_personas}")
print(f"Niños: {ninos} | Adultos: {adultos} | Adultos Mayores: {adultos_mayores}")
print(f"Estado de la sala: {'LLENA' if sala_llena else 'DISPONIBLE'}")