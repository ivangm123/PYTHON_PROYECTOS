class Ave:
    def __init__(self):
        self.volador = "Volador"


class Pato(Ave):

    def __init__(self):
        super().__init__()
        self.nada = True


    def vuela(self):
        print(f"Vuela pato")


if __name__ == '__main__':
    pato = Pato()
    print(pato.volador)
    pato.vuela()
    print(pato.nada)