'''
Note: 
Hyperspace is a unique type of space where the game will get slower when bullets are fired because of the framerate issues of VScode therefore, 
There can be only 3 enemies firing bullets at once to maintain a decent framerate however, 2 enemies is essential to maintain 60 fps.  
'''
import arcade
import os
import math
import time
 
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
enemy_bullet = []
enemy_bullet_timer = -140
enemy_bullet_firerate = 50
enemy_bullet_angle = 0
enemy_healthbar = 40
enemy_color_healthbar = arcade.color.GREEN
enemy_lives = 3
enemy_size_healthbar = 40
 
# Variable to record if certain keys are being pressed.
key_pressed = [False] * 4
 
# Colour change when the user hovers over it
button_color = arcade.color.BLUE
 
# Different screens
page = 3
 

def level_one():
    for enemy_x in range(int(WIDTH/3 - WIDTH/7), WIDTH, int(WIDTH/3)):
        enemy.append([enemy_x, HEIGHT/2 * 1.75, 3])
 
def level_two():
    for enemy_x in range(int(WIDTH/3 - WIDTH/7), WIDTH, int(WIDTH/3)):
        for enemy_y in range(int(HEIGHT/2 + 200), int(HEIGHT/2) + 800, 200):
            enemy.append([enemy_x, enemy_y, 3])
 
 
def level_three():
    pass
 
 
def level_boss():
    global enemy_lives, enemy_size_healthbar, enemy_bullet_firerate, player_x, player_y
    enemy.append([player_x, player_y + 200, 10])
    enemy_lives = 10
    enemy_size_healthbar = 40
    enemy_bullet_firerate = 30
    player_x = WIDTH/2
    player_y = HEIGHT/2 * 0.5
 
 
def reset():
    global enemy, enemy_bullet, enemy_bullet_firerate, enemy_bullet_timer, key_pressed, enemy_healthbar, enemy_color_healthbar, player_x, player_y
    global player_bullet, player_bullet_firerate, player_bullet_timer, player_bullet_click, enemy_lives, enemy_size_healthbar, enemy_bullet_angle
    key_pressed = [False] * 4
    player_x = WIDTH/2
    player_y = HEIGHT/2
    enemy = []
    enemy_bullet = []
    enemy_bullet_timer = -140
    enemy_bullet_firerate = 50
    enemy_bullet_angle = 0
    enemy_lives = 3
    enemy_size_healthbar = 40
    enemy_healthbar = 40
    enemy_color_healthbar = arcade.color.GREEN
    player_bullet = []
    player_bullet_firerate = False
    player_bullet_timer = -2
    player_bullet_click = 20
 
 
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
# elif page == 3:
#       pass  
# elif page == 4:
#     level_two()
# elif page == 5:
#     level_three()
# elif page == 6:
#     level_boss()
# else:
#     # Win Screen
#     pass
 
 
def player_movement():
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
 
 
def constrain_player():
    global player_x, player_y
    # Constrain player to border
    if player_x < 40/2 + 2:
        player_x = 40/2 + 2
    if player_x > WIDTH - (40/2 + 2):
        player_x = WIDTH - (40/2 + 2)
    if player_y < 40/2 + 2:
        player_y = 40/2 + 2
    if player_y > HEIGHT - (40/2 + 2):
        player_y = HEIGHT - (40/2 + 2)
 
 
def bullet_player_firerate():
    global player_bullet_click, player_bullet_firerate, player_bullet, player_bullet_timer
    # Firerate of bullet
    if player_bullet_click < 20:
        player_bullet_click += 1
    if player_bullet_firerate:
        player_bullet_timer += 1
    if player_bullet_timer % 20 == 0 and player_bullet_click == 20:
        player_bullet.append([player_x, player_y])
 
 
def enemy_hit():
    global enemy, player_bullet, enemy_lives, enemy_healthbar, enemy_lives, enemy_size_healthbar, enemy_size_healthbar
    # Player bullet and Hitbox of enemies 
    for bullet_animation in range(len(player_bullet) - 1, -1, -1):
        for hit in range(len(enemy) - 1, -1, -1):
            if (enemy[hit][0] - enemy_size_healthbar/2 - 5 <= player_bullet[bullet_animation][0] <= enemy[hit][0] + enemy_size_healthbar/2 + 5 and 
                enemy[hit][1] - 40/2 - 5 <= player_bullet[bullet_animation][1] <= enemy[hit][1] + 40/2 + 5):
                del player_bullet[bullet_animation]
                player_bullet.append([0, 826])
                enemy[hit][2] -= 1
                if enemy[hit][2] == 0:
                    del enemy[hit]
        player_bullet[bullet_animation][1] += 15
        if player_bullet[bullet_animation][1] > HEIGHT + 25: 
            del player_bullet[bullet_animation]
 
 
