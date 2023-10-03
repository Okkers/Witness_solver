import numpy as np
from solver import solve_puzzle
# Unique symbols for each block
amt_of_symbols = 38

# Button interaction with path nodes, add hexagon if not there  
def callback_roads(button):
    pths = ["imgs/road/blank_road.png", "imgs/road/hexagon.png", "imgs/road/hexagon_ong.png", "imgs/road/hexagon_down.png", 
            "imgs/road/start.png", "imgs/road/end.png", "imgs/road/roadie.png"]

    if button.background_normal == pths[1] or button.background_normal == pths[2] or button.background_normal == pths[3]:
        button.background_normal = pths[4]
    elif button.background_normal == pths[4]:
        button.background_normal = pths[5]
    elif button.background_normal == pths[5]:
        button.background_normal = pths[6]
    elif button.background_normal == pths[6]:
        button.background_normal = pths[0]
        
    elif button.background_normal == pths[0]:
        if button.height == 20 and button.width == 20:
            button.background_normal = pths[1]
            button.background_down = pths[1]
        elif button.height == 20 and button.width == 100:
            button.background_normal = pths[2]
            button.background_down = pths[2]
        elif button.height == 100 and button.width == 20:
            button.background_normal = pths[3] 
            button.background_down = pths[3] 
    else:
        button.background_normal = pths[0]
        button.background_down = pths[0]

def callback_buttons(button):
    cur_img = button.background_normal.split("/")[2].split(".")[0]
    cur_img = int(cur_img) + 1 
    if  cur_img > amt_of_symbols:
        cur_img = 1
    button.background_normal = "imgs/block/"+str(cur_img)+".png"
    button.background_down = "imgs/block/"+str(cur_img)+".png"

def callback_solution(layout, arr, dim_x, button):    
    start = (0,0)
    end = (len(arr)-1, len(arr)-1)

    for indx,i in enumerate(layout.children[::-1][:len(layout.children)-1]):

        plc = i.background_normal.split("/")[2].split(".")[0]
        if plc[0].isdigit():
            arr[indx//(2*dim_x+1), indx % (2*dim_x+1)] = plc
        else:
            if "hexagon_" in plc:
                arr[indx//(2*dim_x+1), indx%(2*dim_x+1)] = -1
            elif "hexagon" in plc:
                arr[indx//(2*dim_x+1), indx%(2*dim_x+1)] = -2
            elif "start" in plc:
                arr[indx//(2*dim_x+1), indx%(2*dim_x+1)] = -5
                start = (indx//(2*dim_x+1), indx%(2*dim_x+1))
            elif "end" in plc:
                arr[indx//(2*dim_x+1), indx%(2*dim_x+1)] = -10
                end = (indx//(2*dim_x+1), indx%(2*dim_x+1))
            elif "roadie" in plc:
                arr[indx//(2*dim_x+1), indx%(2*dim_x+1)] = -3
            else:
                arr[indx//(2*dim_x+1), indx%(2*dim_x+1)] = 0

    puzzle = solve_puzzle(arr, start, end, start)

    sol = puzzle.bfs()
    if type(sol) == str:
        print(sol)
    else:
        print(sol.grid)

        for indx,i in enumerate(layout.children[::-1][:len(layout.children)-1]):
            if sol.grid[indx//(2*dim_x+1), indx%(2*dim_x+1)] == -3:
                i.background_normal = "imgs/road/roadie.png"