#crear un a lista de frutas y concatenar sus elementos en una sola cadena de texto

#Crear la lista de frutas

frutas = ["Manzana","Pera","Naranja"]

#separación no optima
print(f"{frutas[0]},{frutas[1]},{frutas[2]}")

#concatenar los elementos de una lista

cadenaFrutas=",".join(frutas)
print(cadenaFrutas)