print("Por favor, digite 6 números:")

numeros = []
produto = 1
soma = 0

for i in range(6):
    while True:
        try:
            numero = float(input(f"Digite o {i+1}º número: "))
            numeros.append(numero)
            produto *= numero
            soma += numero
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

media = soma / 6

print(f"\nOs números digitados foram: {numeros}")
print(f"O produto de todos os números é: {produto}")
print(f"A média aritmética entre os números é: {media}")