"""Adivina la palabra"""

PalabraAdivinar = "HolaProgramadores"

intentos_max = 4
intento = 0

while intentos_max != intento:
    print("*********JUEGO DE ADIVINAR********")
    print(f"Tienes {intentos_max} intentos te quedan {intentos_max - intento}")

    intentoAdivinar = input(f"Ingresa la palabra: ")

    if intentoAdivinar == PalabraAdivinar:
        print("Ganaste...")
    elif intentoAdivinar < PalabraAdivinar:
        print("Fallaste...")
        intento = intento+1
    else:
        print("Perdiste la palabra era {PalabraAdivinar}")