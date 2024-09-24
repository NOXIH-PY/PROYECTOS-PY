#listas
# una lista es una colección ordenada y mutable (se puede modificiar)
# y pueden almacenar cualquier tipo.
"""
Caracteristicas: 
Son ordenadas
son mutables
pueden contener elementos duplicados
los elementos puede ser de diferentes tipos
"""

mi_lista = [10,20,30,40,"Hola"]
print(mi_lista)

#Acceder a un elemento
print(mi_lista[3])

#modificar un elemento

mi_lista[3] = "Adios"
print(mi_lista)

#Agregar un elemento

mi_lista.append(60)
print(mi_lista)

#eliminar un elemento

mi_lista.remove(mi_lista[1])
print(mi_lista)

mi_lista.remove(10)
print(mi_lista)

#contador
print(len(mi_lista))
#operadores
"""
append(): Agrega un elemento al final
remove(): Elimina el primer elemento que coincide con el valor
len(): longitud de la lsita
"""