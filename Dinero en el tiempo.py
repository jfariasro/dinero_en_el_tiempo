"""Proyecto: Simulador que Calcule el Valor de Dinero en el tiempo"""

while True:
    print("\n*Valor de Dinero en el Tiempo*"
          "\n1. Valor Futuro"
          "\n2. Valor Presente"
          "\n3. Intereses"
          "\n4. Tasa de Interés Real o Paridad de Fisher"
          "\n5. Periodos de Capitalización Y Tasa de Interés Simple")

    opciones = int(input("\n¿Qué Valor deseas Calcular? -> "))
    while (opciones < 1 or opciones > 5):
        opciones = int(input("ERROR!!!!\n¿Qué Valor deseas Calcular? -> "))
    print()

    if (opciones == 1):
        print("Calculando un Valor Futuro, Prohibido Ingresar Numeros Negativos y 0")

        VP = float(input("\nIngresa la Cantidad que tienes el día de hoy: $"))
        while (VP <= 0):
            VP = int(input("ERROR!!!!\nIngresa la Cantidad que tienes el día de hoy: $"))
        intereses = int(input("\nIngrese los Intereses de Anualidad: "))
        while (intereses <= 0):
            intereses = int(input("ERROR!!!!\nIngrese los Intereses de Anualidad: "))
        periodo = int(input("\nIngresa la Cantidad de Años: "))
        while (periodo <= 0):
            periodo = int(input("ERROR!!!!\nIngresa la Cantidad de Años: "))

        i = intereses / 100
        VF = float(VP * (1 + i) ** periodo)
        print(f"\nValor Presente -> ${VP}"
              f"\nIntereses      -> {intereses}%"
              f"\nPeriodo o Años -> {periodo}"
              f"\n\nValor Futuro o Mañana -> ${VF:.2f}")

    if (opciones == 2):
        print("Calculando el Valor Presente, Prohibido los Numeros Negativos y 0")

        VF = float(input("\nQue Valor Planeo tener en un Futuro -> $"))
        while (VF <= 0):
            VF = float(input("ERROR!!!!\nQue Valor Planeo tener en un Futuro -> $"))
        intereses = int(input("\nIngrese los Intereses de Anualidad: "))
        while (intereses <= 0):
            intereses = int(input("ERROR!!!!\nIngrese los Intereses de Anualidad: "))
        periodo = int(input("\nIngresa la Cantidad de Años: "))
        while (periodo <= 0):
            periodo = int(input("ERROR!!!!\nIngresa la Cantidad de Años: "))
        i = intereses / 100
        VP = float(VF / ((1 + i) ** periodo))
        print(f"\nValor Futuro -> ${VF}"
              f"\nIntereses      -> {intereses}%"
              f"\nPeriodo o Años -> {periodo}"
              f"\n\nValor Presente (Hoy) -> ${VP:.2f}")

    if (opciones == 3):
        print("Calculando un Interés con Valor Presente y Valor Futuro Conocidos\n"
              "\nNota: Prohibido Ingresar Numeros Negativos, y Tener en cuenta que el Valor Presente\n"
              "no puede ser mayor o igual al Valor Futuro")

        VP = float(input("\nIngresa la Cantidad que tienes el día de hoy: $"))
        while (VP <= 0):
            VP = int(input("ERROR!!!!\nIngresa la Cantidad que tienes el día de hoy: $"))
        VF = float(input("\nQue Valor Planeo tener en un Futuro -> $"))
        while ((VF <= 0) or (VF <= VP)):
            VF = float(input("ERROR!!!!\nQue Valor Planeo tener en un Futuro -> $"))
        periodo = int(input("\nIngresa la Cantidad de Años: "))
        while (periodo <= 0):
            periodo = int(input("ERROR!!!!\nIngresa la Cantidad de Años: "))

        i = float((VF / VP) ** (1 / periodo) - 1)
        intereses = int(i * 100)
        print(f"\nValor Presente -> ${VP}"
              f"\nValor Futuro   -> ${VF}"
              f"\nPeriodo o Años -> {periodo}"
              f"\n\nIntereses -> {intereses}%")

    if (opciones == 4):
        print("Calculando la Paridad de Fisher")

        interes = int(input("\nDigite la Tasa de Interés: "))
        while (interes <= 0):
            interes = int(input("ERROR!!!!\nDigite la Tasa de Interés: "))
        i = float(interes / 100)

        inflacion = int(input("\nDigite la Tasa de Inflación: "))
        while (inflacion <= 0):
            inflacion = int(input("ERROR!!!!\nDigite la Tasa de Inflación: "))
        infla = float(inflacion / 100)
        _real = float((1 + i) / (1 + infla) - 1)
        real = float(_real * 100)
        print(f"\nTasa de Interés   -> {interes}%"
              f"\nTasa de Inflación -> {inflacion}%"
              f"\n\nInterés Real -> {real:.2f}%")

    if (opciones == 5):
        print("\t___Calculando Periodos de Capitalización___"
              "\n\nCapitalización: Periodos en el año"
              "\nDiaria: 365"
              "\nSemanal: 52"
              "\nMensual 12"
              "\nTrimestral: 4"
              "\nSemestral: 2"
              "\nAnual: 1")
        TAS = float(input("\nDigite el Porcentaje del TAS: "))
        while (TAS <= 0):
            TAS = float(input("ERROR!!!!\nDigite el Porcentaje del TAS: "))
        tas = float(TAS / 100)

        diaria = float((1 + tas / 365) ** 365 - 1)
        semanal = float((1 + tas / 52) ** 52 - 1)
        mensual = float((1 + tas / 12) ** 12 - 1)
        trimestral = float((1 + tas / 4) ** 4 - 1)
        semestral = float((1 + tas / 2) ** 2 - 1)
        anual = float((1 + tas / 1) ** 1 - 1)
        _diaria = float(diaria * 100)
        _semanal = float(semanal * 100)
        _mensual = float(mensual * 100)
        _trimestral = float(trimestral * 100)
        _semestral = float(semestral * 100)
        _anual = float(anual * 100)

        print(f"\nTeniendo un TAS DEL -> {TAS}%"
              f"\n\nObtenemos el TAE:"
              f"\nDIARIA     -> {_diaria:.2f}%"
              f"\nSEMANAL    -> {_semanal:.2f}%"
              f"\nMENSUAL    -> {_mensual:.2f}%"
              f"\nTRIMESTRAL -> {_trimestral:.2f}%"
              f"\nSEMESTRAL  -> {_semestral:.2f}%"
              f"\nANUAL      -> {_anual:.2f}%")

    bandera = input("\nDesea retornar al menú de opciones (S/N): ").upper()
    while(bandera != "S" and bandera != "N"):
        bandera = input("Error!!!!\nDesea retornar al menú de opciones (S/N): ").upper()
    if(bandera == "N"):
        break

print()