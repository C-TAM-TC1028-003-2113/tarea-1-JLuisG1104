def main():

    import math
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))

    paginas = int(math.ceil(palabras/475))

    costo = (paginas * 60)

    publicacion = costo - (costo * 0.10)

    print("El costo de la publicación es:", publicacion)

if __name__ == '__main__':
    main()
