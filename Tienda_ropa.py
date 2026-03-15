from limpiar_pantalla import limpiar_pantalla

agotados = 0
stock_bajo = 0
stock_normal = 0

for i in range(1, 11):
    limpiar_pantalla()
    print(f"--- INVENTARIO PRODUCTO {i}/10 ---")
    
    nombre = input("Nombre del producto: ")
    
    cantidad = -1
    while True:
        try:
            cantidad = int(input(f"Cantidad disponible de '{nombre}': "))
            if cantidad >= 0:
                break
            print("La cantidad no puede ser negativa.")
        except ValueError:
            print("Error: Ingrese un número entero.")
            
    estado = ""
    if cantidad == 0:
        estado = "AGOTADO"
        agotados += 1
    elif 1 <= cantidad <= 5:
        estado = "STOCK BAJO"
        stock_bajo += 1
    else:
        estado = "STOCK NORMAL"
        stock_normal += 1
        
    print(f"Clasificación: {estado}")
    input("Enter para siguiente producto...")

limpiar_pantalla()
print("--- REPORTE DE INVENTARIO ---")
print(f"Productos Agotados:    {agotados}")
print(f"Productos Stock Bajo:  {stock_bajo}")
print(f"Productos Normales:    {stock_normal}")

if agotados > 0:
    print("\n¡ALERTA! Hay productos agotados que requieren reposición inmediata.")
elif stock_bajo > 0:
    print("\nAtención: Algunos productos tienen pocas unidades.")
else:
    print("\nEl inventario se encuentra saludable.")