# Dados iniciais
populacao_a = 90000
taxa_crescimento_a = 0.035  # 3.5%
populacao_b = 250000
taxa_crescimento_b = 0.012  # 1.2%
anos = 0

# Loop para calcular o tempo necessário
while populacao_a < populacao_b:
    populacao_a = populacao_a * (1 + taxa_crescimento_a)
    populacao_b = populacao_b * (1 + taxa_crescimento_b)
    anos += 1

# Exibição do resultado
print(f"Serão necessários {anos} anos para que a população da cidade A iguale ou ultrapasse a da cidade B.")