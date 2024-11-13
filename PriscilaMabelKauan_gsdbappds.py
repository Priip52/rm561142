# Implementação do programa em Python que realiza as operações solicitadas

# Entrada de dados: quantidade de dias
n = int(input("Insira a quantidade de dias: "))

# Inicialização de variáveis
total_consumo = 0
dias_meta_cumprida = 0
maior_consumo = None
menor_consumo = None

# Meta de consumo sustentável
meta = 150

# Loop para entrada e processamento dos dados de consumo diário
for i in range(1, n + 1):
    consumo = int(input(f"Insira o consumo do dia {i}: "))
    
    # Contagem dos dias que cumpriram a meta
    if consumo >= meta:
        dias_meta_cumprida += 1
    
    # Soma para cálculo da média
    total_consumo += consumo
    
    # Identificação do maior e menor consumo
    if maior_consumo is None or consumo > maior_consumo:
        maior_consumo = consumo
    if menor_consumo is None or consumo < menor_consumo:
        menor_consumo = consumo

# Cálculo da média de consumo
media_consumo = total_consumo / n

# Impressão do relatório de resultados
dias_nao_cumpriram_meta = n - dias_meta_cumprida

if dias_meta_cumprida == n:
    print("Parabéns! Todos os dias cumpriram a meta de consumo sustentável.")
elif dias_meta_cumprida == 0:
    print("Infelizmente, nenhum dia cumpriu a meta de consumo sustentável.")
else:
    print(f"{dias_meta_cumprida} dias cumpriram a meta e {dias_nao_cumpriram_meta} dias não cumpriram a meta.")

print(f"A média de consumo foi de {media_consumo:.2f} kWh. O maior consumo foi de {maior_consumo} kWh e o menor consumo foi de {menor_consumo} kWh.")
