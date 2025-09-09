# Solicita os dois números inteiros ao usuário
try:
    numero_inicial = int(input("Digite o primeiro número inteiro: "))
    numero_final = int(input("Digite o segundo número inteiro: "))
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.")
    exit()

# Garante que o intervalo seja crescente
if numero_inicial > numero_final:
    numero_inicial, numero_final = numero_final, numero_inicial

# Inicializa a variável para a soma dos números ímpares
soma_impares = 0

# Percorre o intervalo e soma os números ímpares
for numero in range(numero_inicial, numero_final + 1):
    if numero % 2 != 0:  # Verifica se o número é ímpar
        soma_impares += numero

# Exibe o resultado final
print(f"\nA soma de todos os números ímpares no intervalo entre {numero_inicial} e {numero_final} é: {soma_impares}")