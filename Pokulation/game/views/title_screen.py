import arcade
from game.views.level_select_screen import LevelView

#----------------------------------------------------------------------------------------------------#  

class TitleView(arcade.View):

    def __init__(self):
        """ This is run once we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("Pokulation/assets/sprites/title_screen.png")

    def on_draw(self):
        """ Draw this view"""
        self.clear()
        self.texture.draw_sized(500, 350, 1000, 700)

    def on_key_press(self, symbol: int, modifiers: int):
        """ Perform actions depending on button pressed """
        if symbol == arcade.key.ENTER:
            # Go to Game View
            level_view = LevelView()
            self.window.show_view(level_view)
        if symbol == arcade.key.ESCAPE:
            self.window.close()

#----------------------------------------------------------------------------------------------------#