print("Por favor, digite 8 números inteiros.")

# Inicializa os contadores
positivos = 0
negativos = 0
zeros = 0

# Loop para receber 8 números
for i in range(8):
    try:
        numero = int(input(f"Digite o {i+1}º número: "))
        
        # Verifica a categoria do número e atualiza o contador correspondente
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        # Se a entrada for inválida, o loop volta para pedir o mesmo número
        # O "i -= 1" é crucial para compensar o incremento do 'for'
        i -= 1

# Exibe o resultado final
print("\n--- Resultado ---")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de zeros: {zeros}")