'''
Note:
Most functions have no arguements because the main purpose of them in this program is to keep everything more organized.
Problems occur because I wanted to avoid exception handling (try: except:) 
and varibles that are global throughtout the program doesn't need to be used in that particular function
'''
import arcade
import os
import math
import random
 
WIDTH = 700
HEIGHT = 800
 
# start player position in middle of window
player_x = WIDTH/2
player_y = HEIGHT/2
 
# bullets of player
player_bullet = []
player_rocket = []
player_rocket_firerate = False
player_rocket_timer = 0
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

# Numbers that players can achieve
score = 0
combo = 0

# Player shield
shield = []
shield_timer = 0
shield_uptime = False

# Variable to record if certain keys are being pressed.
key_pressed = [False] * 4
 
# Colour change when the user hovers over it
button_color = arcade.color.BLUE
button_color_two = button_color

# Different screens
page = 1
 

def level_one():
    """Spawns the enemies in level 1
    """    
    for enemy_x in range(int(WIDTH/3 - WIDTH/7), WIDTH, int(WIDTH/3)):
        enemy.append([enemy_x, HEIGHT/2 * 1.75, 3])
 

def level_two():
    """Spawns the enemies in level 2
    """    
    for enemy_x in range(int(WIDTH/3 - WIDTH/7), WIDTH, int(WIDTH/3)):
        enemy.append([enemy_x, HEIGHT/2 * 1.75, 3])
 
 
def level_three():
    """Spawns the enemies in level 3 and reset some variables
    """    
    global enemy_bullet_timer, amount_laser_enemies
    enemy_bullet_timer = -50
    amount_laser_enemies = 9
    for enemy_two_x in range(int(WIDTH/9 - 20), WIDTH, int(WIDTH/9)):
        enemy_two.append([enemy_two_x, HEIGHT/2 * 1.75, 3])
 

def level_four():
    """Spawns in enemies in level 4 and reset some variables
    """    
    global enemy_bullet_timer, amount_laser_enemies
    enemy_bullet_timer = -50
    amount_laser_enemies = 2
    for enemy_x in range(int(WIDTH/3 - WIDTH/7), WIDTH, int(WIDTH/3)):
        enemy.append([enemy_x, HEIGHT/2 * 1.75, 3])
    for enemy_two_x in range(310, 410, 99):
        enemy_two.append([enemy_two_x, HEIGHT - 50, 3])


def level_boss():
    """Spawns the boss enemy and reset some variables
    """    
    global enemy_lives, enemy_size_healthbar, enemy_bullet_firerate, player_x, player_y
    enemy.append([player_x, player_y + 200, 50])
    enemy_lives = 50
    enemy_size_healthbar = 600
    enemy_bullet_firerate = 30
    player_x = WIDTH/2
    player_y = HEIGHT/2 * 0.5
 
 
def reset():
    """Resets all variables in the program
    """    
    global enemy, enemy_bullet, enemy_bullet_firerate, enemy_bullet_timer, key_pressed, enemy_healthbar, enemy_color_healthbar, player_x, player_y
    global enemy_lives, enemy_size_healthbar, enemy_bullet_angle
    global random_movement, enemy_lazer_firerate, laser_y, enemy_two, enemy_lazer, enemy_lazer_charging, score
    player_x = WIDTH/2
    player_y = HEIGHT/2
    enemy = []
    enemy_two = []
    enemy_lazer_charging = []
    enemy_lazer = []
    enemy_bullet = []
    enemy_bullet_timer = -140
    enemy_bullet_firerate = 50
    enemy_bullet_angle = 0
    enemy_lives = 3
    enemy_size_healthbar = 40
    enemy_healthbar = 40
    enemy_color_healthbar = arcade.color.GREEN
    random_movement = [[0, 0]]
    enemy_lazer_firerate = 50
    laser_y = 0
    
 
def player_movement():
    """Contains the movement in player x and y axis
    """    
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
    """Makes sure that the player cannot leave the screen
    """    
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
    """Creates bullets and maintains the firerate of the bullets
    """    
    global player_bullet_click, player_bullet_firerate, player_bullet, player_bullet_timer
    # Firerate of bullet
    if player_bullet_click < 20:
        player_bullet_click += 1
    if player_bullet_firerate:
        player_bullet_timer += 1
    if player_bullet_timer % 20 == 0 and player_bullet_click == 20:
        player_bullet.append([player_x, player_y])
 
 
