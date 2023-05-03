# Uso de break-continue-else
cadena="Hola"
letra=input("Ingrese una letra: ")
for car in cadena:
    if car == letra:
        print("Letra encontrada")
        break
else:
    print("Letra no encontrada")

# Uso de continue
cadena="Hola"
for letra in cadena:
    if letra=="o":
        continue
    print(letra)