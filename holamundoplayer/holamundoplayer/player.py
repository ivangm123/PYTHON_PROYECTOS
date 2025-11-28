"""
Esta es el modulo que incluye la clase de reproductor de musica
"""


class Player:
    """
    Esta clase crea un reproductor de musica
    """

    def play(self, song):
        """
        Reproduce la cancion que recibio en el constructor

        Parameters:
        song (str): este es un string con el path de la cancion

        :returns:
        :rtype: int si la cancion se reprodujo correctamente

        """
        print("Reproduciendo cancion")
