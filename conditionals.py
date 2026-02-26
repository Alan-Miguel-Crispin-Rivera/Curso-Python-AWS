# Se va a crear un validaddor para saber si podemos o no entrar a una fiesta, es importante agregar que para entrar a la fiesta debes de ser mayor de edad
# Vamos a comparar si la edad es mayor o igual a 18
# Recordemos que cuando usamos la funcion input, todo lo que se ingrese por consola sera un string, entonces, si queremos que sea de otro tipo de dato
# tendremos que utilizar alguna funciona que lo cambie, en este caso, usamos la funcion int para convertir un string a un valor de tipo int 

age = int(input("Ingrese su edad: "))

if age >= 18:
    print("Puede ingresar a la fiesta")
else:
    print("No puede ingresar a la fiesta")


# Ahora vamos a validar si la persona es mayor de edad y ademas, si la persona tiene mas de 600 pesos Version 1
edad = int(input("Ingrese su edad: "))
dinero = int(input("Ingrese la cantidad de dinero que trae: "))

if edad >= 18:
    if dinero >= 600:
        print("Puede ingresar a la fiesta")
    else:
        print("Saldo insuficiente jaja ")
else:
    print("No puede entrar a la fiesta")

# Ahora vamos a validar si la persona es mayor de edad y ademas, si la persona tiene mas de 600 pesos Version 2    
if edad >= 18 and dinero >= 600:
    print("Puede ingresar a la fiesta")
else:
    print("No puede entrar a la fiesta")
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Condicional con multiples comparaciones

your_money = input("Escriba el dinero con el que cuenta: ")
your_money = int(your_money)

if your_money < 100:
    print("Le compra unas galletas")
elif your_money >= 100 and your_money <= 200:
    print("Le compra unos chocolates")
elif your_money >= 200 and your_money <= 300:
    print("Le compro un peluche")
else:
    print("Le compro unos audifonos")
    
    
# ------------------------------------------LABORATORIO-------------------------------------------------------------------------------------------------------    
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Estamos usando la comparacion con el == para saber si es igual o no
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    
# Version mejorada usando elif para tener mas opciones 
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")