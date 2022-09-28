import numpy as np
import copy

def find_value(M, value):
    row, col = np.where(M==value)
    return row, col

def move_left(M):
    row, col = find_value(M, 0)
    M[row,col] = M[row,col-1]
    M[row,col-1] = 0
    return M

def move_right(M):
    row, col = find_value(M, 0)
    M[row,col] = M[row,col+1]
    M[row,col+1] = 0
    return M

def move_up(M):
    row, col = find_value(M, 0)
    M[row,col] = M[row-1,col]
    M[row-1,col] = 0
    return M

def move_down(M):
    row, col = find_value(M, 0)
    M[row,col] = M[row+1,col]
    M[row+1,col] = 0
    return M

def manhattan_distance(M, M_end):
    h = 0
    for row in range (len(M)):
        for col in range (len(M)):
            row_end, col_end = find_value(M_end, M[row,col])
            h = h + abs(row_end-row) + abs(col_end-col)     
    return h

def misplaced_count(M, M_end):
    h = 0
    for row in range (len(M)):
        for col in range (len(M)):
            if M[row,col] != M_end[row,col]:
                h = h + 1
    return h

def generate_frontier(M, M_end, visited, cost):
    open = []
    if np.allclose(M, M_end):
        print("Matriz já é solução. Fim do jogo.")
    else:
        row, col = find_value(M, 0)
        if (row <= 1):
            M_current = copy.deepcopy(M)
            M_next = move_down(M_current)
            if any(np.array_equal(M_next, i) for i in visited) == False:
                open.append((M_next, cost))
        if (row >= 1):
            M_current = copy.deepcopy(M)
            M_next = move_up(M_current)
            if any(np.array_equal(M_next, i) for i in visited) == False:
                open.append((M_next,cost))
        if (col >= 1):
            M_current = copy.deepcopy(M)
            M_next = move_left(M_current)
            if any(np.array_equal(M_next, i) for i in visited) == False:
                open.append((M_next, cost))
        if (col <= 1):
            M_current = copy.deepcopy(M)
            M_next = move_right(M_current)
            if any(np.array_equal(M_next, i) for i in visited) == False:
                open.append((M_next,cost))
    return open

#---------------------------------------------------------------------------
#   MAIN CODE
#---------------------------------------------------------------------------

# Gera matrizes
M_in = np.matrix('5 8 6; 2 0 7; 1 3 4')
M_end = np.matrix('1 2 3; 4 5 6; 7 8 0')

# Inicializa fronteira e nodos fechados
open = []
visited = []

# Inicializa custo uniforme
cost = 0

# Inicializa primeiro nodo
open.append((M_in, cost))
M = M_in

# Faz primeira iteração
open.sort(key=lambda x:x[1])
M = open.pop(0)[0]
cost = cost + 1
open.append(generate_frontier(M, M_end, visited, cost))
visited.append(M)

while np.allclose(M,M_end) != True:
    open.sort(key=lambda x:x[0][0][1])
    M = open[0][0][0]
    open[0].pop(0)
    cost = cost + 1
    open.append(generate_frontier(M, M_end, visited, cost))
    visited.append(M)

# print(open[0][0][0])
# print(open)
# print(M)
# cost = cost + 1
# open.append(generate_frontier(M, M_end, visited, cost))
# visited.append(M)
    # if cost == 2:
    #     break

# print(open)
# print(visited)
print("Matriz solução encontrada. Fim de Jogo.")
print(M)
#---------------------------------------------------------------------------
#   DEBUG
#---------------------------------------------------------------------------

# print(M_in)
# teste = move_down(M_in)
# print(M_in)

# y = 0

# def teste(x):
#     return x + 1

# print(y)
# z = teste(y)
# print(y)

# biblioteca copy -> funcao deep copy