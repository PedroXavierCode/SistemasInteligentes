import numpy as np
import copy

# Gera matrizes
M_in = np.matrix('5 8 6; 2 0 7; 1 3 4')
M_end = np.matrix('1 2 3; 4 5 6; 7 8 0')

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

def create_paths(M, M_end):
    open = []
    if np.allclose(M, M_end):
        print("Matriz já é solução. Fim do jogo.")
    else:
        row, col = find_value(M, 0)
        if (row <= 1):
            M_current = copy.deepcopy(M)
            M_next = move_down(M_current)
            open.append(M_next)
        if (row >= 1):
            M_current = copy.deepcopy(M)
            M_next = move_up(M_current)
            open.append(M_next)
        if (col >= 1):
            M_current = copy.deepcopy(M)
            M_next = move_left(M_current)
            open.append(M_next)
        if (col <= 1):
            M_current = copy.deepcopy(M)
            M_next = move_right(M_current)
            open.append(M_next)
    return(open)

#---------------------------------------------------------------------------
#   MAIN CODE
#---------------------------------------------------------------------------

# while np.allclose(M_in,M_end) != True:
#     if np.allclose(M_in,M) == True:
#         M = try_paths(M_in, M_end)
#         print(M)
#     else:
#         M = try_paths(M, M_end)

open = create_paths(M_in,M_end)
print(open)
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