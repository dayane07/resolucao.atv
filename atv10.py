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

# Cria a lista para armazenar os números pares
numeros_pares = []

# Percorre o intervalo e adiciona os números pares à lista
for numero in range(numero_inicial, numero_final + 1):
    if numero % 2 == 0:
        numeros_pares.append(numero)

# Exibe a lista final
if numeros_pares:
    print(f"\nOs números pares no intervalo entre {numero_inicial} e {numero_final} são:")
    print(numeros_pares)
else:
    print(f"\nNão há números pares no intervalo entre {numero_inicial} e {numero_final}.")
