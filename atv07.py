menor_numero = None

for i in range(7):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if menor_numero is None or numero < menor_numero:
        menor_numero = numero

print(f"\nO menor número digitado foi: {menor_numero}")

