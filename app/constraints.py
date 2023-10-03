import numpy as np 

class grid():
    def __init__(self, arr, start, end):
        self.start = start 
        self.end = end
        self.grid = arr

    checks = [(-1,0), (1,0), (0,-1), (0,1)]

    # Helper function for Flood-Fill
    def is_valid(self, grid, square):
        if square[0] == -1 or square[0] == grid.shape[0] or square[1] == -1 or square[1] == grid.shape[1] or grid[square[0],square[1]] == -3:
            return False
        return True
    
    # Flood-Fill algorithm to find areas of the grid
    def flood_fill(self, grid, square):
        squares_in = []
        check_grid = grid.copy()
        check_grid[square[0],square[1]] = -3
        queue = []
        queue.append(square)
        squares_in.append(square)
        c = "0"
        while len(queue) != 0:
            currPixel = queue.pop()

            posX = currPixel[0]
            posY = currPixel[1]

            if self.is_valid(check_grid, [posX+1,posY]):
                squares_in.append([posX+1, posY])
                check_grid[posX+1, posY] = -3
                queue.append([posX+1, posY])
        
            if self.is_valid(check_grid, [posX,posY+1]):
                squares_in.append([posX,posY+1])
                check_grid[posX, posY+1] = -3
                queue.append([posX, posY+1])

            if self.is_valid(check_grid, [posX-1,posY]):
                squares_in.append([posX-1, posY])
                check_grid[posX-1, posY] = -3
                queue.append([posX-1, posY])

            if self.is_valid(check_grid, [posX,posY-1]):
                squares_in.append([posX, posY-1])
                check_grid[posX, posY-1] = -3
                queue.append([posX, posY-1])

        return squares_in


    # Check if we have made a path from start to finish by overwriting the -5 "start" and -10 "end" numbers.
    def constraint_finished(self, start, end):
        if self.grid[start[0],start[1]] != -5 and self.grid[end[0],end[1]] != -10:
            return True
        return False

    # Check if ...
    def constraint_next_to(self, grid):
        pass

    # Check if 2 or more colors are in the same area by Flood-Fill algorithm
    def constraint_color(self, square):
        const_nums = [2,3,4,5,6,7,8,9,27,28,29,30,31,32,33,34]
        if self.grid[square[0],square[1]] in const_nums: 
            checkers = self.flood_fill(self.grid, square)
            
            if self.constraint_finished(self.start, self.end):
                for new_sq in checkers:
                    if self.grid[new_sq[0], new_sq[1]] in const_nums:
                        if self.grid[new_sq[0], new_sq[1]] != self.grid[square[0],square[1]]:
                            return False 
        return True 
    
    # Check if all dots on the path has been met
    def constraint_hexagon(self, square):
        const_nums = [-1,-2]

        if self.grid[square[0], square[1]] in const_nums: 
            if self.constraint_finished(self.start, self.end):
                return False
            counter = 0
            for x,y in self.checks:
                new_x, new_y = square[0]+x, square[1]+y
                if new_x == -1 or new_y == -1 or new_x == len(self.grid) or new_y == len(self.grid):
                    counter += 1 
                elif self.grid[new_x, new_y] not in [-1,-2,-5,-10,0]:
                    counter += 1 
            if counter > 3:
                return False
         
        return True 
    
    # Check if the Straight tetris piece has been made in the grid 
    def constraint_tetris_straight(self, grid, square):
        const_nums = [18,19,21]
        pass
    
    # Check if the L tetris piece has been made in the grid
    def constraint_tetris_l(self, grid, square):
        const_nums = [11,12,13,14,20]
        pass

    # Check if the square tetris piece has been made in the grid
    def constraint_tetris_square(self, grid, square):
        const_num = 10
        pass 

    # Check if the negative tetris pieces are satisfied
    def constraint_tetris_negative(self, grid, square):
        const_nums = [23,24,25,26]
        pass 

    # Check if every star is paired up in the right colors
    def constraint_star(self, grid, square):
        const_nums = [27,28,29,30,31,32,33,34]
        pass 

    # Check if triangles have been visited the correct amount of times
    def constraint_triangles(self, grid, square):
        const_nums = [36,37,38]
        pass 

    # Check if the negation is satisfied by cancelling out another term
    def constraint_negation(self, grid, square):
        const_num = 35
        pass

    def all_constraints(self, square):
        if self.grid[square[0], square[1]] in [2,3,4,5,6,7,8,9,27,28,29,30,31,32,33,34]:
            if not self.constraint_color(square):
                return False
        if self.grid[square[0], square[1]] in [-1,-2]:
            if not self.constraint_hexagon(square):
                return False
        # ...
        return True
    
    def check_all(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if not self.all_constraints((i,j)):
                    return False
        return True