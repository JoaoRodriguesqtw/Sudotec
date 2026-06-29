#17. Desenvolva um algoritmo que converta temperaturas usando menu.
while True:
    print("\n -- Bem vindo ao conversor de temperaturas-- ")
    print()
    print("-- Digite 1 se você quer converter de Celsius para outra unidade de medida --")
    print("-- Digite 2 se você quer converter de Fahrenheit para outra unidade de medida --")
    print("-- Digite 3 se você quer converter de Kelvin para outra unidade de medida --")
    print("-- Digite 4 para fechar o programa --")
    print()
    li_opcao = int(input("Digite o numero da opção escolhida: "))
    print()

    if li_opcao == 1:

        print("-- Digite 1 se você quer converter de Celsius para Fahrenheit --")
        print("-- Digite 2 se você quer converter de Celsius para Kelvin --")
        print()
        li_segunda_opcao = int(input("Digite o numero da opção escolhida: "))
        print()

        if li_segunda_opcao == 1:

            li_temp_celsius = int(input("digite a temperatura em celcius: "))
            print()
            lf_temp_fahrenheit = (li_temp_celsius * 1.8) + 32
            print(f"{li_temp_celsius} graus Celsius são {lf_temp_fahrenheit} graus Fahrenheit ")

        elif li_segunda_opcao == 2:

            li_temp_celsius = int(input("digite a temperatura em celcius: "))
            print()
            lf_temp_kelvin = (li_temp_celsius + 273.15)
            print(f"{li_temp_celsius} graus Celsius são {lf_temp_kelvin} graus Kelvin ")
    
    elif li_opcao == 2:
        print("-- Digite 1 se você quer converter de Fahrenheit para Celsius  --")
        print("-- Digite 2 se você quer converter de Fahrenheit para Kelvin --")
        print()
        li_segunda_opcao = int(input("Digite o numero da opção escolhida: "))
        print()
        if li_segunda_opcao == 1:

            lf_temp_fahrenheit = float(input("digite a temperatura em Fahrenheit: "))
            print()
            li_temp_celsius = (lf_temp_fahrenheit - 32)/ 1.8
            print(f"{lf_temp_fahrenheit} graus Fahrenheit são {li_temp_celsius} graus Celsius")

        elif li_segunda_opcao == 2:

            lf_temp_fahrenheit = float(input("digite a temperatura em Fahrenheit: "))
            print()
            lf_temp_kelvin = (lf_temp_fahrenheit - 32)/ 1.8 + 273.15
            print(f"{lf_temp_fahrenheit} graus Fahrenheit são {lf_temp_kelvin} graus Kelvin ")

    elif li_opcao == 3:

        print("-- Digite 1 se você quer converter de Kelvin para celsius --")
        print("-- Digite 1 se você quer converter de Kelvin para Fahrenheit --")
        print()
        li_segunda_opcao = int(input("Digite o numero da opção escolhida: "))

        if li_segunda_opcao == 1:

            lf_temp_kelvin = float(input("Digite a temperatura em Kelvin: "))
            print()
            lf_temp_celsius = (lf_temp_kelvin - 273.15)
            print(f"{lf_temp_kelvin} graus Kelvin são {(lf_temp_celsius):.2f} graus Celsius")
        
        elif li_segunda_opcao == 2:
            lf_temp_kelvin = float(input("Digite a temperatura em Kelvin: "))
            print()
            lf_temp_fahrenheit = 1.8 * (lf_temp_kelvin - 273.15) + 32
            print(f"{lf_temp_kelvin} graus Kelvin são {(lf_temp_fahrenheit):.2f} graus Fahrenheit")

    elif li_opcao == 4:
        print("Fechando programa")
        break



