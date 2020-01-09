import arcade
import os
 
WIDTH = 700
HEIGHT = 800
 
# start player position in middle of window
player_x = WIDTH/2
player_y = HEIGHT/2
 
# Variable to record if certain keys are being pressed.
key_pressed = [False] * 4
 
 
def on_update(delta_time):
    global player_x, player_y
    # The result of a key pressed
    if key_pressed[0]:
        player_y += 5
    if key_pressed[1]:
        player_y -= 5
    if key_pressed[2]:
        player_x -= 5
    if key_pressed[3]:
        player_x += 5
    
    # Constrain player to border
    if player_x < 40/2 + 2:
        player_x = 40/2 + 2
    if player_x > WIDTH - (40/2 + 2):
        player_x = WIDTH - (40/2 + 2)
    if player_y < 40/2 + 2:
        player_y = 40/2 + 2
    if player_y > HEIGHT - (40/2 + 2):
        player_y = HEIGHT - (40/2 + 2)
 
 
def on_draw():
    global player_x, player_y
    arcade.start_render()
 
    arcade.draw_rectangle_filled(player_x, player_y, 40, 40, arcade.color.GREEN)
    arcade.draw_rectangle_outline(player_x, player_y, 40, 40, arcade.color.WHITE, 5)
 
 
def on_key_press(key, modifiers):
    global key_pressed
    if key == arcade.key.W:
        key_pressed[0] = True
    if key == arcade.key.S:
        key_pressed[1] = True
    if key == arcade.key.A:
        key_pressed[2] = True
    if key == arcade.key.D:
        key_pressed[3] = True
 
 
def on_key_release(key, modifiers):
    global key_pressed
    if key == arcade.key.W:
        key_pressed[0] = False
    if key == arcade.key.S:
        key_pressed[1] = False
    if key == arcade.key.A:
        key_pressed[2] = False
    if key == arcade.key.D:
        key_pressed[3] = False
 
def setup():
    arcade.open_window(WIDTH, HEIGHT, "HYPERSPACE Python Arcade Edition")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)
 
    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
 
    arcade.run()
 
 
if __name__ == '__main__':
    setup()

