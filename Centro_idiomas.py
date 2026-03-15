from limpiar_pantalla import limpiar_pantalla

suma_promedios = 0
cantidad_estudiantes = 0

bajo = 0
medio = 0
alto = 0

mejor_estudiante = ""
mejor_promedio = -1

while True:
    limpiar_pantalla()
    print("--- EVALUACIÓN DE ESTUDIANTES ---")
    
    nombre = input("Nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
        
    try:
        speaking = float(input("Nota Speaking (0-100): "))
        listening = float(input("Nota Listening (0-100): "))
        reading = float(input("Nota Reading (0-100): "))
        
        if not (0 <= speaking <= 100 and 0 <= listening <= 100 and 0 <= reading <= 100):
            print("Las notas deben estar entre 0 y 100.")
            input("Enter para reintentar...")
            continue
            
        promedio = (speaking + listening + reading) / 3
        
        nivel = ""
        if promedio < 60:
            nivel = "Bajo"
            bajo += 1
        elif 60 <= promedio <= 79:
            nivel = "Medio"
            medio += 1
        else:
            nivel = "Alto"
            alto += 1
            
        print(f"Promedio: {promedio:.2f} - Nivel: {nivel}")
        
        suma_promedios += promedio
        cantidad_estudiantes += 1
        
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_estudiante = nombre
            
        input("Estudiante registrado. Enter para continuar...")
        
    except ValueError:
        print("Error: Debe ingresar notas numéricas.")
        input("Enter para continuar...")

limpiar_pantalla()
print("--- RESULTADOS DEL GRUPO ---")

if cantidad_estudiantes > 0:
    prom_gral = suma_promedios / cantidad_estudiantes
    print(f"Promedio general del grupo: {prom_gral:.2f}")
    print(f"Mejor estudiante: {mejor_estudiante} con {mejor_promedio:.2f}")
    print("\nClasificación por niveles:")
    print(f"Nivel Bajo (<60):  {bajo}")
    print(f"Nivel Medio (60-79): {medio}")
    print(f"Nivel Alto (80+):   {alto}")
else:
    print("No se registraron estudiantes.")