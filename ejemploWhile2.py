# Deletreo: for para cadenas/listas/
nom=input("Ingrese su nombre: ")
for car in nom:
    print (car)

# Definir variable
texto=str()
nom=input("Ingrese su nombre: ")
for car in nom:
    texto=texto + " " + car
print (texto)

# Quitar guión del principio
texto=str()
nom=input("Ingrese su nombre: ")
for x in nom:
    if texto != "":
        texto = texto + "-" + x
    else:
        texto = texto + x
print (texto)

# Ejemplo de indice - RANGE()
texto = "Hola"
for indice in range (len(texto)):
    print(texto[indice])

# Ejemplo de indice numérico
texto = "Hola"
cc=len(texto)
for indice in range (cc):
    print(texto[cc])