from Cantante import Cantante
from DJ import DJ
from Banda import Banda
from Festival import iniciar_festival


def main():

    lista_artistas=[]

    print("BIENVENIDO AL FESTIVAL MUSICAL")
    print("===================================")

    cantidad=int(input("\nCuantos artistas se presentaran?: "))

    for i in range(cantidad):

        print(f"\nRegistro del artista {i + 1}")

        tipo=input("Tipo de artista (Cantante, DJ o Banda): ").strip().lower()

        nombre=input("Nombre: ")
        genero=input("Genero musical: ")
        popularidad=int(input("Popularidad (1-100): "))

        if tipo=="cantante":

            cancion=input("Cancion mas popular: ")

            artista = Cantante(nombre, genero, popularidad, cancion)

        elif tipo=="dj":

            estilo=input("Estilo musical: ")

            artista = DJ(nombre, genero, popularidad, estilo)

        elif tipo=="banda":

            integrantes=int(input("Numero de integrantes: "))

            artista = Banda(nombre, genero, popularidad, integrantes)

        else:

            print("Tipo de artista no valido")
            continue

        lista_artistas.append(artista)

        print("Artista registrado correctamente")

    iniciar_festival(lista_artistas)


if __name__=="__main__":
    main()