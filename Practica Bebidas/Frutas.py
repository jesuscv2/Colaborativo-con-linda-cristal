# Programa que te permite vender bebidas
# Solicita una opcion paraa elegir la bebida
# Pregunta cantidad de bebida
# Muestra total a pagar

print("Aguas de litro el mananteal")
print("---Menu de bebidas---")
print("1.Agua de mango - $40")
print("2.Agua de jamaica - $45")
print("3.Agua de horchata - $35")

opcion=int(input("Elige una opcion del menu: "))
cantidad=int(input("¿cuantos litros quieres?"))

if opcion == 1:
    bebida= "Agua de mango"
    precio= 40
elif opcion == 2:
    bebida = "Agua de jamaica"
    precio = 45
elif opcion == 3:
    bebida = "Agua de horchata"
    precio = 35
else:
    bebida = "Agua no existe"
    precio = 0
if precio>0:
    total = precio = cantidad
