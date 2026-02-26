# Creamos una lista de datos de diferentes tipos
my_mixed_type_list = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Usamos el ciclo for para recorrer nuestra lista, uno por uno de los elementos de la lista
for item in my_mixed_type_list:
    print("{} is of the data type {}".format(item,type(item)))