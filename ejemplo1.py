#Prueba de Python en VSCode
print ("Hola comisión 23413")
nombre= "Victoria"
profesion="estudiante avanzada de Lic. en Ciencia Política"
nacimiento=2000
print ("Hola, mi nombre es", nombre, "soy", profesion, "y nací en el año", nacimiento)
print ("Hola mi nombre {}, soy {} y nací en el año {}".format (nombre, profesion, nacimiento))
print (f"Hola mi nombre es {nombre}, soy {profesion}, nací en el año {nacimiento}")

#F-Strings
salarioMensual=5000
salarioDiario=salarioMensual/10
print(f"Mi salario mensual es de {salarioMensual} y mi salario diario es de {salarioDiario}")

#F-Strings formateando: recortar número de decimales
num=1.14
print (f"Formatear el valor con cuatro dígitos: {num: .2f}")
print (f"Imprimir el valor como un porcentaje: {num: .0%}")
print (f"Formato exponencial: {num:e}")