import numpy as np

# Gera matrizes
M_in = np.matrix('5 8 6; 2 0 7; 1 3 4')
M_fim = np.matrix('1 2 3; 4 5 6; 7 8 0')

def find_0(M):
    linha, coluna = np.where(M==0)
    return linha, coluna

def move_esquerda(M):
    linha, coluna = find_0(M)
    if (coluna >= 1):
        M[linha,coluna] = M[linha,coluna-1]
        M[linha,coluna-1] = 0
    else:
        raise Exception("Não é possível mover para a esquerda")
    return M

def move_direita(M):
    linha, coluna = find_0(M)
    if (coluna <= 1):
        M[linha,coluna] = M[linha,coluna+1]
        M[linha,coluna+1] = 0
    else:
        raise Exception("Não é possível mover para a direita")
    return M

def move_cima(M):
    linha, coluna = find_0(M)
    if (linha >= 1):
        M[linha,coluna] = M[linha-1,coluna]
        M[linha-1,coluna] = 0
    else:
        raise Exception("Não é possível mover para cima")
    return M

def move_baixo(M):
    linha, coluna = find_0(M)
    if (linha <= 1):
        M[linha,coluna] = M[linha+1,coluna]
        M[linha+1,coluna] = 0
    else:
        raise Exception("Não é possível mover para baixo")
    return M

M = move_esquerda(M_in)
print(M)


# print(M_in)
# print(M_fim)
