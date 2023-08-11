### Create board
import numpy as np

# Implement input for board (Assumption being a square)

def create_board(n,m):
    board = np.full((2*n+1,2*m+1), "w")

    for i in range(0,len(board),2):
        board[i,:] = "p"
        
    for i in range(0, len(board[1]), 2):
        board[:,i] = "p"
    board[len(board)-1,:] = "p"
    board[:,len(board[1])-1] = "p"

    print(board)


create_board(1,4)



