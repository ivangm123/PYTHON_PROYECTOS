try:
    n1 = int(input(f"Ingresa un numero: "))

except Exception as e:
    print(f"Ocurrio un error")
else:
    print(f"No ocurrio ningun error")
finally:
    print(f"Se ejecuta siempre")