def enemy_hit():
    """Keeps track of score and combo of player and checks if the player rocket or bullet hits the enemy. 
    Also the speed of the rocket and bullet are created in this function.
    """    
    global enemy, player_bullet, enemy_lives, enemy_healthbar, enemy_lives, enemy_size_healthbar, enemy_size_healthbar, enemy_two, score, combo
    global player_rocket_firerate, player_rocket_timer
    # Checks if player bullet hits an enemy
    for bullet_animation in range(len(player_bullet) - 1, -1, -1):
        for hit in range(len(enemy) - 1, -1, -1):
            if (enemy[hit][0] - enemy_size_healthbar/2 - 5 <= player_bullet[bullet_animation][0] <= enemy[hit][0] + enemy_size_healthbar/2 + 5 and 
                enemy[hit][1] - 40/2 - 5 <= player_bullet[bullet_animation][1] <= enemy[hit][1] + 40/2 + 5):
                del player_bullet[bullet_animation]
                player_bullet.append([0, 826])
                enemy[hit][2] -= 1
                score += 5
                combo += 1
                if enemy[hit][2] <= 0:
                    del enemy[hit]
                    score += 100

    
        for hit_enemy in range(len(enemy_two) - 1, -1, -1):
            if (enemy_two[hit_enemy][0] - enemy_size_healthbar/2 - 5 <= player_bullet[bullet_animation][0] <= enemy_two[hit_enemy][0] + enemy_size_healthbar/2 + 5 and 
                enemy_two[hit_enemy][1] - 40/2 - 5 <= player_bullet[bullet_animation][1] <= enemy_two[hit_enemy][1] + 40/2 + 5):
                del player_bullet[bullet_animation]
                player_bullet.append([0, 826])
                enemy_two[hit_enemy][2] -= 1
                score += 5
                combo += 1
                if enemy_two[hit_enemy][2] <= 0:
                    del enemy_two[hit_enemy]
                    score += 100

        # player bullet speed
        player_bullet[bullet_animation][1] += 15
        if player_bullet[bullet_animation][1] > HEIGHT + 25: 
            del player_bullet[bullet_animation]

    # player rocket
    if player_rocket_firerate:
        player_rocket_timer += 1

    if player_rocket_timer == 500:
        player_rocket_firerate = False
        player_rocket_timer = 0
    
    # Checks if player rocket hits an enemy
    for rocket_animation in range(len(player_rocket) - 1, -1, -1):
        for hit in range(len(enemy) - 1, -1, -1):
            if (enemy[hit][0] - enemy_size_healthbar/2 - 5 <= player_rocket[rocket_animation][0] <= enemy[hit][0] + enemy_size_healthbar/2 + 5 and 
                enemy[hit][1] - 40/2 - 5 <= player_rocket[rocket_animation][1] <= enemy[hit][1] + 40/2 + 5):
                del player_rocket[rocket_animation]
                player_rocket.append([0, 826])
                enemy[hit][2] -= 3
                if enemy[hit][2] <= 0:
                    del enemy[hit]
                    score += 100

        for hit_enemy in range(len(enemy_two) - 1, -1, -1):
            if (enemy_two[hit_enemy][0] - enemy_size_healthbar/2 - 5 <= player_rocket[rocket_animation][0] <= enemy_two[hit_enemy][0] + enemy_size_healthbar/2 + 5 and 
                enemy_two[hit_enemy][1] - 40/2 - 5 <= player_rocket[rocket_animation][1] <= enemy_two[hit_enemy][1] + 40/2 + 5):
                del player_rocket[rocket_animation]
                player_rocket.append([0, 826])
                enemy_two[hit_enemy][2] -= 3
                if enemy_two[hit_enemy][2] <= 0:
                    del enemy_two[hit_enemy]
                    score += 100
        
        # Player rocket speed
        player_rocket[rocket_animation][1] += 15
        if player_rocket[rocket_animation][1] > HEIGHT + 25: 
            del player_rocket[rocket_animation]
 
 
