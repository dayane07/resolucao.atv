# Pede um número inteiro ao usuário
try:
    numero = int(input("Digite um número inteiro positivo: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit()

# Um número perfeito deve ser positivo
if numero <= 0:
    print("Por favor, digite um número inteiro positivo.")
    exit()

# Inicializa a soma dos divisores
soma_divisores = 0

# Percorre os números de 1 até o número - 1
for i in range(1, numero):
    # Verifica se i é um divisor
    if numero % i == 0:
        soma_divisores += i

# Compara a soma dos divisores com o próprio número
if soma_divisores == numero:
    print(f"O número {numero} é um número perfeito!")
else:
    print(f"O número {numero} não é um número perfeito.")