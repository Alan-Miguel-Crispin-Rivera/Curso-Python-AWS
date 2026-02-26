# Creamos una variable para guardar un texto (string)
my_string = "This is a string"

# Imprimimos el valor de la variable
print(my_string)

# Imprimimos el tipo de dato de la variable 
print(type(my_string))

# Imprimimos el valor de la variable junto con un string y junto con el tipo de dato utilizando las funciones str y type
print(my_string + " is of the data type " + str(type(my_string)))

# Creamos dos variables de tipo string
first_string = "water"
second_string = "fall"

# En la variable third_string guardamos la concatenacion de dos variables de tipo string
third_string = first_string + second_string

# Imprimimos el valor de la variable que contiene la concatenacion
print(third_string)

# Usamos la funcion input para almacenar lo que escriba el usuario por consola
name = input("What is your name?: ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

# Imprimimos multiples variables usando el metodo format, las variables se ponen en el orden en el que se usan en el texto 
print("{}, you like a {} {}!".format(name,color,animal))
