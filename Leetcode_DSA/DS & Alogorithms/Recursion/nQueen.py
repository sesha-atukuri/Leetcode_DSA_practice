#Given an integer n, find all possible ways to position n queens on an n×n chessboard
# so that no two queens attack each other. A queen in chess can move horizontally, vertically, or diagonally.

#Do solve the problem using recursion first even if you see some non-recursive approaches.

def nqueens(n):
    solution = []
    chessboard = [None]*n
    col_occupied = [False]*n
    diagnol_occupied = [False]* (2*n-1)
    backslash_diagnoloccupied = [False]*(2*n-1)

    def issafe(row,col):
        return not (col_occupied[col] or diagnol_occupied[row+col] or backslash_diagnoloccupied[row-col+n-1])




    def helper(chessboard,row):
        if row == n:
            solution.append([''.join(row) for row in chessboard])
                #print(solution)
            return

        for col in range(0,n):
            if issafe(row,col):
                chessboard[row] = col
                col_occupied[col] = True
                diagnol_occupied[row + col]  = True
                backslash_diagnoloccupied[row - col + n - 1] = True
                helper(chessboard,row+1)
                col_occupied[col] = False
                diagnol_occupied[row + col] = False
                backslash_diagnoloccupied[row - col + n - 1] = False

    helper(chessboard,0)
    return solution



print(nqueens(4))