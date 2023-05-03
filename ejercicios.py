# Adivinar un número aleatorio
import random
numsecre=random.randint(0,100)
intentos = 0
print("Adivine el número comprendido entre el 0 y el 100: ")

while True: 
    intento=int(input("Introduce tu posible número: "))
    intentos +=1
    if intento < numsecre:
        print("El número es más grande que" , intento)
    elif intento > numsecre:
        print("El número es más chico que" , intento)
    else:
        print("¡Felicidades, adivinaste el número en" , intentos, "intentos!")
        break

# Referencias de Python
# https://www.w3schools.com/python/python_ref_functions.asp