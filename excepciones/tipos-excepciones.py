try:
    n1 = int(input(f"Ingresa un numero: "))

except ValueError as e:
    print(f"Ingrese el valor que corresponda")
except NameError as e:
    print(f"Ocurrio un error de asignacion")