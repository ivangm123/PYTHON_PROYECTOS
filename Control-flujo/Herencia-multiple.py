

class Animal:
    def comer(self):
        print(f"comiendo...")



class Perro(Animal):
    def pasear(self):
        print(f"paseando...")



class Chanchito(Perro):

    def programar(self):
        print(f"Programando...")

if __name__ == '__main__':

    chanchito = Chanchito()
    chanchito.pasear()
    chanchito.programar()


    perro = Perro()
    perro.comer()