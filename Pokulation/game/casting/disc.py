import arcade
from constants import *

class Disc(arcade.Sprite):
    """ Type disc sprite """

    def __init__(self, type):
        """ Disc constructor """

        # Attributes of player and type for the disc.
        self.type = type
        self.image_file_name = (f"Pokulation/assets/sprites/{self.type.lower()}.png")
        self.played_position = None
        self.aim_angle = 0

        # Call the parent
        super().__init__(self.image_file_name, hit_box_algorithm="Detailed")
    