def enemy_bullet_and_player_death_by_bullets():
    """Checks if the enemy bullet hits the player or shield
    """    
    global enemy_bullet_timer, enemy_bullet_firerate, enemy_bullet, player_x, player_y, page, enemy, enemy_bullet_angle, enemy_two, enemy_lazer, enemy_lazer_firerate
    global enemy_lazer_charging, laser_y, amount_laser_enemies, shield_uptime, shield_timer
    # Shield
    if 3 <= page <= 7:
        if shield_uptime:
            shield_timer += 1

        if shield_timer >= 50 and len(shield) == 1:
            del shield[0]

        if shield_timer >= 500:
            shield_timer = 0
            shield_uptime = False

    # Firerate of enemy bullet
    enemy_bullet_timer += 1

    # Creates enemy bullet
    if enemy_bullet_timer % enemy_bullet_firerate == 0:
        for i in range(len(enemy) - 1, -1, -1):
            enemy_bullet.append([enemy[i][0], enemy[i][1]])

    # Checks if the enemy bullet hits the player's shield
    for e_bullet in range(len(enemy_bullet) - 1, -1, -1):
        if shield_uptime and len(shield) == 1:
            distance = math.sqrt((enemy_bullet[e_bullet][0] - player_x)**2 + (enemy_bullet[e_bullet][1] - player_y)**2)
            if distance <= 50:
                del enemy_bullet[e_bullet]
                enemy_bullet.append([0, 26])
                del shield[0]

        # Checks if player is hit
        if (player_x - 40/2 - 10 <= enemy_bullet[e_bullet][0] <= player_x + 40/2 + 10 and
                player_y - 40/2 - 10 <= enemy_bullet[e_bullet][1] <= player_y + 40/2 + 10):
                page = 0

        # Enemy bullet speed
        if 3 <= page <= 6:
            enemy_bullet[e_bullet][1] -= 15
            if enemy_bullet[e_bullet][1] < - 25:
                del enemy_bullet[e_bullet]

        # Tracking bullets on boss level
        elif page == 7:
            for direction in range(len(enemy) - 1, -1, -1):
                x_diff = enemy[direction][0] - player_x
                y_diff = enemy[direction][1] - player_y
                angle = math.atan2(y_diff, x_diff)
                enemy_bullet_angle = math.degrees(angle) - 90
                bullet_change_x = math.cos(angle) * 5
                bullet_change_y = math.sin(angle) * 5
                enemy_bullet[e_bullet][1] -= bullet_change_y
                enemy_bullet[e_bullet][0] -= bullet_change_x


    # lazer enemy
    if 5 <= page <= 6:
        # Creates enemy lazer charging texture
        if 100 <= enemy_bullet_timer <= 104:
            for i in range(len(enemy_two) - 1, -1, -1):
                enemy_lazer_charging.append([enemy_two[i][0], enemy_two[i][1]])
                if len(enemy_lazer_charging) == amount_laser_enemies + 1:
                    del enemy_lazer_charging[0]

        # When the enemy lazer charging texture disappears
        if enemy_bullet_timer % 105 == 0:
            enemy_lazer_charging = []        

        # Creates enemy real lazer texture
        if 200 <= enemy_bullet_timer <= 299:
            for j in range(len(enemy_two) - 1, -1, -1):
                enemy_lazer.append([enemy_two[j][0], enemy_two[j][1]])
                if len(enemy_lazer) == amount_laser_enemies + 1:
                    del enemy_lazer[0]
        
        # When the enemy real lazer disappears
        if enemy_bullet_timer % 299 == 0:
            enemy_lazer = []
            laser_y = 0

        # Resets the enemy bullet timer because somehow the modulus wouldn't work and speed up
        if enemy_bullet_timer >= 299:
            enemy_bullet_timer = -50

        # Checks if enemy lazer hits the player
        for enemy_two_lazer in range(len(enemy_lazer) - 1, -1, -1):
            if (player_x - 40/2 - 10 <= enemy_lazer[enemy_two_lazer][0] <= player_x + 40/2 + 10 and
                enemy_lazer[enemy_two_lazer][1] - 30 - laser_y <= player_y + 30 <= enemy_lazer[enemy_two_lazer][1]):
                    page = 0


