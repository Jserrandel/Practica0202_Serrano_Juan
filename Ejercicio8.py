#Escribir un programa que pregunte por consola el precio
#de un producto en euros con dos decimales y muestre
#por pantalla el número de euros y el número de céntimos
#del precio introducido.
Precio = input("¿CUanto vale? ")
print(Precio[:Precio.find('.')], 'euros y', Precio[Precio.find('.')+1:], 'céntimos.')