while True:
    try:
        idade_str = input("Digite a idade (entre 1 e 100 anos): ")
        idade = int(idade_str)
        if 1 <= idade <= 100:
            break
        else:
            print("Erro: A idade deve estar entre 1 e 100 anos.")
    except ValueError:
        print("Erro: Por favor, digite um número válido para a idade.")

while True:
    try:
        salario_str = input("Digite o salário (valor positivo): ")
        salario = float(salario_str)
        if salario > 0:
            break
        else:
            print("Erro: O salário deve ser um valor positivo.")
    except ValueError:
        print("Erro: Por favor, digite um número válido para o salário.")

while True:
    genero = input("Digite o gênero ('f' para feminino, 'm' para masculino, 'o' para outro): ").lower()
    if genero in ['f', 'm', 'o']:
        break
    else:
        print("Erro: Opção de gênero inválida. Use 'f', 'm' ou 'o'.")

while True:
    situacao_empregaticia = input("Digite a situação empregatícia ('e' para empregado, 'd' para desempregado, 'a' para autônomo): ").lower()
    if situacao_empregaticia in ['e', 'd', 'a']:
        break
    else:
        print("Erro: Opção de situação empregatícia inválida. Use 'e', 'd' ou 'a'.")

print("\n--- Informações Válidas ---")
print(input("nome:"))
print("Idade:", idade)
print(f"Salário: R${salario:.2f}")
print("Gênero:", genero.upper())
print("Situação empregatícia:", situacao_empregaticia.upper())