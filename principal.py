# Definindo os classificadores (m = 4) e as classificações para cada objeto (n = 5)
# y_ij representa a classificação do objeto i pelo classificador j
classificacoes = [
    [1, 0, 1, 0],  # Classificações do objeto 1 pelos classificadores M1, M2, M3, M4
    [0, 1, 0, 1],  # Classificações do objeto 2 pelos classificadores M1, M2, M3, M4
    [1, 1, 1, 0],  # Classificações do objeto 3 pelos classificadores M1, M2, M3, M4
    [0, 0, 0, 0],  # Classificações do objeto 4 pelos classificadores M1, M2, M3, M4
    [1, 1, 0, 1]  # Classificações do objeto 5 pelos classificadores M1, M2, M3, M4
]

# Inicializando a lista de classificações finais
resultados_finais = []

# Loop sobre cada objeto
for i in range(len(classificacoes)):  # i varia de 0 a 4 (5 objetos)
    soma_classificacoes = 0

    # Loop sobre cada classificador
    for j in range(len(classificacoes[i])):  # j varia de 0 a 3 (4 classificadores)
        soma_classificacoes += classificacoes[i][j]  # Soma as classificações dos classificadores para o objeto i

    # Decidindo a classificação final com base na soma das classificações
    if soma_classificacoes >= 1:
        y_i = 1
    else:
        y_i = 0

    resultados_finais.append(y_i)  # Adicionando a classificação final do objeto i na lista de resultados finais

# Retornando as classificações finais
print(resultados_finais)  # Deve imprimir: [1, 1, 1, 0, 1]
