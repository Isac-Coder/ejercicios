from limpiar_pantalla import limpiar_pantalla

venta_alimento = 0
venta_juguete = 0
venta_accesorio = 0

for i in range(1, 11):
    limpiar_pantalla()
    print(f"--- VENTA {i}/10 ---")
    print("Categorías: 1. Alimento | 2. Juguete | 3. Accesorio")
    
    categoria = 0
    while True:
        try:
            categoria = int(input("Seleccione categoría (1-3): "))
            if 1 <= categoria <= 3:
                break
            print("Opción fuera de rango.")
        except ValueError:
            print("Error: Ingrese un número.")
            
    valor = 0
    while True:
        try:
            valor = float(input("Ingrese valor de la compra: "))
            if valor > 0:
                break
            print("El valor debe ser positivo.")
        except ValueError:
            print("Error: Ingrese un número válido.")
            
    if categoria == 1:
        venta_alimento += valor
    elif categoria == 2:
        venta_juguete += valor
    elif categoria == 3:
        venta_accesorio += valor
        
    input("Venta registrada. Enter para continuar...")

limpiar_pantalla()
print("--- INFORME DE VENTAS ---")
print(f"Total Alimentos:   ${venta_alimento}")
print(f"Total Juguetes:    ${venta_juguete}")
print(f"Total Accesorios:  ${venta_accesorio}")

mayor_venta = venta_alimento
cat_ganadora = "Alimento"

if venta_juguete > mayor_venta:
    mayor_venta = venta_juguete
    cat_ganadora = "Juguete"
    
if venta_accesorio > mayor_venta:
    mayor_venta = venta_accesorio
    cat_ganadora = "Accesorio"
    
if mayor_venta == 0:
    print("No hubo ventas.")
else:
    print(f"\nLa categoría con más ingresos fue: {cat_ganadora} (${mayor_venta})")