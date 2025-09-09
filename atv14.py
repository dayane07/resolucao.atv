# Solicita um número inteiro ao usuário
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit()

# Lida com casos especiais: números <= 1 não são primos
if numero <= 1:
    print(f"O número {numero} não é primo.")
else:
    # Assume que o número é primo
    e_primo = True
    # Inicia a verificação a partir de 2
    for i in range(2, numero):
        # Se encontrar um divisor, não é primo
        if numero % i == 0:
            e_primo = False
            break  # Interrompe o loop para otimizar

    # Exibe o resultado com base na verificação
    if e_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")