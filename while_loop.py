# Siempre que importemos una libreria debe de ir al inicio del codigo
import random

numero = input("Ingrese el numero 0: ")
numero = int(numero)

# Usaremos while para verificar que lo que hay dentro de la variable numero sea menor a 10
while numero < 10 :
    # Aumentamos el valor para que no se convierta en un bucle infinito
    numero = numero + 1
    # Solo se va a imprimir el valor si numero es menor a 10
    print(numero)
    
    
# Vamos a construir un while que nos muestre la tabla de multiplicar de algun numero
number = input("Ingrese un numero entre 0 y 10: ")
number = int(number)

# Inicializamos el multiplicador 
multiplicador = 0

while multiplicador < 10 :
    # Se incrementa el valor del multiplicador 
    multiplicador = multiplicador + 1
    multiplicacion = number * multiplicador
    # print(number, " * ", multiplicador, " ", multiplicacion)
    # Estamos usando los fstrings ajaja o como se llamen
    print(f"{number} * {multiplicador} = {multiplicacion}")
    
# -----------------------------------------------------------LABORATORIO------------------------------------------------------------------------
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

num = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == num:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        

