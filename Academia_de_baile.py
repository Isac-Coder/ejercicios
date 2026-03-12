from limpiar_pantalla import limpiar_pantalla
limpiar_pantalla()

try:
    asistencia = int(input("Ingrese la cantidad de clases a las que asistio:\n"))

    if asistencia < 0:
        print("Su asistencia no puede ser menor a 0")
    
    elif asistencia < 5:
        print("Su asistencia BAJA")
    elif asistencia >= 5 and asistencia < 8:
        print("Su asistencia es MEDIA")
    else:
        print("Su asistencia es ALTA")
except ValueError:
    print("Por favor ingrese un numero valido o un valor numerico")