def enemy_movement_and_collision_with_player():
    """Movement of all enemy players
    """    
    global enemy, page, enemy_size_healthbar, enemy_bullet_timer, random_movement, enemy_two, enemy_two_speed
    # Enemy movement 
    for movement in range(len(enemy) - 1, -1, -1):
        if page == 3 or page == 6:
            # Movement on x-axis
            enemy[movement][0] += 5
            if enemy[movement][0] > WIDTH * 1.5:
                enemy[movement][0] = -300

            # Movement on y-axis
            enemy[movement][1] -= 2
            if enemy[movement][1] <= -22:
                enemy[movement][1] = HEIGHT + (40/2 + 2)
        
        # Checks if the enemy runs into the player
        if (enemy[movement][0] - enemy_size_healthbar/2 - 20 <= player_x <= enemy[movement][0] + enemy_size_healthbar/2 + 20 and
                enemy[movement][1] - 40/2 - 20 <= player_y <= enemy[movement][1] + 40/2 + 20):
            page = 0

        elif page == 4:
            # Creates movement speed
            if enemy_bullet_timer % 50 == 0:
                del random_movement[0]
                random_movement.append([random.randint(-3, 3), random.randint(0, 3)])
            
            # Movement on the x-axis
            enemy[movement][0] += random_movement[0][0]

            # Checks if the enemy goes out of the scren
            if enemy[movement][0] > WIDTH + 40/2 or enemy[movement][0] < -40/2:
                enemy[movement][0] = WIDTH/2
                enemy[movement][1] = HEIGHT + (40/2 + 2)
            
            # Movement on the y-axis
            enemy[movement][1] -= random_movement[0][1]

            # Checks if enemies go out of the screen
            if enemy[movement][1] <= -22:
                    enemy[movement][1] = HEIGHT + (40/2 + 2)

        # Checks if the enemy runs into the player
        if (enemy[movement][0] - enemy_size_healthbar/2 - 20 <= player_x <= enemy[movement][0] + enemy_size_healthbar/2 + 20 and
                enemy[movement][1] - 40/2 - 20 <= player_y <= enemy[movement][1] + 40/2 + 20):
            page = 0

    # Enemy movement for lazer enemy
    for movement_enemy_two in range(len(enemy_two) -1, -1, -1):
        if page == 6:
            # Movement on the x-axis
            enemy_two[movement_enemy_two][0] += enemy_two_speed

            # Checks if the enemy goes out of the screen
            if enemy_two[movement_enemy_two][0] > WIDTH - 40/2 or enemy_two[movement_enemy_two][0] < 40/2:
                enemy_two_speed = -enemy_two_speed

        # Checks if the enemy runs into the player
        if (enemy_two[movement_enemy_two][0] - enemy_size_healthbar/2 - 20 <= player_x <= enemy_two[movement_enemy_two][0] + enemy_size_healthbar/2 + 20 and
            enemy_two[movement_enemy_two][1] - 40/2 - 20 <= player_y <= enemy_two[movement_enemy_two][1] + 40/2 + 20):
            page = 0

 
