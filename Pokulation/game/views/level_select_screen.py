import arcade
from game.views.debugging_screen import DebugView

#----------------------------------------------------------------------------------------------------#  

class LevelView(arcade.View):

    def __init__(self):
        """ This is run once we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("Pokulation/assets/sprites/level_select.png")

    def on_draw(self):
        """ Draw this view"""
        self.clear()
        self.texture.draw_sized(500, 350, 1000, 700)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """ Locate mouse and change view depending on where clicked """
        # LEVEL 1
        if 76 < x < 255 and 412 < y < 588:
            print("Level 1")
            # level_view = Level1View()
            # level_view.setup()
            # self.window.show_view(level_view)
        # LEVEL 2
        elif 300 < x < 478 and 412 < y < 588:
            print("Level 2")
        # LEVEL 3
        elif 523 < x < 701 and 412 < y < 588:
            print("Level 3")
        # LEVEL 4
        elif 745 < x < 926 and  412 < y < 588:
            print("Level 4")
        # LEVEL 5
        elif 76 < x < 255 and 215 < y < 390:
            print("Level 5")
        # LEVEL 6
        elif 300 < x < 478 and 215 < y < 390:
            print("Level 6")
        # LEVEL 7
        elif 523 < x < 701 and 215 < y < 390:
            print("Level 7")
        # LEVEL 8
        elif 745 < x < 926 and 215 < y < 390:
            print("Level 8")
        # LEVEL 9
        elif 76 < x < 255 and 20 < y < 195:
            print("Level 9")
        # LEVEL 10
        elif 300 < x < 478  and 20 < y < 195:
            print("Level 10")
        # LEVEL 11
        elif 523 < x < 701  and 20 < y < 195:
            print("Level 11")
        # LEVEL 12
        elif 745 < x < 926  and 20 < y < 195:
            debug_view = DebugView()
            debug_view.setup()
            self.window.show_view(debug_view)

    def on_key_press(self, symbol: int, modifiers: int):
        """ Perform actions depending on button pressed """
        if symbol == arcade.key.ESCAPE:
            self.window.close()

#----------------------------------------------------------------------------------------------------#