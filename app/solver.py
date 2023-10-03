import numpy as np 
from constraints import grid

class solve_puzzle(grid):
    # inherits grid, start, end 
    def __init__(self, grid, start, end, path_front):
        self.grid = grid
        self.start = start 
        self.end = end
        self.path_front = path_front

    # Find successors for the path
    def successors(self):
        successor_states = []
        
        if self.path_front == self.start: 
            self.grid[self.start] = -3 

        candidate_fronts = [(-1,0),(1,0),(0,-1),(0,1)]
        for ch1, ch2 in candidate_fronts:
            cur_cand = (self.path_front[0]+ch1, self.path_front[1]+ch2)

            if cur_cand[0] == -1 or cur_cand[0] == len(self.grid) or cur_cand[1] == -1 or cur_cand[1] == len(self.grid):
                pass 
            elif self.grid[cur_cand] == -3:
                pass 
            elif cur_cand[0] % 2 != 0 and cur_cand[1] % 2 != 0 :
                pass 
            else:
                new_grid = self.grid.copy()
                new_grid[cur_cand] = -3 

                cand = solve_puzzle(new_grid, self.start, self.end, cur_cand)
                if cand.check_all():
                    successor_states.append(cand)
        return successor_states
    
    def bfs(self):
        queue = [self]

        while len(queue) != 0 :
            cur_grid = queue.pop()
            if cur_grid.constraint_finished(cur_grid.start, cur_grid.end):
                if cur_grid.check_all():
                    return cur_grid
            else:
                successors = cur_grid.successors()
                for successor in successors:
                    queue.append(successor)
        return "No solution found"