def main():
    # escribe tu código abajo de esta línea
    anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheque = int(input("Dame el número de cheques: "))
    saldo = (anterior + ingresos - egresos - (cheque * 13))
    saldof = saldo - (saldo * 0.075)
    print("El saldo final de la cuenta es:", saldof)


if __name__ == '__main__':
    main()
