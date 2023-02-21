# Criando as matrizes
matriz1 = [[3, 1, 3], [6, 5, 5]] # Matriz 2x3
matriz2 = [[100, 50], [50, 100], [50, 50]] # Matriz 3x2
resposta = [[0, 0], [0, 0]] # Matriz 2x2 para armazenar a resposta

# Realizando a multiplicação das matrizes
for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz2)):
            resposta[i][j] += matriz1[i][k] * matriz2[k][j]

# Imprimindo a matriz resposta
for linha in resposta:
    print(linha)
