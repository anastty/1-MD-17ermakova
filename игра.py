
"""
Platformer Game

python -m arcade.examples.platform_tutorial.03_more_sprites
"""
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Platformer"


# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5
CHARACTER_SCALING = 0.20

PLAYER_MOVEMENT_SPEED = 15

class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self): # __init__, а не init
        # Call the parent class and set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.player_list = None
        self.wall_list = None

        self.player_sprite = None
        self.physics_engine = None

        self.background_color = arcade.csscolor.CORNFLOWER_BLUE


        # Variable to hold our texture for our player
        self.player_texture = arcade.load_texture("images/перс для игры.png")

        # Separate variable that holds the player sprite
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.scale = CHARACTER_SCALING
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 115

        # SpriteList for our player
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # SpriteList for our boxes and ground
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Create the ground
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Put some crates on the ground
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", scale=0.5)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)


        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass


    def on_draw(self):
        """Render the screen."""

        self.clear()

        self.player_list.draw()
        self.wall_list.draw()



    def on_update(self, delta_time):
        """Movement and Game Logic"""

        self.physics_engine.update()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()