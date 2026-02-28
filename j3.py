
contador = 0
compra = {}


while True:
    nombre = str(input('Ingrese el nombre del producto, escriba "salir" para cerrar el programa: '))
    if nombre.lower() == "salir":
        break
    else:
        contador = contador + 1
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input(f"Ingrese el número de unidades del producto {nombre} que va a llevar: "))
        compra[contador] = {
            "Nombre":nombre,
            "Precio": precio,
            "Cantidad": cantidad
            }
subtotal = 0        
for n in compra:
    subtotal= (compra[n]["Precio"])*(compra[n]["Cantidad"]) + subtotal

total = 0
descuento = 0
if subtotal>= 100000:
    descuento = subtotal*0.1
    total = subtotal - descuento
else:
    descuento = 0
    total = subtotal - descuento

print(f"El subtotal es: {subtotal}")
print(f"El total es: {total}")
print(f"Su descuento fue de: {descuento}")
print(f"Los detalles de su compra son: ")

for n in compra:
    for nn in compra[n]:
        print(compra[n][nn])
    print("====================")
