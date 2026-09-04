#Almacenar las edades de 6 estudiantes
edades = []

def almacenarEdades(edad):
    edades.append(edad)

def mostarEdades():
    return edades

for i in range(10):
    while True:
        try:
            edad = int(input(f"Estudiante # {i+1}. Dime tu edad: "))
            almacenarEdades(edad)
            break
        except ValueError:
            print("Se debe ingresar un numero entero.")
