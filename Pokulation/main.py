import arcade
import arcade.gui
from constants import *
from game.views.title_screen import TitleView
# from game.views.debugging_screen import DebugView


def main():
    """Main function"""

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = TitleView()
    # start_view = DebugView()
    window.show_view(start_view)

    arcade.run()

if __name__ == "__main__":
    main()