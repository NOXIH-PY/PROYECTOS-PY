def operaciones (a,b):
    def suma ():
        return(a + b)
    
    def resta ():
        return (a - b)
    
    resultado_suma = suma()
    resultado_resta = resta()

    return resultado_suma , resultado_resta

suma_resultado , resta_resultado = operaciones (10,5)
print(suma_resultado)