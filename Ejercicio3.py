#Escribir un programa que pregunte el nombre del usuario 
#en la consola y después de que el usuario lo introduzca 
#muestre por pantalla <NOMBRE> tiene <n> letras,
#donde <NOMBRE> es el nombre de usuario en mayúsculas y
#<n> es el número de letras que tienen el nombre.
Nombre = input("¿Cual es tu nombre? ")
letras = len(Nombre.replace(" ", ""))
print(f"{Nombre.upper()} tiene {letras} letras")