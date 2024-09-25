"""Calculadora de Promedio de Calificaciones
Crea un sistema que permita al usuario ingresar las calificaciones de varios estudiantes y calcule el promedio general.
Usa condicionales para validar si el estudiante ha aprobado o reprobado"""

def Calcular_promedio (calificaciones,cantidad):
    return sum (calificaciones) / cantidad
def estado_del_estudiante(promedio):
    if promedio >= 4: 
        return "Aprobado"
    else:
        return "Reprobado"

calificaciones = []
cantidad = int(input("¿Cuantas calificaciones desea ingresar?: "))
contador = 0
while contador < cantidad:
    calificacion = float(input("Ingrese Calificación: "))
    if (calificacion in range(0,6)):
        calificaciones.append(calificacion)
        contador += 1
    else:
        print ("Ingresaste la calificación incorrecta el rango es de 0 - 5")
promedio = Calcular_promedio(calificaciones,cantidad)
estado = estado_del_estudiante (promedio)

print(f"Promedio: {promedio}, Estado: {estado}")