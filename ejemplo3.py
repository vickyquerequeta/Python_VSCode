# Ejemplo A de colores
color=input("Ingrese un color: ")
if color=="rojo":
    print("El color es primario")
elif color=="azul":
    print("El color es primario")
elif color=="amarillo":
    print("El color es primario")

# Ejemplo B de colores
color=input("Ingrese un color: ")
if color=="rojo" or "azul" or "amarillo":
    print("El color es primario")
else:
    print("El color ingresado no es primario")

# Ejemplo C de colores
color=input("Ingrese un color: ")
if color=="rojo" or "azul" or "amarillo":
    print("El color es primario")
elif color=="naranja" or "violeta" or "verde":
    print("El color es secundario")
else:
    print("El color ingresado no es primario")

# Manipular Mayuscula/Minuscula con Métodos
color=imput("Ingrese un color")
elcolor=color.lower()
print(elcolor)
elcolor=color.upper()
print(elcolor)