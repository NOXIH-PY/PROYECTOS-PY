"""
if condicion1:
    #bloque de codigo si condicion1 es verdadero
    if condicion2:
        #Bloque de codigo si condición 2 es verdadero pero condición 1 es verdadera
    else:
        #bloque de codigo si condición 2 es falsa pero condición 1 es vedadera
else:
    #bloque de codigo si condición 1 es falsa

"""

edad = 18
tiene_licencia = True
if edad >= 18:
    print("Eres mayor de edad,")

    if tiene_licencia:
        print("Tiene licnencia de conducir, Puede Manejar,")
    else:
        print("No tiene licencia de conducir, no puede manejar,")
else:
    print("eres menor de edad no puede manejar,")