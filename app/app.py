import kivy
 
# It’s required that the base Class
# of your App inherits from the App class.
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button

amt_of_symbols = 38

def callback_roads(button):
    print(button.background_normal)
    if button.background_normal == "imgs/road/blank_road.png":
        if button.height == 20 and button.width == 20:
            button.background_normal = "imgs/road/hexagon.png"
            button.background_down = "imgs/road/hexagon.png"
        elif button.height == 20 and button.width == 100:
            button.background_normal = "imgs/road/hexagon_ong.png"
            button.background_down = "imgs/road/hexagon_ong.png"
        elif button.height == 100 and button.width == 20:
            button.background_normal = "imgs/road/hexagon_down.png" 
            button.background_down = "imgs/road/hexagon_down.png" 
    else:
        button.background_normal = "imgs/road/blank_road.png"
        button.background_down = "imgs/road/blank_road.png"

def callback_buttons(button):
    cur_img = button.background_normal.split("/")[2].split(".")[0]
    cur_img = int(cur_img) + 1 
    if  cur_img > amt_of_symbols:
        cur_img = 1
    print(cur_img)
    button.background_normal = "imgs/block/"+str(cur_img)+".png"
    button.background_down = "imgs/block/"+str(cur_img)+".png"

class MyApp(App):
    def build(self):
        layout = GridLayout(rows = 2*dim_x+1, cols= 2*dim_y+1, row_default_height=40, pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        for i in range(2*dim_x+1):
            for j in range(2*dim_y+1):
                if i % 2 == 0 and j % 2 == 0:
                    h = int(20)
                    w = 20 
                    img = "imgs/road/blank_road.png"

                elif i % 2 == 0:
                    h = 20 
                    w = 100
                    img = "imgs/road/blank_road.png"

                elif j % 2 == 0:
                    h = 100
                    w = 20
                    img = "imgs/road/blank_road.png"
                
                else:
                    h = 100
                    w = 100
                    img = "imgs/block/1.png"

                if h == 100 and w == 100:
                    btn = (Button(text = "",
                                  size_hint_y=None,
                                  size_hint_x=None,
                                  height=h,
                                  width=w,
                                  background_normal = img,
                                  background_down = img))
                    btn.bind(on_press=callback_buttons)
                    layout.add_widget(btn)

                else:
                    btn = (Button(text = "",
                                  size_hint_y=None,
                                  size_hint_x=None,
                                  height=h,
                                  width=w,
                                  background_normal = img,
                                  background_down = img))
                    btn.bind(on_press=callback_roads)

                    layout.add_widget(btn)
                    
        layout.row_default_height = layout.minimum_height
        layout.col_default_height = layout.minimum_width

        return layout


if __name__ == "__main__":
    print("input dimensions of the puzzle:")
    dim_x, dim_y = [int(x) for x in input().split(",")]
    MyApp().run()