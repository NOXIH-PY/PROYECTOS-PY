salario = float(input("introduce tu salario anual: "))

if salario > 50000:
    if salario > 100000:
        print("El impuesto es del 30%")
    else:
        print("El impuesto es del 28%")
else:
    print("No pagan inpuesto")