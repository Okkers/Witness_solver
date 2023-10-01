import numpy as np
import kivy
# from abc import abstractmethod
# from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from functools import partial
import block_dict
import constraints
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

def callback_solution(layout, arr, button):    
    for indx,i in enumerate(layout.children[::-1][:len(layout.children)-1]):

        print(indx//(2*dim_x+1), indx%(2*dim_x+1))

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
            elif "end" in plc:
                arr[indx//(2*dim_x+1), indx%(2*dim_x+1)] = -10
            elif "roadie" in plc:
                arr[indx//(2*dim_x+1), indx%(2*dim_x+1)] = -3
            else:
                arr[indx//(2*dim_x+1), indx%(2*dim_x+1)] = 0
    print(arr)
    print("--------------")
    heyo = constraints.grid(arr)
    flood = heyo.flood_fill(arr, [5,3])
    out = heyo.constraint_color(arr, [5,3])
    print(flood)
    print(out)
    print("--------------")
    print(arr)

class create_puzzle(App):

    def build(self):
        np_arr = np.full((2*dim_x+1, 2*dim_y+1), 1, dtype = int)

        layout = GridLayout(rows = 2*dim_x+2, cols= 2*dim_y+1, row_default_height=40, pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        for i in range(2*dim_x+1):
            for j in range(2*dim_y+1):
                img = "imgs/road/blank_road.png"
                if i % 2 == 0 and j % 2 == 0:
                    h = int(20)
                    w = 20 
                elif i % 2 == 0:
                    h = 20 
                    w = 100
                elif j % 2 == 0:
                    h = 100
                    w = 20
                else:
                    h = 100
                    w = 100
                    img = "imgs/block/1.png"

                btn = (Button(text = "",
                                size_hint_y=None,
                                size_hint_x=None,
                                height=h,
                                width=w,
                                background_normal = img,
                                background_down = img))

                if h == 100 and w == 100:
                    btn.bind(on_press=callback_buttons)
                else:
                    btn.bind(on_press=callback_roads)
                layout.add_widget(btn)

        sol_btn = Button(text = "Find Solution",
                                size_hint_y=None,
                                size_hint_x=None,
                                height=40,
                                width=20,
                                pos = (400,100))
        sol_btn.bind(on_press=partial(callback_solution, layout, np_arr))

        layout.add_widget(sol_btn)

        layout.row_default_height = layout.minimum_height
        layout.col_default_height = layout.minimum_width
        layout.pos_hint = {"center_x": 0.9, "center_y": 0.3}

        return layout

if __name__ == "__main__":
    print("input dimensions of the puzzle, in the form '(x,y)':")
    dim_x, dim_y = [int(x) for x in input().split(",")]
    create_puzzle().run()