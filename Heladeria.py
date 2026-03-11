pedidos = 0
vainilla = 0
chocolate = 0
fresa = 0

from limpiar_pantalla import limpiar_pantalla

for i in range(5):
    limpiar_pantalla()
    print("Bienvenido a la heladería. \n")
    sabor = input("Ingrese el sabor del helado (1 = vainilla, 2 = chocolate, 3 = fresa): \n").lower()
    
    if sabor == "1":
        sabor = "vainilla"
        vainilla += 1
    elif sabor == "2":
        sabor = "chocolate"
        chocolate += 1
    elif sabor == "3":
        sabor = "fresa"
        fresa += 1
    
    if sabor in ["vainilla", "chocolate", "fresa"]:
        pedidos += 1
    else:
        print("Sabor no válido. Intente nuevamente.\n")
        continue

    if i == 4:
        print(f"Pedido {i + 1}: Sabor seleccionado - {sabor}\n")
        print(f"Total de pedidos realizados: {pedidos}\n")
        print(f"Cantidad de helados pedidos por sabor:\n")
        print(f"Vainilla: {vainilla}")
        print(f"Chocolate: {chocolate}")
        print(f"Fresa: {fresa}")
    else:
        None