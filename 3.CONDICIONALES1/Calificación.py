"""
Escribe un programa que pida una calificación numérica
(0 - 100) y determine si el estudiante aprueba o no (60 o más aprobado)
"""
import math
calificación = float(input("ingrese tu calificación "))

calificación = round(calificación) #aproximación normal

#calificación = math.floor(calificación) #aproximación hacia a abajo

#calificación = math.ceil(calificación) #aproximación hacia arriba

if calificación >=60 and calificación <= 100:
    print("Aprovado")
elif calificación >= 0 and calificación <60:
    print("Reprobó")
else:
    print("La calificación no es valida")