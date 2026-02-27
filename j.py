def sumar(*numeros):
    resultado = 0
    for n in numeros:
        resultado+=n
    return resultado

def restar(*numeros):
    if len(numeros) == 0:
        return "No hay números para restar, gracias"
    
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado-=n
    return resultado

def multiplicar(*numeros):
    resultado = 1
    for n in numeros:
        resultado*=n
    return resultado

def dividir(*numeros):
    resultado= numeros[0]
    for n in numeros[1:]:
        if n==0:
            return "No se puede dividir entre 0"
        resultado/=n
    return resultado

print("""
=====MENÚ=====
1. Suma
2. Resta
3. Multiplicar
4. Dividir                            
      
      """)



while True:
    inicio = (input("¿Qué operación harémos hoy?: "))
    
    if inicio.lower() == "salir":
        print("No tienes escapatoria tienes que continuar")
        continue

    try:
        operacion = int(inicio)
        if 1<= operacion <=4:
            break
        else:
            print("Debe ser un número entre 1 y 4")
    except ValueError:
        print("Error debes ingresar un número entre 1 y 4")

numeros= list()


while True:
    c= (input('Ingrese el número que desea operar o escriba "salir" para obtener su resultado: '))
    if c == "salir":
        break
    else:
        c = float(c)
        numeros.append(c)

numeros= tuple(numeros)

if operacion== 1:
    resultado= sumar(*numeros)
elif operacion ==2:
    resultado= restar(*numeros)
elif operacion ==3:
    resultado= multiplicar(*numeros)
elif operacion==4:
    resultado= dividir(*numeros)

print(resultado)