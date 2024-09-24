Temperatura = float(input("ingrese la tempreatura actual: "))
llueve = input("está lloviendo? (Si/No)").lower()

if Temperatura < 15:
    if llueve == "SI":
        print("Usa un abrigo y paraguas")
    else:
        print("Usa un abrigo")
elif 15 <= Temperatura <=25:
    if llueve == "SI":
        print("Lleva paraguas")
    else:
        print("usa ropa ligera")
else:
    print("usa ropa fresca")
