#Escribir un programa que pregunte el nombre del usuario en la consola y un
#número entero e imprima por pantalla en líneas distintas el nombre del usuario
#tantas veces como el número introducido.
Nombre = input("¿Como te llamas?")
Numero = int(input("Dime un numero entero"))
for i in range(Numero):
    print(Nombre)