import arcade
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Pokulation"
DISC_RADIUS = 33
OBJECT_SCALE = 1
OFFSCREEN_X = -100
OFFSCREEN_Y = -100

STARTING_VELOCITY = 400
DELTA_TIME = 1/60

COIN_DROP = arcade.load_sound("Pokulation/assets/sounds/coin_drop.wav")
BEEP_1 = arcade.load_sound("Pokulation/assets/sounds/short_beep_1.wav")
BEEP_2 = arcade.load_sound("Pokulation/assets/sounds/short_beep_2.wav")
BEEP_3 = arcade.load_sound("Pokulation/assets/sounds/short_beep_3.wav")
POP = arcade.load_sound("Pokulation/assets/sounds/short_pop.wav")
CLICK = arcade.load_sound("Pokulation/assets/sounds/click.wav")

#           0           1          2        3          4       5       6       7        8
TYPES = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel",
        "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"]
#         9       10        11        12        13         14      15       16       17

# Create a dictionary to reference super effective moves.
SUPER_EFFECTIVE = {
    "Normal":   ["Nothing"],
    "Fighting": ["Normal", "Rock", "Steel", "Ice", "Dark"],
    "Flying":   ["Fighting", "Bug", "Grass"],
    "Poison":   ["Grass", "Fairy"],
    "Ground":   ["Poison", "Rock", "Steel", "Fire", "Electric"],
    "Rock":     ["Flying", "Bug", "Fire", "Ice"],
    "Bug":      ["Grass", "Psychic", "Dark"],
    "Ghost":    ["Ghost", "Psychic"],
    "Steel":    ["Rock", "Ice", "Fairy"],
    "Fire":     ["Bug", "Steel", "Grass", "Ice"],
    "Water":    ["Ground", "Rock", "Fire"],
    "Grass":    ["Ground", "Rock", "Water"],
    "Electric": ["Flying", "Water"],
    "Psychic":  ["Fighting", "Poison"],
    "Ice":      ["Flying", "Ground", "Grass", "Dragon"],
    "Dragon":   ["Dragon"],
    "Dark":     ["Ghost", "Psychic"],
    "Fairy":    ["Fighting", "Dragon", "Dark"]
} 
#----------------------------------------------------------------------------------------------------#

class CalculateVelocity():

    def get_x_velocity_from_angle(self, angle, velocity=STARTING_VELOCITY):
        """ Transforms an angle input into an x velocity """
        # Check which quadrant it is in then adjust accordingly
        if angle == 0 or angle == 180:
            x_velocity = 0
        elif angle == 90:
            x_velocity == velocity
        elif angle == -90:
            x_velocity == -velocity
        elif 0 < angle < 90:
            x_velocity = velocity * math.sin(math.radians(angle))
        elif 90 < angle < 180:
            x_velocity = velocity * math.cos(math.radians(angle - 90))
        elif -90 < angle < 0:
            x_velocity = -velocity * math.cos(math.radians(angle + 90))
        elif -180 < angle < -90:
            x_velocity = - velocity * math.sin(math.radians(angle + 180))
        else:
            return print("There was an error locating the input angle.")
        return x_velocity


    def get_y_velocity_from_angle(self, angle, velocity=STARTING_VELOCITY):
        """ Transforms an angle input into a y velocity """
        # Check which quadrant it is in then adjust accordingly
        if angle == 90 or angle == -90:
            y_velocity = 0
        elif angle == 0:
            y_velocity = velocity
        elif angle == 180:
            y_velocity = -velocity
        elif 0 < angle < 90:
            y_velocity = velocity * math.cos(math.radians(angle))
        elif 90 < angle < 180:
            y_velocity = -velocity * math.sin(math.radians(angle - 90))
        elif -90 < angle < 0:
            y_velocity = velocity * math.sin(math.radians(angle + 90))
        elif -180 < angle < -90:
            y_velocity = -velocity * math.cos(math.radians(angle + 180))
        else:
            return print("There was an error locating the input angle.")
        return y_velocity