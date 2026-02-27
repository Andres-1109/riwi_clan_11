def determinarTipoNumero():
    while True:
        try:
            nu = float(input("Escriba un número: "))
            break
        except ValueError:
            print("Solamente puede ingresar números") 
    if nu > 0:
        return("El número es positivo")
    elif nu<0:
        return("El numero es negativo")
    else:
        return("El número es cero")
    

print(determinarTipoNumero())

def clasificacioEdades():
    while True:
        try:
            age= int(input("Escriba la edad a clasificar: "))
        except ValueError:
            print("Ingrese sólo un número entero")
            continue
        if age < 0:
            print("La edad no puede ser negativa")
            continue
        elif age> 130:
            print("La edad debe ser menor a 130")
            continue
        break
    
    if age< 18:
        return("La persona es menor de edad")
    elif 32 >age >=18:
        return("La persona es Joven")
    elif 72>age>=32:
        return("La persona es adulta")
    else:
        return("La persona es anciana")
    
print(clasificacioEdades())