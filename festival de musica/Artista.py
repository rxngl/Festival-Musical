class Artista:

    def __init__(self, nombre, genero, popularidad):
        self.nombre=nombre
        self.genero=genero
        self.popularidad=popularidad

    def presentarse(self):
        print(f"Me presento, soy {self.nombre}, mi género musical es {self.genero}")

    def actuar(self):
        pass

    def despedirse(self):
        print(f"Gracias por su atencion soy {self.nombre}, Hasta pronto")