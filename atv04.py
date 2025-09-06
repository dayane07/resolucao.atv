populacao_A = 90000
taxa_crescimento_A = 0.035  # 3.5%
populacao_B = 250000
taxa_crescimento_B = 0.012  # 1.2%
anos = 0

while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    anos += 1

print(f"Serão necessários {anos} anos para que a população da cidade A ultrapasse ou iguale a da cidade B.")
print(f"População final da cidade A: {int(populacao_A)}")
print(f"População final da cidade B: {int(populacao_B)}")