def enemy_player_and_healthbar_draw():
    """Draws enemy players and their healthbar
    """    
    global enemy, enemy_healthbar, enemy_color_healthbar, enemy_lives, enemy_size_healthbar, enemy_texture, enemy_two, enemy_two_texture, boss 
    for draw in range(len(enemy) - 1, -1, -1):
        scale = 1

        # Draws enemy players and boss
        if 3 <= page <= 6:
            arcade.draw_texture_rectangle(enemy[draw][0], enemy[draw][1], scale * enemy_texture.width, scale * enemy_texture.height, enemy_texture)
        elif page == 7:
            scale = 0.2
            arcade.draw_texture_rectangle(enemy[draw][0], enemy[draw][1], scale * boss_texture.width, scale * boss_texture.height, boss_texture, 180)

        # Checks the healthbar colour
        if 1/3 * 100 < enemy[draw][2]/enemy_lives * 100 <= 2/3 * 100:
            enemy_color_healthbar = arcade.color.YELLOW
        elif enemy[draw][2]/enemy_lives * 100 <= 1/3 * 100:
            enemy_color_healthbar = arcade.color.RED
        else:
            enemy_color_healthbar = arcade.color.GREEN
        enemy_healthbar = enemy_size_healthbar * enemy[draw][2]/enemy_lives

        # Draws the health bar
        if 3 <= page <= 6:
            arcade.draw_xywh_rectangle_filled(enemy[draw][0] - enemy_size_healthbar/2, enemy[draw][1] + 40/2 + 5, enemy_healthbar, 5, enemy_color_healthbar)
        elif page == 7:
            arcade.draw_xywh_rectangle_filled(enemy[draw][0] - enemy_size_healthbar/2, enemy[draw][1] + 50, enemy_healthbar, 5, enemy_color_healthbar)

    for enemy_two_draw in range(len(enemy_two) - 1, -1, -1):
        scale = 1
        
        # Draws enemy lazers
        arcade.draw_texture_rectangle(enemy_two[enemy_two_draw][0], enemy_two[enemy_two_draw][1], scale * enemy_two_texture.width, scale * enemy_two_texture.height, enemy_two_texture)

        # Draws healthbar of enemy lazers
        if 1/3 * 100 < enemy_two[enemy_two_draw][2]/enemy_lives * 100 <= 2/3 * 100:
            enemy_color_healthbar = arcade.color.YELLOW
        elif enemy_two[enemy_two_draw][2]/enemy_lives * 100 <= 1/3 * 100:
            enemy_color_healthbar = arcade.color.RED
        else:
            enemy_color_healthbar = arcade.color.GREEN
        enemy_healthbar = enemy_size_healthbar * enemy_two[enemy_two_draw][2]/enemy_lives

        # Draws healthbar
        arcade.draw_xywh_rectangle_filled(enemy_two[enemy_two_draw][0] - enemy_size_healthbar/2, enemy_two[enemy_two_draw][1] + 40/2 + 5, enemy_healthbar, 5, enemy_color_healthbar)
 
 
def enemy_bullet_draw():
    """Draws bullets
    """    
    global enemy_bullet, enemy_bullet_angle, enemy_bullet_texture, enemy_lazer, enemy_lazer_firing_texture, enemy_laser_charging_texture, enemy_lazer_charging
    global laser_y, enemy_bullet_timer, enemy_two_speed
    # Enemy bullet
    for enemy_bullet_draw in range(len(enemy_bullet)):
        scale = 1
        # Draws for reagular enemy
        if 3 <= page <= 6:
            arcade.draw_texture_rectangle(enemy_bullet[enemy_bullet_draw][0], enemy_bullet[enemy_bullet_draw][1] - 10, scale * enemy_bullet_texture.width, scale * enemy_bullet_texture.height, enemy_bullet_texture, enemy_bullet_angle)
        # Draws for boss
        elif page == 7:
            arcade.draw_texture_rectangle(enemy_bullet[enemy_bullet_draw][0], enemy_bullet[enemy_bullet_draw][1] - 15, scale * enemy_bullet_texture.width, scale * enemy_bullet_texture.height, enemy_bullet_texture, enemy_bullet_angle)

    # Enemy laser descending rate
    if 5 <= page <= 6:
        if 200 <= enemy_bullet_timer <= 299:
            laser_y += 20
        
        # Draws enemy lazer
        for enemy_lazer_draw in range(len(enemy_lazer)):
            arcade.draw_xywh_rectangle_textured(enemy_lazer[enemy_lazer_draw][0] - 20, enemy_lazer[enemy_lazer_draw][1] - 30 - laser_y, 40, 0 + laser_y, enemy_laser_firing_texture)

        # Draws enemy charging lazer
        for enemy_lazer_charging_draw in range(len(enemy_lazer_charging)):
            arcade.draw_texture_rectangle(enemy_lazer_charging[enemy_lazer_charging_draw][0], enemy_lazer_charging[enemy_lazer_charging_draw][1] - 380, 4 * enemy_laser_charging_texture.width, 35 * enemy_laser_charging_texture.height, enemy_laser_charging_texture)


def player_draw():
    """Draws enemy player and player shield
    """    
    global player_x, player_y, player_texture
    # player
    scale = 1
    # Draws player
    arcade.draw_texture_rectangle(player_x, player_y, scale * player_texture.width, scale * player_texture.height, player_texture)

    # Draws Shield in respect to the player x and y axis
    for shield_draw in range(len(shield)):
        arcade.draw_texture_rectangle(player_x, player_y, scale * shield_texture.width, scale * shield_texture.height, shield_texture)


