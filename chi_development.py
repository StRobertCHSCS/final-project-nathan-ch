'''
Note: 
Hyperspace is a unique type of space where the game will get slower when bullets are fired because of the framerate issues of VScode therefore, 
There can be only 3 enemies firing bullets at once to maintain a decent framerate however, 2 enemies is essential to maintain 60 fps.  
'''
import arcade
import os
import math
import time
import random
 
WIDTH = 700
HEIGHT = 800
 
# start player position in middle of window
player_x = WIDTH/2
player_y = HEIGHT/2
 
# bullets of player
player_bullet = []
player_bullet_firerate = False
player_bullet_timer = -2
player_bullet_click = 20
 
# enemy player
enemy = []
enemy_two = []
enemy_bullet = []
enemy_lazer = []
enemy_lazer_charging = []
enemy_bullet_timer = -140
enemy_bullet_firerate = 50
enemy_bullet_angle = 0
enemy_healthbar = 40
enemy_color_healthbar = arcade.color.GREEN
enemy_lives = 3
enemy_size_healthbar = 40
random_movement = [[0, 0]]
enemy_lazer_firerate = 50
laser_y = 0
enemy_two_speed = 5
amount_laser_enemies = 9
 
# Variable to record if certain keys are being pressed.
key_pressed = [False] * 4
 
# Colour change when the user hovers over it
button_color = arcade.color.BLUE
 
# Different screens
page = 3
  
 
# Which screen is being displayed (This doesn't work but the first time)
# if page == 0:
#     # Death Screen
#     pass
# elif page == 1:
#     # Main page
#     pass
# elif page == 2:
#     # Controls
#     pass
# elif page == 7:
#     # Win Screen
#     pass
 
 
def dead_draw():
    global button_color
    arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, (255, 255, 255, 5))
    arcade.draw_text("YOU DIED", WIDTH/2 - 250, HEIGHT/2 * 1.5, arcade.color.RED, 100)
    arcade.draw_text(":'(", WIDTH/2 - 100, HEIGHT/2, arcade.color.RED, 200)
    arcade.draw_xywh_rectangle_filled(WIDTH/3 - 30, HEIGHT/6, 300, 200, button_color)
 
 
def home_page_draw():
    arcade.draw_text("Home page", WIDTH/2 - 250, HEIGHT/2 * 1.5, arcade.color.BLUE, 100)


def controls_page_draw():
    
def on_draw():
    arcade.start_render()
    global page
    if page == 0:
        dead_draw()
    elif page == 1:
        home_page_draw()
    elif page == 2:
        controls_page_draw()
    elif page == 7:
        win_screen()
 
 
def on_mouse_press(x, y, button, modifiers):
    global player_x, player_y, player_bullet, player_bullet_firerate, page, button_color
    if page >= 3 and button == arcade.MOUSE_BUTTON_LEFT:
            player_bullet_firerate = True
    elif page == 0 and button == arcade.MOUSE_BUTTON_LEFT:
            if (x > WIDTH/3 - 30 and x < WIDTH/3 - 30 + 300 and
                    y > HEIGHT/6 and y < HEIGHT/6 + 200):
                page = 1
    elif page == 1 and button == arcade.MOUSE_BUTTON_LEFT:
            reset()
            level_one()
            page = 3
 
 
def on_mouse_release(x, y, button, modifiers):
    global player_bullet_firerate, player_bullet_timer, player_bullet_click, page
    if page >= 3 and button == arcade.MOUSE_BUTTON_LEFT:
        player_bullet_timer = -2
        player_bullet_firerate = False
        if player_bullet_click == 20:
            player_bullet_click = -2
 
 
def on_mouse_motion(x, y, dx, dy):
    global button_color, page
    if page == 0:
        if (x > WIDTH/3 - 30 and x < WIDTH/3 - 30 + 300 and
                y > HEIGHT/6 and y < HEIGHT/6 + 200):
            button_color = arcade.color.BLUE_SAPPHIRE
        else:
            button_color = arcade.color.BLUE
 
 
def setup():
    global player_texture, player_bullet_texture, enemy_texture, enemy_bullet_texture, enemy_two_texture, enemy_laser_charging_texture, enemy_laser_firing_texture
    arcade.open_window(WIDTH, HEIGHT, "HYPERSPACE Python Arcade Edition")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)
 
    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release
    window.on_mouse_motion = on_mouse_motion
 
    #Load sprites
    player_texture = arcade.load_texture("images/Player.png")
    player_bullet_texture = arcade.load_texture("images/Bullet.png")
    enemy_texture = arcade.load_texture("images/Enemy.png")
    enemy_bullet_texture = arcade.load_texture("images/Enemy Bullet.png")
    enemy_two_texture = arcade.load_texture("images/Beamer.png")
    enemy_laser_charging_texture = arcade.load_texture("images/Laser Charging.png")
    enemy_laser_firing_texture = arcade.load_texture("images/Laser Firing.png")
 
    arcade.run()
 
 
if __name__ == '__main__':
    setup()