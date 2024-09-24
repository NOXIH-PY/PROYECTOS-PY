"""
Condicionales en Python
Los condicionales permiten tomar decisiones dentro de un programa, Mediante una estructura de Condiciones
segun si una condicion es verdadera o falsa
"""
#Ejemplo if - else
edad = 8
if edad>= 18:
    print("Eres Mayor de Edad") #bloque si la condicion es verdadera
else:
    print("Eres Menor de Edad")#bloque si la condición es falsa

#Ejemplo de if - elif - else

nota = 3
if nota == 5:
    print("Exelente")
elif nota >= 4:
    print("Aprovó")
else:
    print("Reprobó")