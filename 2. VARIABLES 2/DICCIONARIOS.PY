"""
Diccionarios
Es una colección desordenada de pares Clave-Valor donde cada clave es única
y estar asociada a un valor. se utilizan para representar una relación de datos

Caracteristicas:
 Los elementos se almacenan como pares clave-valor
 son mutables
 las claves son unicas, pero los valores pueden repetirse
 las claves debe ser inmutables
"""

#definicion de un diccionario
mi_diccionario = {
    "nombre":   "Erik Salamando",
    "edad":     24,
    "ciudad":   "Cartago",
    "idiomas":  ["ingles","español","Frances"],
    "Gruposanguineo": None
}

print(mi_diccionario["nombre"])  #Salida Erik Salmando

#modificar un valor
mi_diccionario["edad"] = 28
print(mi_diccionario)

#agregar clave valor
mi_diccionario["profesión"] = "Animador 3D"
print(mi_diccionario)

#eliminar un par de clave valor
del mi_diccionario["ciudad"]
print(mi_diccionario)
"""
Operadores
* del: elimina un par de clave de valor
"""