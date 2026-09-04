#Sumar 2 numeros
def sumar(numero1, numero2):
    return numero1 + numero2

suma = sumar(15, 17)
print(suma)

def restar(numero1 = 0, numero2 = 2):
    return numero1 - numero2

resta = restar(4, 2)
print(resta)
resta = restar(numero2= 6, numero1 = 2)
print(resta)
resta = restar(8)
print(resta)


def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        return "El segundo valor deb ser mayor que 0"

print(multiplicar(4, 2))
print(dividir(20, 5))