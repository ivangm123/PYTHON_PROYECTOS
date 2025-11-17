from abc import ABC, abstractmethod


class Usuario():
    def guardar(self):
        print(f"Guardando Usuario en BBDD")

class Sesion():
    def guardar(self):
        print(f"Guardando Sesion en BBDD")

def guardar(entidades):
    for entidad in entidades:

        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])
