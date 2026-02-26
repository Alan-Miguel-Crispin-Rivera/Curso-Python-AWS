# Variable que almacena una lista, las listas utilizan [], las listas son mutables
my_fruit_list = ["apple", "banana", "cherry"]
# Imprimimos la lista completa
print(my_fruit_list)
print(type(my_fruit_list))
# Imprimimos el primer elemento de la lista, despues el segundo y al final el tercero
print(my_fruit_list[0])
print(my_fruit_list[1])
print(my_fruit_list[2])

# Cambiamos el valor de la segunda posicion de nuestra lista, las listas son mutables
my_fruit_list[2] = "orange"
print(my_fruit_list)

# Variable que almacena una tupla, las tuplas utilizan (), las tuplas son inmutables
my_final_answer_tuple = ("apple", "banana", "pineapple")
print(my_final_answer_tuple)
print(type(my_final_answer_tuple))

# Aunque sea una tupla, para imprimir elementos usamos [], estamos imprimiendo el primer, segundo y tercer elemento
print(my_final_answer_tuple[0])
print(my_final_answer_tuple[1])
print(my_final_answer_tuple[2])

# Variable que almacena un diccionario, los diccionarios funcionan bajo el concepto de clave : valor 
my_favorite_fruit_dictionary = {
    "Alan" : "mango",
    "Sandra" : "banana",
    "Paulo" : "pineapple",
}

print(my_favorite_fruit_dictionary)
print(type(my_favorite_fruit_dictionary))

# Para imprimir un elemento de un diccionario en lugar de colocar la posicion, colocamos la clave (key) entre []
print(my_favorite_fruit_dictionary["Alan"])
print(my_favorite_fruit_dictionary["Sandra"])
print(my_favorite_fruit_dictionary["Paulo"])

