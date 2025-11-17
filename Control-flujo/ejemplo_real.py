class Model:
    tabla = None
    def __init__(self):
        if self.tabla is None:
            print(f"Error, la tabla no está definida.")



    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando {_id} en la tabla {self.tabla}")



class Usuario(Model):
    tabla = "Usuario"




if __name__ == '__main__':
    model = Model()
    usuario = Usuario()
    usuario.guardar()
    usuario.buscar_por_id(123)