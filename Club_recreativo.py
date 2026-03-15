from limpiar_pantalla import limpiar_pantalla

PRECIO_BASICO = 50000
PRECIO_PREMIUM = 90000
PRECIO_FAMILIAR = 130000

total_recaudado = 0
cnt_basico = 0
cnt_premium = 0
cnt_familiar = 0

while True:
    limpiar_pantalla()
    print("--- REGISTRO CLUB RECREATIVO ---")
    print("Escriba 'salir' en nombre para terminar.")
    
    nombre = input("Nombre de la persona: ")
    if nombre.lower() == 'salir':
        break
        
    try:
        edad = int(input("Ingrese la edad: "))
        if edad < 0:
            print("Edad no válida.")
            input("Enter para continuar...")
            continue
            
        print("\nPLANES:")
        print(f"1. Básico   (${PRECIO_BASICO})")
        print(f"2. Premium  (${PRECIO_PREMIUM})")
        print(f"3. Familiar (${PRECIO_FAMILIAR})")
        
        opcion = input("Seleccione plan (1-3): ")
        valor_pagar = 0
        plan_nombre = ""
        
        if opcion == "1":
            valor_pagar = PRECIO_BASICO
            plan_nombre = "Básico"
            cnt_basico += 1
        elif opcion == "2":
            valor_pagar = PRECIO_PREMIUM
            plan_nombre = "Premium"
            cnt_premium += 1
        elif opcion == "3":
            valor_pagar = PRECIO_FAMILIAR
            plan_nombre = "Familiar"
            cnt_familiar += 1
        else:
            print("Opción de plan no válida.")
            input("Enter para continuar...")
            continue
            
        print(f"\nPlan seleccionado: {plan_nombre}")
        if edad < 18:
            print(">> NOTA: Registro juvenil.")
        elif edad >= 60:
            print(">> NOTA: Beneficio senior aplicado (informativo).")
            
        print(f"Valor a pagar: ${valor_pagar}")
        
        total_recaudado += valor_pagar
        input("Registro guardado. Enter para continuar...")
        
    except ValueError:
        print("Error: Dato numérico inválido.")
        input("Enter para continuar...")

limpiar_pantalla()
print("--- INFORME FINAL DEL CLUB ---")
print(f"Total dinero recaudado: ${total_recaudado}")
print("\nVentas por plan:")
print(f"Básico:   {cnt_basico}")
print(f"Premium:  {cnt_premium}")
print(f"Familiar: {cnt_familiar}")

mas_vendido = "Ninguno"
max_v = 0

if cnt_basico > max_v:
    max_v = cnt_basico
    mas_vendido = "Básico"
    
if cnt_premium > max_v:
    max_v = cnt_premium
    mas_vendido = "Premium"

if cnt_familiar > max_v:
    max_v = cnt_familiar
    mas_vendido = "Familiar"
    
print(f"\nPlan más vendido: {mas_vendido}")