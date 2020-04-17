from random import sample
import random

def deepCopy(matrix):
    copy = []
    i=0
    for row in matrix:
        copy.append([])
        for col in row:
            copy[i].append(col)
        i += 1
    return copy

def randomTable():
    matrix = [[],[],[],[],[],[],[],[],[]]
    for i in range(1,82):
        matrix[i%9].append(random.randint(1,9))
    return matrix

def zerosTable():
    matrix = [[],[],[],[],[],[],[],[],[]]
    for i in range(81):
        matrix[i//9].append(0)
    return matrix

""" Print legible del tablero """
def tablePrint(matrix):
    print('        0   1   2   3   4   5   6   7   8  ')
    print('      |           |           |           |')
    print('    --+---+---+---+---+---+---+---+---+---+--')
    for row in matrix:
        print('  {}   | {} | {} | {} | {} | {} | {} | {} | {} | {} |'.format(matrix.index(row), row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        if matrix.index(row) in [2,5,8]:
            print('    --+---+---+---+---+---+---+---+---+---+--  ')
        else:
            print('      +---+---+---+---+---+---+---+---+---+  ')
    print('      |           |           |           |')

""" Chequea la viabilidad de la fila """
def availableRow(matrix, value, x, y):
    pass

""" Chequea la viabilidad de la columna """
def availableCol(matrix, value, x, y):
    pass

""" Chequea la viabilidad de la caja """
def availableBox(matrix, value, x, y):
    pass

def checkSudoku(matrix):
    pass

def createSudoku(base=3):
    base  = base  # Will generate any size of random sudoku board in O(n^2) time
    side  = base*base
    nums  = sample(range(1,side+1),side) # obtengo una lista desordenada y luego la repito desfasada en cada fila
    board = [[nums[(base*(r%base)+r//base+c)%side] for c in range(side) ] for r in range(side)]
    """ 
    En las siguientes dos líneas reordeno las filas y columnas, limitándo los cambios a una 
    vecindad dada por la base (recordar algebra lineal)
    """
    rows  = [ r for g in sample(range(base),base) for r in sample(range(g*base,(g+1)*base),base) ]
    cols  = [ c for g in sample(range(base),base) for c in sample(range(g*base,(g+1)*base),base) ]  
    # Dos veces para aleatoriedad
    board = [[board[r][c] for c in cols] for r in rows]
    rows  = [ r for g in sample(range(base),base) for r in sample(range(g*base,(g+1)*base),base) ]
    cols  = [ c for g in sample(range(base),base) for c in sample(range(g*base,(g+1)*base),base) ]           
    board = [[board[r][c] for c in cols] for r in rows]
    return board

if __name__ == "__main__":
    sudoku = createSudoku()
    tablePrint(sudoku)
