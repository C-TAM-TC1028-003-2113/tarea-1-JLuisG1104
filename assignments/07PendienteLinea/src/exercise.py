def main():
    # escribe tu código abajo de esta línea
    # Aqui estoy pidiendo los datos iniciales
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    # Aqui calculo la pendiente que existe entre el punto 1 y punto 2
    m = (y2 - y1) / (x2 - x1)
    # Aqui muestro el resultado final al usuario
    print("Pendiente:", m)


if __name__ == '__main__':
    main()
