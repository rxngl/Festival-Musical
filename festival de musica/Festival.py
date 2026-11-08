def iniciar_festival(lista_artistas):

    print("FESTIVAL MUSICAL")
    print("=======================\n")

    for artista in lista_artistas:

        artista.presentarse()
        artista.actuar()
        artista.despedirse()

        print("\nFin de la presentacion\n")