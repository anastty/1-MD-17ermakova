
"""
Platformer Game
"""
from typing import List
import math
import arcade
import arcade.gui

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Platformer"


# Constants used to scale our sprites from their original size
TILE_SCALING = 1
CHARACTER_SCALING = 0.10

PLAYER_MOVEMENT_SPEED = 15
JUMP_MAX_HEIGHT = 200

PLAYER_X_SPEED = 5
PLAYER_Y_SPEED = 5

PLAYER_SPRITE_IMAGE_CHANGE_SPEED = 1

class MainView(arcade.View):
    """
    Main application class.
    """
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__()

        self.camera_max = 0

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


        self.key_right_pressed = False
        self.key_left_pressed = False

        self.collide = False
        self.player_dy = PLAYER_Y_SPEED
        self.player_dx = PLAYER_X_SPEED

        self.gui_camera = None
        self.score_text = None
        self.total_time = 0
        self.player_sprite_images_r = []

        self.tile_map = None
        self.coins = 0
        self.manager = arcade.gui.UIManager()

        switch_menu_button = arcade.gui.UIFlatButton(text="Pause", width=150)

        # Initialise the button with an on_click event.
        @switch_menu_button.event("on_click")
        def on_click_switch_button(event):
            # Passing the main view into menu view as an argument.
            menu_view = MenuView(self)
            self.window.show_view(menu_view)

        # Use the anchor to position the button on the screen.
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="top",
            child=switch_menu_button,
        )

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

    def on_show_view(self):
        """This is run once when we switch to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Enable the UIManager when the view is showm.
        self.manager.enable()

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.background_texture = arcade.load_texture("images/фон для игры.png")

        self.player_texture = arcade.load_texture("images/перс для игры1.png")
        wall = arcade.Sprite("images/перс для игры1.png", scale=1)

        # Separate variable that holds the player sprite
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.scale = CHARACTER_SCALING
        self.player_sprite.center_x = 40
        self.player_sprite.center_y = 220

        # SpriteList for our player
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # SpriteList for our boxes and ground
        #self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Create the ground
        #for x in range(-300, 1250, 64):
        #    wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
        #    wall.center_x = x
        #    wall.center_y = 32
        #    self.wall_list.append(wall)

        # Put some crates on the ground
        #coordinate_list = [[100, 400], [450, 850], [50, 1200], [300, 1500], [100, 1800], [350,2100], [100, 2400], [400, 100], [400, 700]]

       # for coordinate in coordinate_list:
        #    wall = arcade.Sprite("images/platforma.png", scale=0.5)
         #   wall.center_x = coordinate[0]
         #   wall.center_y = coordinate[1]
         #   self.wall_list.append(wall)

        self.camera = arcade.Camera2D()

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        self.gui_camera = arcade.Camera2D()

        for i in range(1, 5):
            self.player_sprite_images_r.append(arcade.load_texture(f"images/перс для игры{1}.png"))

        map_name = "images/map.json"

        layer_options = {
            "platforms": {
                "use_special_hash": True,
            }
        }

        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.wall_list = self.scene["platforms"]


    def on_draw(self):
        """Render the screen."""

        self.clear()
        self.camera.use()

        self.player_list.draw()
        self.scene.draw()

        # Within on_draw

        self.manager.draw()
        self.gui_camera.use()

        arcade.Text(f"Max Height: {self.camera_max}", x = 0, y = 5).draw()
        arcade.Text(f"Time: {self.total_time_print}", x = 0, y = 20).draw()
        arcade.Text(f"Coins: {self.coins}", x = 0, y = 40).draw()

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x


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
        for block in self.scene["platforms"]:
            if (self.player_sprite.center_x + self.player_sprite.width / 5 >= block.center_x - block.width / 2 and \
                self.player_sprite.center_x - self.player_sprite.width / 3 <= block.center_x + block.width / 2) and \
                (self.player_sprite.center_y + self.player_sprite.height / 2 >= block.center_y - block.height / 2 and \
                 self.player_sprite.center_y - self.player_sprite.height / 2 <= block.center_y + block.height / 2):
                    self.collide = True

        for block in self.scene["coins"]:
            if (self.player_sprite.center_x + self.player_sprite.width / 5 >= block.center_x - block.width / 2 and \
                self.player_sprite.center_x - self.player_sprite.width / 3 <= block.center_x + block.width / 2) and \
                (self.player_sprite.center_y + self.player_sprite.height / 2 >= block.center_y - block.height / 2 and \
                 self.player_sprite.center_y - self.player_sprite.height / 2 <= block.center_y + block.height / 2):
                    self.scene["coins"].remove(block)
                    self.coins += 1

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

        if self.coins == 5:
            arcade.exit()

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


class MenuView(arcade.View):
    """Main menu view class."""

    def __init__(self, main_view):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        resume_button = arcade.gui.UIFlatButton(text="Resume", width=150)
        start_new_game_button = arcade.gui.UIFlatButton(text="Start New Game", width=150)
        volume_button = arcade.gui.UIFlatButton(text="Volume", width=150)
        options_button = arcade.gui.UIFlatButton(text="Options", width=150)

        exit_button = arcade.gui.UIFlatButton(text="Exit", width=320)

        # Initialise a grid in which widgets can be arranged.
        self.grid = arcade.gui.UIGridLayout(
            column_count=2, row_count=3, horizontal_spacing=20, vertical_spacing=20
        )

        # Adding the buttons to the layout.
        self.grid.add(resume_button, column=0, row=0)
        self.grid.add(start_new_game_button, column=1, row=0)
        self.grid.add(volume_button, column=0, row=1)
        self.grid.add(options_button, column=1, row=1)
        self.grid.add(exit_button, column=0, row=2, column_span=2)

        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.grid,
        )

        self.main_view = main_view

        @resume_button.event("on_click")
        def on_click_resume_button(event):
            # Pass already created view because we are resuming.
            self.window.show_view(self.main_view)

        @start_new_game_button.event("on_click")
        def on_click_start_new_game_button(event):
            # Create a new view because we are starting a new game.
            main_view = MainView()

            main_view.setup()

            self.window.show_view(main_view)

        @exit_button.event("on_click")
        def on_click_exit_button(event):
            arcade.exit()

        @volume_button.event("on_click")
        def on_click_volume_button(event):
            volume_menu = SubMenu(
                "Volume Menu",
                "How do you like your volume?",
                "Enable Sound",
                ["Play: Rock", "Play: Punk", "Play: Pop"],
                "Adjust Volume",
            )
            self.manager.add(volume_menu, layer=1)

        @options_button.event("on_click")
        def on_click_options_button(event):
            options_menu = SubMenu(
                "Funny Menu",
                "Too much fun here",
                "Fun?",
                ["Make Fun", "Enjoy Fun", "Like Fun"],
                "Adjust Fun",
            )
            self.manager.add(options_menu, layer=1)

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

    def on_show_view(self):
        """This is run once when we switch to this view"""

        # Makes the background darker
        arcade.set_background_color([rgb - 50 for rgb in arcade.color.DARK_BLUE_GRAY])

        # Enable the UIManager when the view is showm.
        self.manager.enable()

    def on_draw(self):
        """Render the screen."""
        # Clear the screen
        self.clear()
        self.manager.draw()

class SubMenu(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    """Acts like a fake view/window."""

    def __init__(
        self,
        title: str,
        input_text: str,
        toggle_label: str,
        dropdown_options: List[str],
        slider_label: str,
    ):
        super().__init__(size_hint=(1, 1))

        # Setup frame which will act like the window.
        frame = self.add(arcade.gui.UIAnchorLayout(width=300, height=400, size_hint=None))
        frame.with_padding(all=20)

        # Add a background to the window.
        # Nine patch smoothes the edges.
        frame.with_background(
            texture=arcade.gui.NinePatchTexture(
                left=7,
                right=7,
                bottom=7,
                top=7,
                texture=arcade.load_texture(
                    ":resources:gui_basic_assets/window/dark_blue_gray_panel.png"
                ),
            )
        )

        back_button = arcade.gui.UIFlatButton(text="Back", width=250)
        # The type of event listener we used earlier for the button will not work here.
        back_button.on_click = self.on_click_back_button

        title_label = arcade.gui.UILabel(text=title, align="center", font_size=20, multiline=False)
        # Adding some extra space around the title.
        title_label_space = arcade.gui.UISpace(height=30, color=arcade.color.DARK_BLUE_GRAY)

        input_text_widget = arcade.gui.UIInputText(text=input_text, width=250).with_border()

        # Load the on-off textures.
        on_texture = arcade.load_texture(
            ":resources:gui_basic_assets/simple_checkbox/circle_on.png"
        )
        off_texture = arcade.load_texture(
            ":resources:gui_basic_assets/simple_checkbox/circle_off.png"
        )

        # Create the on-off toggle and a label
        toggle_label = arcade.gui.UILabel(text=toggle_label)
        toggle = arcade.gui.UITextureToggle(
            on_texture=on_texture, off_texture=off_texture, width=20, height=20
        )

        # Align toggle and label horizontally next to each other
        toggle_group = arcade.gui.UIBoxLayout(vertical=False, space_between=5)
        toggle_group.add(toggle)
        toggle_group.add(toggle_label)

        # Create dropdown with a specified default.
        dropdown = arcade.gui.UIDropdown(
            default=dropdown_options[0], options=dropdown_options, height=20, width=250
        )

        slider_label = arcade.gui.UILabel(text=slider_label)
        pressed_style = arcade.gui.UISlider.UIStyle(
            filled_track=arcade.color.GREEN, unfilled_track=arcade.color.RED
        )
        default_style = arcade.gui.UISlider.UIStyle()
        style_dict = {
            "press": pressed_style,
            "normal": default_style,
            "hover": default_style,
            "disabled": default_style,
        }
        # Configuring the styles is optional.
        slider = arcade.gui.UISlider(value=50, width=250, style=style_dict)

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(title_label)
        widget_layout.add(title_label_space)
        widget_layout.add(input_text_widget)
        widget_layout.add(toggle_group)
        widget_layout.add(dropdown)
        widget_layout.add(slider_label)
        widget_layout.add(slider)

        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="center_x", anchor_y="top")

    def on_click_back_button(self, event):
        # Removes the widget from the manager.
        # After this the manager will respond to its events like it previously did.
        self.parent.remove(self)

def main():
    """Main function"""
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)
    main_view = MainView()
    main_view.setup()
    window.show_view(main_view)
    arcade.run()

if __name__ == "__main__":
    main()