def enemy_bullet_and_player_death_by_bullets():
    global enemy_bullet_timer, enemy_bullet_firerate, enemy_bullet, player_x, player_y, page, enemy, enemy_bullet_angle
    # Enemy bullet and Player death by bullets
    enemy_bullet_timer += 1
    if enemy_bullet_timer % enemy_bullet_firerate == 0:
        for i in range(len(enemy) - 1, -1, -1):
            enemy_bullet.append([enemy[i][0], enemy[i][1]])
    for e_bullet in range(len(enemy_bullet) - 1, -1, -1):
        if (player_x - 40/2 - 10 <= enemy_bullet[e_bullet][0] <= player_x + 40/2 + 10 and
                player_y - 40/2 - 10 <= enemy_bullet[e_bullet][1] <= player_y + 40/2 + 10):
                page = 0
        if 3 <= page <= 4:
            enemy_bullet[e_bullet][1] -= 15
            if enemy_bullet[e_bullet][1] < - 25:
                del enemy_bullet[e_bullet]
        elif page == 6:
            for direction in range(len(enemy) - 1, -1, -1):
                x_diff = enemy[direction][0] - player_x
                y_diff = enemy[direction][1] - player_y
                angle = math.atan2(y_diff, x_diff)
                enemy_bullet_angle = math.degrees(angle) - 90
                bullet_change_x = math.cos(angle) * 5
                bullet_change_y = math.sin(angle) * 5
                enemy_bullet[e_bullet][1] -= bullet_change_y
                enemy_bullet[e_bullet][0] -= bullet_change_x

 
def enemy_movement_and_collision_with_player():
    global enemy, page, enemy_size_healthbar
    # Enemy movement and Player hitbox
    for movement in range(len(enemy) - 1, -1, -1):
        if 3 <= page <= 4:
            enemy[movement][0] += 5
            if enemy[movement][0] > WIDTH * 1.5:
                enemy[movement][0] = -300
            enemy[movement][1] -= 2
            if enemy[movement][1] == -22:
                enemy[movement][1] = HEIGHT + (40/2 + 2)
        if (enemy[movement][0] - enemy_size_healthbar/2 - 20 <= player_x <= enemy[movement][0] + enemy_size_healthbar/2 + 20 and
                enemy[movement][1] - 40/2 - 20 <= player_y <= enemy[movement][1] + 40/2 + 20):
            page = 0
 
 
def dead_draw():
    global button_color
    arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, (255, 255, 255, 5))
    arcade.draw_text("YOU DIED", WIDTH/2 - 250, HEIGHT/2 * 1.5, arcade.color.RED, 100)
    arcade.draw_text(":'(", WIDTH/2 - 100, HEIGHT/2, arcade.color.RED, 200)
    arcade.draw_xywh_rectangle_filled(WIDTH/3 - 30, HEIGHT/6, 300, 200, button_color)
 
 
def home_page_draw():
    arcade.draw_text("Home page", WIDTH/2 - 250, HEIGHT/2 * 1.5, arcade.color.BLUE, 100)
    
 
def enemy_player_and_healthbar_draw():
    global enemy, enemy_healthbar, enemy_color_healthbar, enemy_lives, enemy_size_healthbar, enemy_texture
    # Enemy player and Health bar
    for draw in range(len(enemy) - 1, -1, -1):
        scale = 1
        arcade.draw_texture_rectangle(enemy[draw][0], enemy[draw][1], scale * enemy_texture.width, scale * enemy_texture.height, enemy_texture)
 
        # arcade.draw_rectangle_filled(enemy[draw][0], enemy[draw][1], enemy_size_healthbar, 40, arcade.color.RED)
        # arcade.draw_rectangle_outline(enemy[draw][0], enemy[draw][1], enemy_size_healthbar, 40, arcade.color.WHITE, 2)
        if 1/3 * 100 < enemy[draw][2]/enemy_lives * 100 <= 2/3 * 100:
            enemy_color_healthbar = arcade.color.YELLOW
        elif enemy[draw][2]/enemy_lives * 100 <= 1/3 * 100:
            enemy_color_healthbar = arcade.color.RED
        else:
            enemy_color_healthbar = arcade.color.GREEN
        enemy_healthbar = enemy_size_healthbar * enemy[draw][2]/enemy_lives
        arcade.draw_xywh_rectangle_filled(enemy[draw][0] - enemy_size_healthbar/2, enemy[draw][1] + 40/2 + 5, enemy_healthbar, 5, enemy_color_healthbar)
 
 
