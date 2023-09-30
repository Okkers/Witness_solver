from app.instantiate_puzzle import create_puzzle
import numpy as np 

if __name__ == "__main__":
    print("input dimensions of the puzzle, in the form '(x,y)':")
    dim_x, dim_y = [int(x) for x in input().split(",")]
    create_puzzle().run()
    