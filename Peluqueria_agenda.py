from limpiar_pantalla import limpiar_pantalla

total_dia = 0
cnt_corte = 0
cnt_cepillado = 0
cnt_tintura = 0

for i in range(1, 8):
    limpiar_pantalla()
    print(f"--- ATENCIÓN CLIENTE {i}/7 ---")
    
    nombre = input("Nombre del cliente: ")
    
    print("Servicios: 1. Corte | 2. Cepillado | 3. Tintura")
    servicio = ""
    while True:
        opc = input("Seleccione servicio (1-3): ")
        if opc == "1":
            servicio = "corte"
            cnt_corte += 1
            break
        elif opc == "2":
            servicio = "cepillado"
            cnt_cepillado += 1
            break
        elif opc == "3":
            servicio = "tintura"
            cnt_tintura += 1
            break
        else:
            print("Opción inválida.")

    valor = 0
    while True:
        try:
            valor = float(input("Valor pagado: "))
            if valor >= 0:
                break
            print("El valor no puede ser negativo.")
        except ValueError:
            print("Error numérico.")
            
    total_dia += valor
    print(f"Registrado: {nombre} - {servicio} - ${valor}")
    input("Enter para siguiente cliente...")

limpiar_pantalla()
print("--- CIERRE DE CAJA PELUQUERÍA ---")
print(f"Total recaudado en el día: ${total_dia}")
print("\nClientes por servicio:")
print(f"- Corte: {cnt_corte}")
print(f"- Cepillado: {cnt_cepillado}")
print(f"- Tintura: {cnt_tintura}")

mas_solicitado = "Ninguno"
max_cantidad = 0

if cnt_corte > max_cantidad:
    max_cantidad = cnt_corte
    mas_solicitado = "Corte"
if cnt_cepillado > max_cantidad:
    max_cantidad = cnt_cepillado
    mas_solicitado = "Cepillado"
if cnt_tintura > max_cantidad:
    mas_solicitado = "Tintura"
    
print(f"\nServicio más solicitado: {mas_solicitado}")