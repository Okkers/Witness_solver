import numpy as np
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from functools import partial
from callback_functions import callback_buttons, callback_roads, callback_solution

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
        sol_btn.bind(on_press=partial(callback_solution, layout, np_arr, dim_x))

        layout.add_widget(sol_btn)

        layout.row_default_height = layout.minimum_height
        layout.col_default_height = layout.minimum_width
        layout.pos_hint = {"center_x": 0.9, "center_y": 0.3}

        return layout

if __name__ == "__main__":
    print("input dimensions of the puzzle, in the form '(x,y)':")
    dim_x, dim_y = [int(x) for x in input().split(",")]
    create_puzzle().run()