def player_bullet_draw():
    """Draws player bullet and rocket
    """    
    global player_bullet, player_bullet_texture, rocket_texture
    scale = 1

    # Draws player bullet
    for bullet_draw in range(len(player_bullet)):
        arcade.draw_texture_rectangle(player_bullet[bullet_draw][0], player_bullet[bullet_draw][1] + 10, scale * player_bullet_texture.width, scale * player_bullet_texture.height, player_bullet_texture)
    
    # Draws player rocket
    for rocket_draw in range(len(player_rocket)):
        arcade.draw_texture_rectangle(player_rocket[rocket_draw][0], player_rocket[rocket_draw][1] + 10, scale * rocket_texture.width, scale * rocket_texture.height, rocket_texture)


def dead_draw():
    """Draws player dead page
    """    
    global button_color
    # Draws button
    arcade.draw_xywh_rectangle_filled(WIDTH/3 - 30, HEIGHT/6, 300, 200, button_color)

    # Draws text
    arcade.draw_text("<< GAME OVER >>", WIDTH/2 - 325, HEIGHT/2 * 1.5, arcade.color.RED, 70)
    arcade.draw_text("Score: {}".format(score), WIDTH/2 - 100, HEIGHT/2 + 100, arcade.color.RED, 50)
    arcade.draw_text("Finished combo: {}".format(score), WIDTH/2 - 225, HEIGHT/2 + 50, arcade.color.RED, 50)
    arcade.draw_text("Player deaths: 1", WIDTH/2 - 200, HEIGHT/2, arcade.color.RED, 50)
    arcade.draw_text("Back to", WIDTH/3 + 25, HEIGHT/2 - 150, arcade.color.WHITE, 50)
    arcade.draw_text("Menu", WIDTH/3 + 30, HEIGHT/2 - 225, arcade.color.WHITE, 50)
 
 
def home_page_draw():
    """Draws the home page
    """    
    arcade.draw_text("HYPERSPACE", 25, HEIGHT/2 * 1.5, arcade.color.WHITE, 100)
    arcade.draw_xywh_rectangle_filled(WIDTH/6, HEIGHT/2, 500, 100, button_color)
    arcade.draw_text("Play", WIDTH/2 - 75, HEIGHT/2 + 15, arcade.color.WHITE, 75)
    arcade.draw_xywh_rectangle_filled(WIDTH/6, HEIGHT/4, 500, 100, button_color_two)
    arcade.draw_text("How to play", WIDTH/6 + 25, HEIGHT/4 + 10, arcade.color.WHITE, 75)
    

def controls_page_draw():
    """Draws the "how to play" page
    """    
    arcade.draw_text("W - Forward", 25, HEIGHT - 60, arcade.color.WHITE, 60)
    arcade.draw_text("S - Backward", 25, HEIGHT - 120, arcade.color.WHITE, 60)
    arcade.draw_text("A - Left", 25, HEIGHT - 180, arcade.color.WHITE, 60)
    arcade.draw_text("D - Right", 25, HEIGHT - 240, arcade.color.WHITE, 60)
    arcade.draw_text("LSHIFT - Shield", 25, HEIGHT - 310, arcade.color.WHITE, 60)
    arcade.draw_text("LMB - Bullet", 25, HEIGHT - 370, arcade.color.WHITE, 60)
    arcade.draw_text("RMB - Rocket", 25, HEIGHT - 430, arcade.color.WHITE, 60)
    arcade.draw_xywh_rectangle_filled(WIDTH/3 - 30, HEIGHT/6, 300, 200, button_color)
    arcade.draw_text("Back to", WIDTH/3 + 25, HEIGHT/2 - 150, arcade.color.WHITE, 50)
    arcade.draw_text("Menu", WIDTH/3 + 30, HEIGHT/2 - 225, arcade.color.WHITE, 50)

