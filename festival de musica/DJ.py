from Artista import Artista

class DJ(Artista):

    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo=estilo

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de {self.estilo}")