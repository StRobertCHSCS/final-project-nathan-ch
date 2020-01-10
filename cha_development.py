'''
Note: 
Hyperspace is a unique type of space where the game will get slower when bullets are fired because of the framerate issues of VScode therefore, 
There can be only 3 enemies firing bullets at once to maintain a decent framerate however, 2 enemies is essential to maintain 60 fps.  
'''
import arcade
import os

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
enemy_healthbar = 40
enemy_color_healthbar = arcade.color.GREEN

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
    pass


def level_three():
    pass


def level_boss():
    pass

def reset():
    global enemy, enemy_bullet, enemy_bullet_firerate, enemy_bullet_timer, key_pressed, enemy_healthbar, enemy_color_healthbar, player_x, player_y
    global player_bullet, player_bullet_firerate, player_bullet_timer, player_bullet_click
    player_x = WIDTH/2
    player_y = HEIGHT/2
    enemy = []
    enemy_bullet = []
    enemy_bullet_timer = -140
    enemy_bullet_firerate = 50
    key_pressed = [False] * 4
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
#     reset()
#     level_one()
# elif page == 4:
#     level_two()
# elif page == 5:
#     level_three()
# elif page == 6:
#     level_boss()
# else:
#     # Win Screen
#     pass

level_one()

def on_update(delta_time):
    global key_pressed, player_y, player_x, player_bullet, player_bullet_firerate, player_bullet_timer, player_bullet_click, enemy, enemy_bullet_timer
    global enemy_bullet, enemy_bullet_firerate, page, enemy_healthbar, enemy_color_healthbar
    if page == 3:
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
        
        # Enemy bullet and Player death by bullets
        enemy_bullet_timer += 1
        if enemy_bullet_timer % enemy_bullet_firerate == 0:
            for i in range(len(enemy) - 1, -1, -1):
                enemy_bullet.append([enemy[i][0], enemy[i][1]])
        for e_bullet in range(len(enemy_bullet) - 1, -1, -1):
            enemy_bullet[e_bullet][1] -= 15
            if (player_x - 40/2 - 10 <= enemy_bullet[e_bullet][0] <= player_x + 40/2 + 10 and
                    player_y - 40/2 - 10 <= enemy_bullet[e_bullet][1] <= player_y + 40/2 + 10):
                    page = 0
            if enemy_bullet[e_bullet][1] < - 25:
                del enemy_bullet[e_bullet]

        # Enemy movement and Player hitbox
        for movement in range(len(enemy) - 1, -1, -1):
            enemy[movement][0] += 5
            if enemy[movement][0] > WIDTH * 1.5:
                enemy[movement][0] = -300
            enemy[movement][1] -= 2
            if enemy[movement][1] == -22:
                enemy[movement][1] = HEIGHT + (40/2 + 2)
            if (enemy[movement][0] - 40/2 - 20 <= player_x <= enemy[movement][0] + 40/2 + 20 and
                    enemy[movement][1] - 40/2 - 20 <= player_y <= enemy[movement][1] + 40/2 + 20):
                page = 0
            
def on_draw():
    global player_x, player_y, player_bullet, enemy, enemy_bullet, page, button_color, enemy_healthbar, enemy_color_healthbar
    arcade.start_render()
    if page == 0:
        arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, (255, 255, 255, 5))
        arcade.draw_text("YOU DIED", WIDTH/2 - 250, HEIGHT/2 * 1.5, arcade.color.RED, 100)
        arcade.draw_text(":'(", WIDTH/2 - 100, HEIGHT/2, arcade.color.RED, 200)
        arcade.draw_xywh_rectangle_filled(WIDTH/3 - 30, HEIGHT/6, 300, 200, button_color)
    elif page == 1:
        arcade.draw_text("Home page", WIDTH/2 - 250, HEIGHT/2 * 1.5, arcade.color.BLUE, 100)
    elif page == 3:
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
        
        # Enemy bullet
        for enemy_bullet_draw in range(len(enemy_bullet)):
            arcade.draw_rectangle_filled(enemy_bullet[enemy_bullet_draw][0], enemy_bullet[enemy_bullet_draw][1] - 10, 10, 15, arcade.color.PURPLE)
            arcade.draw_rectangle_outline(enemy_bullet[enemy_bullet_draw][0], enemy_bullet[enemy_bullet_draw][1] - 10, 10, 15, arcade.color.WHITE, 2)
        
        # player
        arcade.draw_rectangle_filled(player_x, player_y, 40, 40, arcade.color.GREEN)
        arcade.draw_rectangle_outline(player_x, player_y, 40, 40, arcade.color.WHITE, 5)

        # player bullet
        for bullet_draw in range(len(player_bullet)):
            arcade.draw_rectangle_filled(player_bullet[bullet_draw][0], player_bullet[bullet_draw][1] + 10, 10, 15, arcade.color.BLUE)
            arcade.draw_rectangle_outline(player_bullet[bullet_draw][0], player_bullet[bullet_draw][1] + 10, 10, 15, arcade.color.WHITE, 2)


def on_key_press(key, modifiers):
    global key_pressed, page
    if page == 3:
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
    if page == 3:
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
    if page == 3 and button == arcade.MOUSE_BUTTON_LEFT:
            player_bullet_firerate = True
    elif page == 0 and button == arcade.MOUSE_BUTTON_LEFT:
            if (x > WIDTH/3 - 30 and x < WIDTH/3 - 30 + 300 and
                    y > HEIGHT/6 and y < HEIGHT/6 + 200):
                page = 1
                reset()
                level_one()
    elif page == 1 and button == arcade.MOUSE_BUTTON_LEFT:
            page = 3


def on_mouse_release(x, y, button, modifiers):
    global player_bullet_firerate, player_bullet_timer, player_bullet_click, page
    if page == 3 and button == arcade.MOUSE_BUTTON_LEFT:
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

    arcade.run()


if __name__ == '__main__':
    setup()