def enemy_bullet_draw():
    global enemy_bullet, enemy_bullet_angle, enemy_bullet_texture
    # Enemy bullet
    for enemy_bullet_draw in range(len(enemy_bullet)):
        scale = 1
        arcade.draw_texture_rectangle(enemy_bullet[enemy_bullet_draw][0], enemy_bullet[enemy_bullet_draw][1] - 10, scale * enemy_bullet_texture.width, scale * enemy_bullet_texture.height, enemy_bullet_texture, enemy_bullet_angle)
        # arcade.draw_rectangle_filled(enemy_bullet[enemy_bullet_draw][0], enemy_bullet[enemy_bullet_draw][1] - 10, 10, 15, arcade.color.PURPLE, enemy_bullet_angle)
        # arcade.draw_rectangle_outline(enemy_bullet[enemy_bullet_draw][0], enemy_bullet[enemy_bullet_draw][1] - 10, 10, 15, arcade.color.WHITE, 2, enemy_bullet_angle)
        
    
def player_draw():
    global player_x, player_y, player_texture
    # player
    scale = 1
    arcade.draw_texture_rectangle(player_x, player_y, scale * player_texture.width, scale * player_texture.height, player_texture)
 
    # arcade.draw_rectangle_filled(player_x, player_y, 40, 40, arcade.color.GREEN)
    # arcade.draw_rectangle_outline(player_x, player_y, 40, 40, arcade.color.WHITE, 5)
 
def player_bullet_draw():
    global player_bullet, player_bullet_texture
    # player bullet
    for bullet_draw in range(len(player_bullet)):
        scale = 1
        arcade.draw_texture_rectangle(player_bullet[bullet_draw][0], player_bullet[bullet_draw][1] + 10, scale * player_bullet_texture.width, scale * player_bullet_texture.height, player_bullet_texture)
        
        # arcade.draw_rectangle_filled(player_bullet[bullet_draw][0], player_bullet[bullet_draw][1] + 10, 10, 15, arcade.color.BLUE)
        # arcade.draw_rectangle_outline(player_bullet[bullet_draw][0], player_bullet[bullet_draw][1] + 10, 10, 15, arcade.color.WHITE, 2)
 
level_one()
 
def on_update(delta_time):
    global page, enemy
    if len(enemy) == 0:
        page += 1
        print(page)
    if len(enemy) == 0 and page == 4:
        reset()
        level_two()
    elif len(enemy) == 0 and page == 6:
        reset()
        level_boss()
    if page >= 3:
        player_movement()
        constrain_player()
        bullet_player_firerate()
        enemy_hit()
        enemy_bullet_and_player_death_by_bullets()
        enemy_movement_and_collision_with_player()
    
            
def on_draw():
    arcade.start_render()
    global page
    if page == 0:
        dead_draw()
    elif page == 1:
        home_page_draw()
    elif page >= 3:
        enemy_player_and_healthbar_draw()
        enemy_bullet_draw()
        player_draw()
        player_bullet_draw()
        
 
def on_key_press(key, modifiers):
    global key_pressed, page
    if page >= 3:
        if key == arcade.key.W:
            key_pressed[0] = True
        if key == arcade.key.S:
            key_pressed[1] = True
        if key == arcade.key.A:
            key_pressed[2] = True
        if key == arcade.key.D:
            key_pressed[3] = True
 
 
def on_key_release(key, modifiers):
    global key_pressed, page
    if page >= 3:
        if key == arcade.key.W:
            key_pressed[0] = False
        if key == arcade.key.S:
            key_pressed[1] = False
        if key == arcade.key.A:
            key_pressed[2] = False
        if key == arcade.key.D:
            key_pressed[3] = False
 
 
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
    global player_texture, player_bullet_texture, enemy_texture, enemy_bullet_texture
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
 
    arcade.run()
 
 
if __name__ == '__main__':
    setup()