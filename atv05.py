while True:
    try:
        # Entrada de dados para a cidade A
        populacao_A = float(input("Digite a população inicial da cidade A: "))
        taxa_crescimento_A = float(input("Digite a taxa de crescimento anual da cidade A (ex: 3.5 para 3.5%): ")) / 100

        # Entrada de dados para a cidade B
        populacao_B = float(input("Digite a população inicial da cidade B: "))
        taxa_crescimento_B = float(input("Digite a taxa de crescimento anual da cidade B (ex: 1.2 para 1.2%): ")) / 100

        # Validação dos valores
        if populacao_A <= 0 or populacao_B <= 0 or taxa_crescimento_A < 0 or taxa_crescimento_B < 0:
            print("ERRO: Todos os valores devem ser positivos. Tente novamente.")
            continue

        anos = 0

        # Lógica do cálculo
        if populacao_A >= populacao_B:
            print("A população da cidade A já é maior ou igual à da cidade B.")
        else:
            while populacao_A < populacao_B:
                populacao_A += populacao_A * taxa_crescimento_A
                populacao_B += populacao_B * taxa_crescimento_B
                anos += 1

            print(f"\nSerão necessários {anos} anos para que a população da cidade A ultrapasse ou iguale a da cidade B.")
            print(f"População final da cidade A: {int(populacao_A)}")
            print(f"População final da cidade B: {int(populacao_B)}")

    except ValueError:
        print("ERRO: Entrada inválida. Por favor, digite apenas números.")
        
    novo_calculo = input("\nDeseja realizar um novo cálculo? (s/n): ").lower()
    if novo_calculo != 's':
        print("Programa encerrado.")
        break