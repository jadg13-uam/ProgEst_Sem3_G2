#Calcular la edad de una persona y decir si es mayor o menor de edad
from datetime import date
from colorama import Fore, Style

try:
    año_nac = int(input("Dime el año en que naciste: "))
    edad = date.today().year - año_nac
    if edad >= 18:
        print("Usted es mayor de edad.")
    else:
        print("Eres menor de edad.")
except ValueError:
    print(Fore.RED + "Ingrese un valor númerico." + Style.RESET_ALL)