def win_page_draw():
    """Draws the player win page
    """    
    # Draws button
    arcade.draw_xywh_rectangle_filled(WIDTH/3 - 30, HEIGHT/6, 300, 200, button_color)

    # Draws text
    arcade.draw_text("<< VICTORY >>", WIDTH/2 - 250, HEIGHT/2 * 1.5, arcade.color.RED, 70)
    arcade.draw_text("Score: {}".format(score), WIDTH/2 - 100, HEIGHT/2 + 100, arcade.color.RED, 50)
    arcade.draw_text("Finished combo: {}".format(score), WIDTH/2 - 225, HEIGHT/2 + 50, arcade.color.RED, 50)
    arcade.draw_text("Player deaths: 0", WIDTH/2 - 200, HEIGHT/2, arcade.color.RED, 50)
    arcade.draw_text("Back to", WIDTH/3 + 25, HEIGHT/2 - 150, arcade.color.WHITE, 50)
    arcade.draw_text("Menu", WIDTH/3 + 30, HEIGHT/2 - 225, arcade.color.WHITE, 50)


def play_page():
    """Draws the play page which keeps track of player statistics, rocket, and sheild usage
    """    
    global score, combo, player_rocket_timer
    # Left side
    arcade.draw_text("Score: {}".format(score), 0, HEIGHT - 31, arcade.color.WHITE, 30)
    arcade.draw_text("Combo: x{}".format(combo), 0, HEIGHT - 61, arcade.color.WHITE, 30)

    # Right side
    arcade.draw_texture_rectangle(WIDTH - 125, HEIGHT - 25, 50, 50, health_texture)
    arcade.draw_text("Lives", WIDTH - 100, HEIGHT - 45, arcade.color.RED, 30)
    arcade.draw_texture_rectangle(WIDTH - 125, HEIGHT - 75, 50, 50, rocket_texture)
    arcade.draw_xywh_rectangle_filled(WIDTH - 100, HEIGHT - 100, player_rocket_timer/5, 50, (0, 255, 0, 50))
    arcade.draw_texture_rectangle(WIDTH - 125, HEIGHT - 125, 50, 50, shield_texture)
    arcade.draw_xywh_rectangle_filled(WIDTH - 100, HEIGHT - 155, shield_timer/5, 50, (0, 255, 0, 50))


# Generates enemies
level_one()


def on_update(delta_time):
    global page, enemy
    # Increases the page number when all enemies in the level are dead
    if len(enemy) == 0 and len(enemy_two) == 0 and page != 8 and not 0 <= page <= 2:
        page += 1

    if len(enemy) == 0 and len(enemy_two) == 0 and page == 4:
        reset()
        level_two()
    elif len(enemy) == 0 and len(enemy_two) == 0 and page == 5:
        reset()
        level_three()
    elif len(enemy) == 0 and len(enemy_two) == 0 and page == 6:
        reset()
        level_four()
    elif len(enemy) == 0 and len(enemy_two) == 0 and page == 7:
        reset()
        level_boss()
        

    if 3 <= page <= 7:
        player_movement()
        constrain_player()
        bullet_player_firerate()
        enemy_hit()
        enemy_bullet_and_player_death_by_bullets()
        enemy_movement_and_collision_with_player()

    
def on_draw():
    """Draws the screen in terms of what page is the user on
    """    
    arcade.start_render()
    global page
    if page == 0:
        dead_draw()
    elif page == 1:
        home_page_draw()
    elif page == 2:
        controls_page_draw()
    elif 3 <= page <= 7:
        enemy_player_and_healthbar_draw()
        enemy_bullet_draw()
        player_draw()
        player_bullet_draw()
        play_page()
    elif page == 8:
        win_page_draw()
 

def on_key_press(key, modifiers):
    """Checks which key the user is pressing and creates shield
    
    Arguments:
        key {int} -- Key that is hit
        modifiers {int} -- If it was shift/ctrl/alt 
    """    
    global key_pressed, page, shield, shield_uptime, shield_timer
    if page >= 3:
        if key == arcade.key.W:
            key_pressed[0] = True
        if key == arcade.key.S:
            key_pressed[1] = True
        if key == arcade.key.A:
            key_pressed[2] = True
        if key == arcade.key.D:
            key_pressed[3] = True

    # Creates shield
    if key == arcade.key.LSHIFT and shield_timer == 0:
        shield.append([player_x, player_y])
        shield_uptime = True    
 
