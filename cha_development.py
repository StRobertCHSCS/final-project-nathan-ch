import arcade
import os
 
WIDTH = 700
HEIGHT = 800
 
# start player position in middle of window
player_x = WIDTH/2
player_y = HEIGHT/2
 
# Variable to record if certain keys are being pressed.
key_pressed = [False] * 4
 
# bullets of player
player_bullet = []
player_bullet_firerate = False
player_bullet_timer = -2
player_bullet_click = 20
 
enemy = []
enemy_bullet = []
enemy_bullet_timer = -140
enemy_bullet_firerate = 50
enemy_healthbar = 40
enemy_color_healthbar = arcade.color.GREEN
 
def level_one():
    for enemy_x in range(int(WIDTH/3 - WIDTH/7), WIDTH, int(WIDTH/3)):
        enemy.append([enemy_x, HEIGHT/2 * 1.75, 3])
 
 
def level_two():
    pass
 
 
def level_three():
    pass
 
 
def level_boss():
    pass
 
 
level_one()
 
def on_update(delta_time):
    global player_x, player_y, key_pressed, enemy_healthbar, enemy
    global player_bullet, player_bullet_firerate, player_bullet_timer, player_bullet_click
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
 
    # Firerate of bullet
    if player_bullet_click < 20:
        player_bullet_click += 1
    if player_bullet_firerate:
        player_bullet_timer += 1
    if player_bullet_timer % 20 == 0 and player_bullet_click == 20:
        player_bullet.append([player_x, player_y])
 
    # Player bullet and Hitbox of enemies 
    for bullet_animation in range(len(player_bullet) - 1, -1, -1):
        for hit in range(len(enemy) - 1, -1, -1):
            if (enemy[hit][0] - 40/2 - 5 <= player_bullet[bullet_animation][0] <= enemy[hit][0] + 40/2 + 5 and 
                enemy[hit][1] - 40/2 - 5 <= player_bullet[bullet_animation][1] <= enemy[hit][1] + 40/2 + 5):
                del player_bullet[bullet_animation]
                player_bullet.append([0, 826])
                enemy[hit][2] -= 1
                if enemy[hit][2] == 0:
                    del enemy[hit]
        player_bullet[bullet_animation][1] += 15
        if player_bullet[bullet_animation][1] > HEIGHT + 25: 
            del player_bullet[bullet_animation]
 
def on_draw():
    global player_x, player_y, player_bullet, enemy, enemy_healthbar, enemy_color_healthbar
    arcade.start_render()
 
     # Enemy player and Health bar
    for draw in range(len(enemy) - 1, -1, -1):
            arcade.draw_rectangle_filled(enemy[draw][0], enemy[draw][1], 40, 40, arcade.color.RED)
            arcade.draw_rectangle_outline(enemy[draw][0], enemy[draw][1], 40, 40, arcade.color.WHITE, 2)
            if enemy[draw][2] == 2:
                enemy_healthbar = 40 * 2/3
                enemy_color_healthbar = arcade.color.YELLOW
            elif enemy[draw][2] == 1:
                enemy_healthbar = 40 * 1/3
                enemy_color_healthbar = arcade.color.RED
            else:
                enemy_color_healthbar = arcade.color.GREEN
                enemy_healthbar = 40
            arcade.draw_xywh_rectangle_filled(enemy[draw][0] - 40/2, enemy[draw][1] + 40/2 + 5, enemy_healthbar, 5, enemy_color_healthbar)
    
    # player
    arcade.draw_rectangle_filled(player_x, player_y, 40, 40, arcade.color.GREEN)
    arcade.draw_rectangle_outline(player_x, player_y, 40, 40, arcade.color.WHITE, 5)
 
     # player bullet
    for bullet_draw in range(len(player_bullet)):
        arcade.draw_rectangle_filled(player_bullet[bullet_draw][0], player_bullet[bullet_draw][1] + 10, 10, 15, arcade.color.BLUE)
        arcade.draw_rectangle_outline(player_bullet[bullet_draw][0], player_bullet[bullet_draw][1] + 10, 10, 15, arcade.color.WHITE, 2)
 
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
 
 
def on_mouse_press(x, y, button, modifiers):
    global player_x, player_y, player_bullet, player_bullet_firerate, page, button_color
    if button == arcade.MOUSE_BUTTON_LEFT:
        player_bullet_firerate = True
 
 
def on_mouse_release(x, y, button, modifiers):
    global player_bullet_firerate, player_bullet_timer, player_bullet_click, page
    if button == arcade.MOUSE_BUTTON_LEFT:
        player_bullet_timer = -2
        player_bullet_firerate = False
        if player_bullet_click == 20:
            player_bullet_click = -2
 
 
def setup():
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
 
    arcade.run()
 
 
if __name__ == '__main__':
    setup()
