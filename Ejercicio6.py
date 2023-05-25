"""
Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-PokéBolas. Este problema consiste en ubicar 
n Pokémon en una red de gimnasios de tamaño n x n, sin que los mismos se enfrenten. Recuerda que un Pokémon puede moverse de manera horizontal, vertical y diagonal, además 
podemos ver una solución al problema de los 4 Pokémon. Nótese que una parte importante para resolver un problema es de qué manera representar la solución, para este caso 
particular usamos un vector de n posiciones (gimnasios) y el valor almacenado representa la fila donde se ubica dicho Pokémon.

 
Cuando hayas entendido el problema y tengas una solución en mente, desarrolla un algoritmo que permita hallar al menos una solución para distintas cantidades de Pokémon, 
y luego completa la siguiente tabla.

n-pokeballs / Soluciones distintas / Todas las soluciones / Una solución
1 / 1 / 1 / [0]
2 / 0 / 0 / [NA]
3 / 0 / 0 / [NA]
4 / 1 / 2 / [1, 4, 0, 3]
5 / 2 / 10 / [0, 0, 1, 3, 0]
6 / 1 / 4 / []
7 / 6 / 40 / []
8 / 12 / 92 / []
9 / 46 / 352 / []
10 / 92 / 724 / []
15 / 285 053 / 2 279 184 / []
"""


# def solve_n_pokeballs(n):
#     def is_valid(board, row, col):
#         # Verifica si es una posición válida para colocar un Pokémon
#         for i in range(row):
#             if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
#                 return False
#         return True

#     def backtrack(board, row):
#         # Caso base: cuando hemos ubicado todos los Pokémon
#         if row == n:
#             return [board]

#         solutions = []
#         for col in range(n):
#             if is_valid(board, row, col):
#                 board[row] = col
#                 solutions.extend(backtrack(board, row + 1))
#                 board[row] = -1  # Reiniciamos la posición

#         return solutions

#     # Inicializar el tablero con valores no válidos (-1)
#     board = [-1] * n

#     # Llamar a la función de backtracking para obtener todas las soluciones
#     all_solutions = backtrack(board, 0)

#     # Devolver la cantidad de soluciones distintas, todas las soluciones y una solución
#     distinct_solutions = len(all_solutions)
#     all_solutions = [[row + 1 for row in solution] for solution in all_solutions]
#     one_solution = all_solutions[0] if distinct_solutions > 0 else []

#     return distinct_solutions, all_solutions, one_solution
# table = [
#     (1, *solve_n_pokeballs(1)),
#     (2, *solve_n_pokeballs(2)),
#     (3, *solve_n_pokeballs(3)),
#     (4, *solve_n_pokeballs(4)),
#     (5, *solve_n_pokeballs(5)),
#     (6, *solve_n_pokeballs(6)),
#     (7, *solve_n_pokeballs(7)),
#     (8, *solve_n_pokeballs(8)),
#     (9, *solve_n_pokeballs(9)),
#     (10, *solve_n_pokeballs(10)),
#     (15, *solve_n_pokeballs(15))
# ]

# # Imprimir la tabla
# print("n-pokeballs / Soluciones distintas / Todas las soluciones / Una solución")
# for row in table:
#     print(f"{row[0]} / {row[1]} / {row[2]} / {row[3]}")






















def isSafe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col, n):
    # base case: If all Pokemon are placed
    # then return true
    if col >= n:
        return True

    # Consider this column and try placing
    # this Pokemon in all rows one by one
    for i in range(n):

        if isSafe(board, i, col, n):
            # Place this Pokemon in board[i][col]
            board[i][col] = 1

            # recur to place rest of the Pokemon
            if solveNQUtil(board, col + 1, n):
                return True

            # If placing Pokemon in board[i][col
            # doesn't lead to a solution, then
            # remove queen from board[i][col]
            board[i][col] = 0

    # if the Pokemon can not be placed in any row in
    # this colum col then return false
    return False

def solveNQ(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solveNQUtil(board, 0, n):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

def printSolution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()

# test
solveNQ(4)
