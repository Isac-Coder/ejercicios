from limpiar_pantalla import limpiar_pantalla

PRECIO_CAFE = 4000
PRECIO_CAPUCHINO = 7000
PRECIO_PASTEL = 6000

total_dia = 0

while True:
    limpiar_pantalla()
    print("--- SISTEMA DE CAJA CAFETERÍA ---")
    print("Escriba 'salir' para cerrar la caja y ver el total del día.")
    print("Presione Enter para atender a un nuevo cliente.")
    
    opcion_principal = input(">> ").strip().lower()
    
    if opcion_principal == "salir":
        break
    
    total_cliente = 0
    while True:
        limpiar_pantalla()
        print(f"--- NUEVO PEDIDO --- Subtotal actual: ${total_cliente}")
        print("MENÚ DE PRODUCTOS:")
        print(f"1. Café       (${PRECIO_CAFE})")
        print(f"2. Capuchino  (${PRECIO_CAPUCHINO})")
        print(f"3. Pastel     (${PRECIO_PASTEL})")
        print("4. Finalizar pedido del cliente")
        
        try:
            entrada = input("\nSeleccione una opción (1-4): ")
            opcion = int(entrada)
        except ValueError:
            print("\nError: Debe ingresar un número válido.")
            input("Presione Enter para continuar...")
            continue
        
        precio_a_sumar = 0
        
        if opcion == 1:
            precio_a_sumar = PRECIO_CAFE
            print("Café agregado.")
        elif opcion == 2:
            precio_a_sumar = PRECIO_CAPUCHINO
            print("Capuchino agregado.")
        elif opcion == 3:
            precio_a_sumar = PRECIO_PASTEL
            print("Pastel agregado.")
        elif opcion == 4:
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")
            continue
            
        total_cliente += precio_a_sumar
        input("Producto registrado. Presione Enter para continuar...")

    limpiar_pantalla()
    print("--- RESUMEN DE CLIENTE ---")
    print(f"Subtotal: ${total_cliente}")
    
    if total_cliente > 20000:
        descuento = total_cliente * 0.10
        print(f"¡Descuento aplicado (10%)!: -${int(descuento)}")
        total_cliente -= descuento
    else:
        print("No aplica descuento.")
        
    print(f"TOTAL A COBRAR AL CLIENTE: ${int(total_cliente)}")
    total_dia += total_cliente
    
    input("\nPresione Enter para volver al menú principal...")

limpiar_pantalla()
print("--- FIN DEL DÍA ---")
print(f"Total acumulado de ventas: ${int(total_dia)}")