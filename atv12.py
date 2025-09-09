# Coleta o número, o início e o fim da tabuada
try:
    numero_tabuada = int(input("Digite o número para a tabuada: "))
    inicio = int(input("Digite o número inicial da tabuada: "))
    fim = int(input("Digite o número final da tabuada: "))
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.")
    exit()

# Garante que o início e o fim estão na ordem correta
if inicio > fim:
    inicio, fim = fim, inicio

print(f"\nTabuada do {numero_tabuada} de {inicio} a {fim}:\n")

# Gera e exibe a tabuada
for i in range(inicio, fim + 1):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")