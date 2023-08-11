import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button

# Unique symbols for each block
amt_of_symbols = 38

# Button interaction with path nodes, add hexagon if not there 
# Button interaction with path nodes, add hexagon if not there 
def callback_roads(button):
    pths = ["imgs/road/blank_road.png", "imgs/road/hexagon.png", "imgs/road/hexagon_ong.png", "imgs/road/hexagon_down.png"]

    if button.background_normal == pths[0]:
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

class create_puzzle(App):
    def build(self):
        layout = GridLayout(rows = 2*dim_x+1, cols= 2*dim_y+1, row_default_height=40, pos_hint = {'center_x': 0.5, 'center_y': 0.5})
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

        layout.row_default_height = layout.minimum_height
        layout.col_default_height = layout.minimum_width
        layout.pos_hint = {"center_x": 0.9, "center_y": 0.3}

        return layout

if __name__ == "__main__":
    print("input dimensions of the puzzle, in the form '(x,y)':")
    dim_x, dim_y = [int(x) for x in input().split(",")]
    create_puzzle().run()