import arcade
from constants import *
from game.casting.disc import Disc
from game.casting.arrow import Arrow

#----------------------------------------------------------------------------------------------------#  

class DebugView(arcade.View):
    """
    The Debugging View with all the actions and scripts.
    """
    def __init__(self):

        super().__init__()   # Call the parent class and set up the window
        arcade.set_background_color(arcade.csscolor.BISQUE)    # Set the background color of the window
        self.physics_engine = arcade.PymunkPhysicsEngine()    # Create the physics engine

        self.mouse_pos = (0,0)    # Sprite list to save the location of the mouse
        self.disc_list = None    # List for a Sprite List to hold all the type discs
        self.new_sprite_list = None    # List to append discs in play to
        self.arrow_list = None    # Sprite list for the arrow image
        self.border_sprites = None
        self.environment_list = None   # Sprite list for the level sprites
        self.held_disc = None    # Initialize a list to add pieces to while we move them with the mouse
        self.held_disc_original_position = None    # Original location of the discs we are dragging incase they are placed in an invalid position


    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.simluation_state = False    # Initialize the simulation state bool to flip when prompted
        self.held_disc = []    # Initialize the list of discs being moved with the mouse
        self.held_disc_original_position = []    # Initialize the list to hold the original location of the discs

        self.uimanager = arcade.gui.UIManager()    # Create a UI manager to handle the UI
        self.uimanager.enable()
        self.start_button = arcade.gui.UIFlatButton(text="Start!", width= 100)    # Create the start button and add it to the UI manager
        self.uimanager.add(arcade.gui.UIAnchorWidget(anchor_x= "right", anchor_y= "bottom", align_x= -10, align_y= 25, child= self.start_button))
        self.start_button.on_click = self.on_buttonclick    # Assign the button to the on_button_click() function

        # Sprite list for the player zone on the left side of the screen
        self.environment_list = arcade.SpriteList()
        player_zone = arcade.SpriteSolidColor(200, 600, arcade.csscolor.WHEAT)
        player_zone.position = (100, 400)
        self.environment_list.append(player_zone)
        # Sprite for the bottom menu bar
        task_bar = arcade.SpriteSolidColor(1000, 100, arcade.csscolor.SLATE_GREY)
        task_bar.position = (500, 50)
        self.environment_list.append(task_bar)
        # Sprites for the border box
        self.border_sprites = arcade.SpriteList()
        top = arcade.SpriteSolidColor(SCREEN_WIDTH, 2, arcade.csscolor.BLACK)
        top.position = (SCREEN_WIDTH/2, SCREEN_HEIGHT)
        left = arcade.SpriteSolidColor(2, SCREEN_HEIGHT, arcade.csscolor.BLACK)
        left.position = (0, SCREEN_HEIGHT/2)
        bottom = arcade.SpriteSolidColor(SCREEN_WIDTH, 2, arcade.csscolor.BLACK)
        bottom.position = (SCREEN_WIDTH/2, 100)
        right = arcade.SpriteSolidColor(2, SCREEN_HEIGHT, arcade.csscolor.BLACK)    
        right.position = (SCREEN_WIDTH, SCREEN_HEIGHT/2)    
        self.border_sprites.append(top)
        self.border_sprites.append(left)
        self.border_sprites.append(bottom)
        self.border_sprites.append(right)

        # Create a Sprite List and a Sprite for each type disc
        self.disc_list = arcade.SpriteList()
        for type in TYPES:
            disc = Disc(type)
            disc.position = (TYPES.index(type) * 47 + 50, 50) 
            self.disc_list.append(disc)

        # Sprite List for all the aiming arrows 
        self.arrow_list = arcade.SpriteList()
        for i in range(len(TYPES)):
            arrow = Arrow()
            arrow.position = (OFFSCREEN_X, OFFSCREEN_Y)
            self.arrow_list.append(arrow)

        # Sprite list for only the simulated discs
        self.new_sprite_list = arcade.SpriteList()


        def disc_collision_handler(disc_1, disc_2, arbiter, space, data):
            """ Called when 2 discs collide """
            type_1 = disc_1.type
            type_2 = disc_2.type
            type_1_super_effective = SUPER_EFFECTIVE.get(type_1)
            type_2_super_effective = SUPER_EFFECTIVE.get(type_2)

            if type_1 in type_2_super_effective:
                arcade.play_sound(POP,volume=.8)
                print("Object Removed")
                self.physics_engine.remove_sprite(disc_1)
                disc_1.remove_from_sprite_lists()
            elif type_2 in type_1_super_effective:
                arcade.play_sound(POP,speed=1.5)
                print("Object Removed")
                self.physics_engine.remove_sprite(disc_2)
                disc_2.remove_from_sprite_lists()
            else:
                arcade.play_sound(CLICK,speed=2)
                print("Non-effective Collision")
            return True
        self.physics_engine.add_collision_handler("disc", "disc", begin_handler=disc_collision_handler)

        def wall_disc_collision_handler(wall, disc, arbiter, space, data):
            """ Called when a disc bumps the wall """
            arcade.play_sound(CLICK,speed=2)
            print("Wall Bounce")
            return True
        self.physics_engine.add_collision_handler("disc", "wall", begin_handler=wall_disc_collision_handler)

        # Add the border sprites to the physics engine
        self.physics_engine.add_sprite_list(self.border_sprites, body_type=arcade.PymunkPhysicsEngine.STATIC, 
                                            collision_type="wall", elasticity=1)


    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.environment_list.draw()    # Draw the environments elements
        self.uimanager.draw()    # Draw the ui manager
        self.disc_list.draw()    # Draw the type discs
        self.new_sprite_list.draw()
        self.border_sprites.draw()
        self.arrow_list.draw()    

    def on_update(self, delta_time):
        if self.simluation_state == True:    # Check if the simulation state is set to true either by button press or ENTER key

            self.physics_engine.step()   # Step the physics engine one frame forward (60 fps)
            # self.physics_engine.resync_sprites()

            # Check for boundary collisions
            for disc in self.new_sprite_list:
                if disc.center_x < 0 + DISC_RADIUS or disc.center_x > SCREEN_WIDTH - DISC_RADIUS:
                    self.y_velocity *= -1
                elif disc.center_y < 100 + DISC_RADIUS or disc.center_y > SCREEN_HEIGHT - DISC_RADIUS:
                    self.x_velocity *= -1


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves the mouse. """
        self.mouse_pos = x, y
        
        # If we are holding a disc, move them with the mouse
        for disc in self.held_disc:
            disc.center_x += dx
            disc.center_y += dy

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        if self.simluation_state == True:    # Check if the simulation is running and ignore mouse presses if true
            pass
        else:
            discs = arcade.get_sprites_at_point((x,y), self.disc_list)    # Get disc we click on
            if len(discs) == 0:    # If there are no discs being held
                if  not 890 < x < 990 and not 25 < y < 75:    # Check if clicking on the start button, !don't update angle when clicking start!
                    arrow = self.arrow_list[self.held_type_index]
                    disc = self.disc_list[self.held_type_index]
                    arrow.face_point(self.mouse_pos)    # Face the arrow sprite towards the mouse
                    arrow.played_position = (arrow.center_x, arrow.center_y)    # Get the angle from the center of the disc to the mouse
                    disc.aim_angle = arcade.get_angle_degrees(arrow.played_position[0], arrow.played_position[1], self.mouse_pos[0], self.mouse_pos[1])
                    print(f"Aim Angle: {disc.aim_angle}")
                    arcade.play_sound(BEEP_3)
            
            else:
                primary_disc = discs[-1]    # Select the top most disc if clicking on a stack of more than one
                self.held_disc = [primary_disc]    # In all other cases, grab the disc we click on
                self.held_disc_original_position = [self.held_disc[0].position]    # Save the new valid position

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """ Called when the user releases a mouse press"""

        if self.simluation_state == True:    # Check if the simulation is running and ignore mouse releases if true
            pass
        else:
            if len(self.held_disc) == 0:    # If we don't have any type discs held, do nothing
                return
            
            self.held_type = self.held_disc[0].type    # Check what piece is being held
            self.held_type_index = TYPES.index(self.held_type)    # Save the index number of what piece is being held

            reset_position = True

            # Are you over the play area?
            if arcade.check_for_collision(self.held_disc[0], self.environment_list[0]):
                # Are you within the screen boundary?
                if 0 + DISC_RADIUS < self.held_disc[0].center_x < SCREEN_WIDTH - DISC_RADIUS and 0 + DISC_RADIUS < self.held_disc[0].center_y < SCREEN_HEIGHT - DISC_RADIUS:
                    # Are you not making contact with any other pieces?
                    if not arcade.check_for_collision_with_list(self.held_disc[0], self.disc_list):
                        reset_position = False    # Don't reset the position if the location is valid
                        print(self.disc_list[self.held_type_index].played_position)
                        self.disc_list[self.held_type_index].played_position = self.held_disc[0].position    # Save the positions of sprites as they move
                        print(f"Type: {self.held_type}, Position: {self.disc_list[self.held_type_index].played_position}")
                        self.arrow_list[self.held_type_index].position = self.held_disc[0].position    # Set an arrow sprite in the center of the disc sprite
                        arcade.play_sound(COIN_DROP)
                    else:
                        arcade.play_sound(BEEP_2)
                else:
                    arcade.play_sound(BEEP_2)
            else:
                arcade.play_sound(BEEP_2)

            if reset_position:    # Bring the disc back to it's starting position if the placement isn't valid.
                self.held_disc[0].position = self.held_disc_original_position[0]

            self.held_disc = []    # Clear the list when nothing is being held

    def on_key_press(self, symbol: int, modifiers: int):
        """ Run when the user presses a key """
        if symbol == arcade.key.R:
            if self.simluation_state == False:
                self.setup()    # Restart
            elif self.simluation_state == True:
                self.simluation_state == False
        elif symbol == arcade.key.ESCAPE:
            self.window.close()    # Close the window
        elif symbol == arcade.key.ENTER:
            self.start_simulation()

    def on_buttonclick(self, event):
        self.start_simulation()


    def is_super_effective(self, obj_1, obj_2):
        """ Takes the input of 2 discs and compares them to the TYPE dictionary. """
        type_1 = TYPES[obj_1]
        type_2 = TYPES[obj_2]

        type_1_strengths = SUPER_EFFECTIVE.get(type_1)
        type_2_strengths = SUPER_EFFECTIVE.get(type_2)

        if type_2 in type_1_strengths:
            return print("First object is super effective against the second.")
        elif type_1 in type_2_strengths:
            return print("The second object is super effective against the first.")
        else:
            return print("Neither object has much effect. They bounce off.")



    def start_simulation(self):

        if self.simluation_state == False:
            self.start_button.text = "Stop!"
            for disc in self.disc_list:
                if disc.played_position != None:
                    self.new_sprite_list.append(disc)
            print(len(self.new_sprite_list))
            self.disc_list.clear()
            self.arrow_list.clear()

            for disc in self.new_sprite_list:
                    disc.change_x = CalculateVelocity.get_x_velocity_from_angle(self, disc.aim_angle)   # Calculate the velocity in the x axis from the angle
                    disc.change_y = CalculateVelocity.get_y_velocity_from_angle(self, disc.aim_angle)   # Calculate the velocity in the y axis from the angle
                    self.x_velocity = disc.change_x
                    self.y_velocity = disc.change_y
                    self.physics_engine.add_sprite(disc, mass=0.1, friction=0.6, elasticity=1, damping=1, 
                                                         gravity=(0,0), body_type=arcade.PymunkPhysicsEngine.DYNAMIC, 
                                                         collision_type="disc", max_velocity=STARTING_VELOCITY)     
                    self.physics_engine.apply_impulse(disc, (self.x_velocity, self.y_velocity))
            
            self.simluation_state = True
        else:
            self.setup()
