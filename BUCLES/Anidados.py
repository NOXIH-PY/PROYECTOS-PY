"""
for variable1 in secuencia1:
    for variable2 in secuencia2:
        #Bloque de codigo a repetir

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in matriz:
    for elementos in i:
        print(elementos)
    print()


suma = 0
for i in range(10):
    for y in range(10):
        for x in range(10):
            print(f"{i} x {y} x {x}")
        print()

"""

while True:
    print("-------Menu---------")
    print("1. Pasta")
    print("2. Carne")
    print("2. Pollo")
    print("2. Salir")
    opción = int(input("Elije una opción: "))

    if opción == 1:
        print("Prepara Pastas")
    elif opción == 2:
        print("Prepara carne")
    elif opción == 3:
        print("Prepara Pollo")
    elif opción == 4:
        print("Saliendo...")
        break
    else:
        print("Opción no valida")