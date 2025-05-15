
"""
Platformer Game
"""
import math
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Platformer"


# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5
CHARACTER_SCALING = 0.20

PLAYER_MOVEMENT_SPEED = 15
JUMP_MAX_HEIGHT = 200

PLAYER_X_SPEED = 5
PLAYER_Y_SPEED = 5

PLAYER_SPRITE_IMAGE_CHANGE_SPEED = 1

class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        # Variable to hold our texture for our player
        self.player_list = None
        self.wall_list = None
        self.player_texture = None
        self.player_sprite = None
        self.physics_engine = None

        self.camera = None
        self.player_jump = False
        self.player_start = None
        self.camera_max = 0

        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        self.key_right_pressed = False
        self.key_left_pressed = False

        self.collide = False

        self.player_dy = PLAYER_Y_SPEED
        self.player_dx = PLAYER_X_SPEED

        self.gui_camera = None
        self.score_text = None
        self.total_time = 0

        self.player_sprite_images_r = []

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.player_texture = arcade.load_texture("images/перс для игры1.png")

        # Separate variable that holds the player sprite
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.scale = CHARACTER_SCALING
        self.player_sprite.center_x = 40
        self.player_sprite.center_y = 90

        # SpriteList for our player
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # SpriteList for our boxes and ground
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Create the ground
        for x in range(-300, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Put some crates on the ground
        coordinate_list = [[100, 600], [450, 850], [50, 1000], [300, 1400], [100, 1600], [350, 1800], [100, 2000], [200, 200], [400, 700]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("images/platforma.png", scale=0.5)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        self.camera = arcade.Camera2D()

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        self.gui_camera = arcade.Camera2D()

        for i in range(1, 5):
            self.player_sprite_images_r.append(arcade.load_texture(f"images/перс для игры{i}.png"))


    def on_draw(self):
        """Render the screen."""

        self.clear()
        self.camera.use()

        self.player_list.draw()
        self.wall_list.draw()

        # Within on_draw
        self.gui_camera.use()

        arcade.Text(f"Max Height: {self.camera_max}", x = 0, y = 5).draw()
        arcade.Text(f"Time: {self.total_time_print}", x = 0, y = 20).draw()

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x
        self.camera_max = 0

        if self.player_sprite.center_y - (self.camera.viewport_height / 4) >= self.camera_max:
            screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 4)
            screen_camera_max = self.player_sprite.center_y - (self.camera.viewport_height / 4)
        else:
            screen_center_y = self.camera_max

        if screen_center_x < self.camera.viewport_height / 2:
            screen_center_x = self.camera.viewport_height / 2
        if screen_center_y < self.camera.viewport_height / 2:
            screen_center_y = self.camera.viewport_height / 2

        player_centered = screen_center_x, screen_center_y

        self.camera.position = player_centered

    def player_movement(self):
        if self.collide:
            self.player_dy = 0

        else:
            self.player_dy = PLAYER_Y_SPEED
            self.player_dx = PLAYER_X_SPEED

        if self.key_left_pressed:
            self.player_sprite.center_x -= self.player_dx
        if self.key_right_pressed:
            self.player_sprite.center_x += self.player_dx
            self.player_sprite.texture = self.player_sprite_images_r[int(self.player_sprite.center_x / PLAYER_SPRITE_IMAGE_CHANGE_SPEED) % 4]

        if self.player_jump:
            self.player_sprite.center_y += self.player_dy
            if self.player_sprite.center_y > self.jump_start + JUMP_MAX_HEIGHT:
                self.player_jump = False
        else:
            if self.player_sprite.center_y >= 113:
                self.player_sprite.center_y -= self.player_dy

    def calculate_collision(self):
        self.collide = False

        #for block in self.wall_list:
         #   if block.center_x + block.width / 2 >= self.player_sprite.center_x >= block.center_x - block.width / 2 and \
         #       block.center_y + block.heigth / 2 >= self.player_sprite.center_y - self.player_sprite.height / 2 >= block.center_y - block.heigth / 2:
         #            self.collide = True
        for block in self.wall_list:
            if (self.player_sprite.center_x + self.player_sprite.width / 5 >= block.center_x - block.width / 2 and \
                    self.player_sprite.center_x - self.player_sprite.width / 4 <= block.center_x + block.width / 2) and \
                    (self.player_sprite.center_y + self.player_sprite.height / 2 >= block.center_y - block.height / 2 and \
                            self.player_sprite.center_y - self.player_sprite.height / 2 <= block.center_y + block.height / 2):
                   self.collide = True

    def on_update(self, delta_time):
        """Movement and Game Logic"""
        self.center_camera_to_player()
        self.physics_engine.update()
        self.player_movement()

        if self.player_jump:
            self.collide = False
        else:
            self.calculate_collision()

        self.total_time += delta_time
        ms, sec = math.modf(self.total_time)

        minutes = int(sec) // 60
        seconds = int(sec) % 60
        msec = int(ms * 100)
        self.total_time_print = f"{minutes:02d}:{seconds:02d}:{msec:02d}"

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.ESCAPE:
            self.setup()

        if key == arcade.key.UP or key == arcade.key.W:
           # self.player_sprite.center_y +-50

            self.player_jump = True
            self.jump_start = self.player_sprite.center_y
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.center_y -= 50
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.key_left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.key_right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.key_left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.key_right_pressed = False


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()