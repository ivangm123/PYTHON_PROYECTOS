from abc import ABC, abstractmethod



class Model(ABC):

    @property
    @abstractmethod
    def tabla(self):
        pass


    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando {_id} en la tabla {self.tabla}")



class Usuario(Model):
    tabla = "Usuario"
    def guardar(self):

        print(f"Guardando {self.tabla} en BBDD")




if __name__ == '__main__':

    usuario = Usuario()
    usuario.guardar()
    Usuario.buscar_por_id(123)