def on_key_release(key, modifiers):
    """Checks which key the user is pressing
    
    Arguments:
        key {int} -- Key that is hit
        modifiers {int} -- checks if it was shift/ctrl/alt 
    """    
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
    """Creates buttons and checks if the mouse clicks on them
    
    Arguments:
        x {float} -- mouse x-axis
        y {float} -- mouse y-axis
        button {int} -- Checks which mouse button is being pressed
        modifiers {int} -- checks if it was shift/ctrl/alt 
    """    
    global player_x, player_y, player_bullet, player_bullet_firerate, page, button_color, score, combo, key_pressed, player_rocket, player_rocket_firerate
    global player_rocket_timer, shield, shield_timer, shield_uptime
    if page >= 3 and button == arcade.MOUSE_BUTTON_LEFT:
            player_bullet_firerate = True
    if page >= 3 and player_rocket_timer == 0 and button == arcade.MOUSE_BUTTON_RIGHT:
            player_rocket.append([player_x, player_y])
            player_rocket_firerate = True
    if page == 0 or page == 2 or page == 8 and button == arcade.MOUSE_BUTTON_LEFT:
            if (x > WIDTH/3 - 30 and x < WIDTH/3 - 30 + 300 and
                    y > HEIGHT/6 and y < HEIGHT/6 + 200):
                page = 1
    elif page == 1 and button == arcade.MOUSE_BUTTON_LEFT:
        if (x > WIDTH/6 and x < WIDTH/6 + 500 and
                y > HEIGHT/2 and y < HEIGHT/2 + 100):
            reset()
            level_one()
            player_bullet = []
            key_pressed = [False] * 4
            score = 0
            combo = 0
            page = 3
            player_rocket = []
            player_rocket_firerate = False
            player_rocket_timer = 0
            shield = []
            shield_timer = 0
            shield_uptime = False
        if (x > WIDTH/6 and x < WIDTH/6 + 500 and
                y > HEIGHT/4 and y < HEIGHT/4 + 100):
            page = 2


 
def on_mouse_release(x, y, button, modifiers):
    """Creates player bullet firerate when released
    
    Arguments:
        x {float} -- mouse x-axis
        y {float} -- mouse y-axis
        button {int} -- Checks which mouse button is released
        modifiers {int} -- checks if it was shift/ctrl/alt 
    """    
    global player_bullet_firerate, player_bullet_timer, player_bullet_click, page
    if page >= 3 and button == arcade.MOUSE_BUTTON_LEFT:
        player_bullet_timer = -2
        player_bullet_firerate = False
        if player_bullet_click == 20:
            player_bullet_click = -2
 
 
def on_mouse_motion(x, y, dx, dy):
    """Changes the color of buttons
    
    Arguments:
        x {float} -- mouse x-axis
        y {float} -- mouse y-axis
        dx {float} -- x changed when the function was called
        dy {float} -- y changed when the function was called
    """    
    global button_color, page, button_color_two
    if page == 0 or page == 2 or page == 8:
        if (x > WIDTH/3 - 30 and x < WIDTH/3 - 30 + 300 and
                y > HEIGHT/6 and y < HEIGHT/6 + 200):
            button_color = arcade.color.BLUE_SAPPHIRE
        else:
            button_color = arcade.color.BLUE
    elif page == 1:
        if (x > WIDTH/6 and x < WIDTH/6 + 500 and
                y > HEIGHT/2 and y < HEIGHT/2 + 100):
            button_color = arcade.color.BLUE_SAPPHIRE
        else:
            button_color = arcade.color.BLUE
        if (x > WIDTH/6 and x < WIDTH/6 + 500 and
                y > HEIGHT/4 and y < HEIGHT/4 + 100):
            button_color_two = arcade.color.BLUE_SAPPHIRE
        else:
            button_color_two = arcade.color.BLUE
 
 
def setup():
    """Loads sprites and sets up the window and creates user input
    """    
    global player_texture, player_bullet_texture, enemy_texture, enemy_bullet_texture, enemy_two_texture, enemy_laser_charging_texture, enemy_laser_firing_texture
    global boss_texture, health_texture, rocket_texture, shield_texture
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
    boss_texture = arcade.load_texture("images/boss.png")
    health_texture = arcade.load_texture("images/Health_Pack.png")
    rocket_texture = arcade.load_texture("images/Rocket.png")
    shield_texture = arcade.load_texture("images/Shielded.png")

    arcade.run()
 
 
if __name__ == '__main__':
    setup()