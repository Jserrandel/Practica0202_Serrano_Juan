#Escribir un programa que pregunte al usuario la fecha
#de su nacimiento en formato dd/mm/aaaa y muestra por
#pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el
#mes se introduzcan con un solo carácter.
fecha = input("¿Cuando naciste? en este formato dd/mm/aaaa por favor: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])