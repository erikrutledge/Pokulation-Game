import arcade

class Arrow(arcade.Sprite):
    """ Instance of an Arrow sprite """

    def __init__(self):
        """ Arrow constructor """

        # Attributes of player and type for the disc.
        self.type = type
        self.image_file_name = (f"Pokulation/assets/sprites/arrow.png")

        # Call the parent
        super().__init__(self.image_file_name, hit_box_algorithm="None")