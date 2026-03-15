from limpiar_pantalla import limpiar_pantalla

total_recaudado = 0
carros = 0
motos = 0

vehiculo_pago_max = 0
placa_pago_max = ""
tipo_pago_max = ""

for i in range(1, 9):
    limpiar_pantalla()
    print(f"--- REGISTRO VEHÍCULO {i}/8 ---")
    
    placa = input("Ingrese la placa: ").upper()
    
    tipo = ""
    while True:
        print("Tipo de vehículo: 1. Carro  2. Moto")
        opc = input("Seleccione (1 o 2): ")
        if opc == "1":
            tipo = "carro"
            break
        elif opc == "2":
            tipo = "moto"
            break
        else:
            print("Opción inválida.")
            
    horas = 0
    while True:
        try:
            horas = int(input("Ingrese horas parqueado: "))
            if horas > 0:
                break
            print("Debe ser mínimo 1 hora.")
        except ValueError:
            print("Error: Ingrese un número válido.")

    pago = 0
    if tipo == "carro":
        pago = horas * 4000
        carros += 1
    else:
        pago = horas * 2000
        motos += 1
        
    print(f"Valor a pagar: ${pago}")
    input("Presione Enter para continuar...")
    
    total_recaudado += pago
    
    if pago > vehiculo_pago_max:
        vehiculo_pago_max = pago
        placa_pago_max = placa
        tipo_pago_max = tipo

limpiar_pantalla()
print("--- FIN DEL DÍA PARQUEADERO ---")
print(f"Total recaudado: ${total_recaudado}")
print(f"Cantidad Carros: {carros}")
print(f"Cantidad Motos: {motos}")
if vehiculo_pago_max > 0:
    print(f"Vehículo que más pagó: {placa_pago_max} ({tipo_pago_max}) con ${vehiculo_pago_max}")