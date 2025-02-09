# CO 1010 - Final Project
# "Galaxy Hero" sample game using Pygame Zero Module

# Import libraries
import pgzrun
import random


# Set up the screen
WIDTH = 1200
HEIGHT = 800

# Set up initial values
i = 1
lives = 5
score = 0
count = 0
level = 1
speed = 8
start = False
mission = False  

# Draw rectangles for start and info buttons in menu
button_start = Rect((405, 480), (385, 85))
button_exit = Rect((405, 635), (385, 85))

# Draw rectangle for buttons shown after the game over
button_reset = Rect((140, 615), (385, 85))
button_menu = Rect((675, 615), (385, 85))
button_continue = Rect((820, 25), (300, 85))

# Load the menu image
menu = Actor("menu_image.png", (WIDTH // 2, HEIGHT // 2))

# Load the background images
background_1 = Actor("background_1.png", (1760 // 2, HEIGHT // 2))
background_2 = Actor("background_2.png", (1760 // 2 + 1760, HEIGHT // 2))

# Load image of the aircraft
aircraft = Actor("aircraft.png", (150, HEIGHT // 2))

# Load image of the obstacle
meteor_1 = Actor("meteor.png", (WIDTH, HEIGHT // 2))
meteor_2 = Actor("meteor.png", (WIDTH + 900, HEIGHT // 2))
stone_1 = Actor("stone.png", (WIDTH , HEIGHT // 2))
stone_2 = Actor("stone.png", (WIDTH , HEIGHT // 2))

# Load image of the repair icon 
repair = Actor("repair.png", (10000, random.randint(150, 650)))

# Load image of star
star = Actor("star.png", (3000, random.randint(150, 650)))

# Load game over image
game_over = Actor("game_over.png", (WIDTH // 2, HEIGHT // 2))

# Load the message image
spaceship = Actor("inside_spaceship.png", (WIDTH // 2, HEIGHT // 2))
message = Actor("message.png", (WIDTH // 2, HEIGHT // 2))
person_1 = Actor("person_1.png", (1005, 310))
person_2 = Actor("person_2.png", (100, 450))


# Define the function to reset the game
def reset_game():
    global i, lives, score, count, level, speed, start, mission, background_1, background_2, aircraft, meteor_1, meteor_2, stone_1, stone_2, repair, star
    
    # Reset initial values 
    i = 1
    lives = 5
    score = 0
    count = 0
    level = 1
    speed = 8
    mission = False
    
    # Reset the images
    background_1 = Actor("background_1.png", (1760 // 2, HEIGHT // 2))
    background_2 = Actor("background_2.png", (1760 // 2 + 1760, HEIGHT // 2))
    aircraft = Actor("aircraft.png", (150, HEIGHT // 2))
    meteor_1 = Actor("meteor.png", (WIDTH, HEIGHT // 2))        
    meteor_2 = Actor("meteor.png", (WIDTH + 900, HEIGHT // 2))
    stone_1 = Actor("stone.png", (WIDTH , HEIGHT // 2))
    stone_2 = Actor("stone.png", (WIDTH , HEIGHT // 2))
    repair = Actor("repair.png", (10000, random.randint(150, 650)))
    star = Actor("star.png", (3000, random.randint(150, 650)))
                 
# Define the draw function
def draw():
    screen.clear()
    
    # Set up the menu
    if not start:
        menu.draw()
        screen.draw.rect(button_start, 'black')
        screen.draw.rect(button_exit, 'black')
        screen.draw.text("Start Game", center=button_start.center, color='black', fontsize=50)
        screen.draw.text("Exit the Game", center=button_exit.center, color='black', fontsize=50)
 
    # Start the game
    elif start:
        if lives > 0:
            # Draw the images of the game
            background_1.draw()    
            background_2.draw() 
            aircraft.draw() 
             
                   # Limit the movement of the aircraft
                    
            meteor_1.draw()
            meteor_2.draw()           
            repair.draw()
            star.draw()
            if i > 3:       # Draw the image of stone_1 after passing level 3
                stone_1.draw()
            if i > 4:       # Draw the image of stone_2 after passing level 4
                stone_2.draw()
                
            # Display the game over message
            if aircraft.left > 1200: 
                music.stop()        # Stop the music
                spaceship.draw()
                message.draw()
                person_1.draw()
                person_2.draw()
                screen.draw.rect(button_continue, 'black')
                screen.draw.text("Continue", center=button_continue.center, color='black', fontsize=50) 
                
                # Display the final score
                if mission:
                    game_over.draw()
                    screen.draw.text("MISSION PASS", color="Green", center=(WIDTH // 2, 250), fontsize=200)
                    screen.draw.text(f"FINAL SCORE: {score}", color="Black", center=(WIDTH // 2, 400), fontsize=90)
                    screen.draw.text("Play Again", center=button_reset.center, color='black', fontsize=50)
                    screen.draw.text("Go to menu", center=button_menu.center, color='black', fontsize=50)   
    
            # Display the score, lives and level
            else:
                screen.draw.text(f"Score: {score}", color="White", topleft=(10, 20), fontsize=40)
                screen.draw.text(f"Lives: {lives}", color="White", topleft=(10, 50), fontsize=40)
                screen.draw.text(f"LEVEL: {level}", (500, 20), color="White", fontsize=100)
            
           
                 
        elif lives == 0:
            music.stop()        # Stop the music
            # Display the game over message and final score
            game_over.draw()
            screen.draw.text("MISSION FAIL", color="Red", center=(WIDTH // 2, 250), fontsize=200)
            screen.draw.text(f"FINAL SCORE: {score}", color="Black", center=(WIDTH // 2, 400), fontsize=90)
            screen.draw.text("Play Again", center=button_reset.center, color='black', fontsize=50)
            screen.draw.text("Go to menu", center=button_menu.center, color='black', fontsize=50)
 
                   
# Define the function to handle mouse cliks
def on_mouse_down(pos):
    global start, mission
    
    if button_start.collidepoint(pos):
        start = True
        play_music()        # Play the background music
     
    elif button_reset.collidepoint(pos):
        reset_game()        # Reset the game
        start = True
        mission = False
        play_music()        # Play the background music
        
    elif button_menu.collidepoint(pos):
        reset_game()
        start = False
    
    elif button_continue.collidepoint(pos):
        start = True
        mission = True   
        
            
    elif button_exit.collidepoint(pos):
        exit()      # Exit the game

# Define the function to take x-coordinate of meteors
def get_x(meteor):
    if meteor == meteor_1:      # Take the x-coordinate of meteor_1
        return meteor_1.x
    elif meteor == meteor_2:    # Take the x-coordinate ot meteor_2
        return meteor_2.x
    if meteor == aircraft:      # Take the x-coordinate of the aircraft
        return aircraft.x
# Define the update function   
def update():
    global lives, score, count, level, speed, i, start
    
    # Stopping the start of the game in the mune
    if not start or mission:
        return
    
    # Stopping the game after game is over
    if lives == 0:
        return
    
    # Stopping the game after mission is passed
    if aircraft.left > 1200:
        return
    
    # Increace the level with respect to scrore
    if count == 3 * i:
        i += 1 
        level += 1      
        if i < 4:       # Increace the speed with respect to scrore
            speed = 5 * i
            
        else:           # Keeping the speed at a constant value
            speed = 15
    
    if i <= 5 :
        # Move the background_1 image to the left
        background_1.x -= 5
    
        if background_1.right < 1:       # Reset the background_1 image position
            background_1.left = 1760
    
        # Move the background_2 image to the left
        background_2.x -= 5
    
        if background_2.right < 1:       # Reset the background_2 image position
            background_2.left = 1760
        
    elif i > 5:
        # Move the aircraft image to the right
        aircraft.x += 4
           
    # Move the meteor_1 image to the left
    meteor_1.x -= speed

    if meteor_1.right < 1 and get_x(aircraft) < 200:        # Reset the meteor_1 image position             
        meteor_1.left = 1800
        meteor_1.y = random.randint(150, 650)     # Randomize the y-coordinate of the mateor_1
        score += 2      # Increase the score by 2
        count += 1      # Increase the count by 1
        
    # Move the meteor_2 image to the left
    meteor_2.x -= speed

    if meteor_2.right < 1 and get_x(aircraft) < 200:       # Reset the meteor_2 image position             
        meteor_2.left = 1800
        meteor_2.y = random.randint(150, 650)     # Randomize the y-coordinate of the mateor_2
        score += 2      # Increase the score by 2
        count += 1      # Increase the count by 1
        
    # Move the repair icon to the left
    repair.x -= speed

    if repair.right < 1 and get_x(aircraft) < 200:      # Reset the repair icon position
        repair.left = 10000
        repair.y = random.randint(150, 650)
            
    if i > 3 :
        # Move the stone_1 image to the left
        stone_1.x -= speed
        
        if stone_1.right < 1 and get_x(aircraft) < 200:       # Reset the stone_1 image position
            meteor_x = get_x(meteor_1)      # Take x-coordinate of meteor_1
            stone_1.x = meteor_x + 450
            stone_1.y = random.randint(150, 650)        # Randomize the y-coordinate of the stone_1
            score += 5      # Increase the score by 5
            count += 1      # Increase the count by 1
            
    if i > 4 :
        # Move the stone_2 image to the left
        stone_2.x -= speed
        
        if stone_2.right < 1 and get_x(aircraft) < 200:       # Reset the stone_2 image position
            meteor_2_x = get_x(meteor_2)     # Take x-coordinate of meteor_2
            stone_2.x = meteor_2_x + 450
            stone_2.y = random.randint(150, 650)        # Randomize the y-coordinate of the stone_2
            score += 5       # Increase the score by 5
            count += 1       # Increase the count by 1    
 
    # Move the star image to the left
    star.x -= speed

    if star.right < 1 and get_x(aircraft) < 200:      # Reset the star image position
        star.left = 3000
        star.y = random.randint(150, 650) 
               
    # Checkibg collision between the aircraft and the meteor
    if meteor_1.colliderect(aircraft) and get_x(aircraft) < 200:
      
        meteor_2_x = get_x(meteor_2)      # Take x coordinate of meteor_2 
        meteor_1.x = meteor_2_x + 900     # Reset the x-coordinate of mateor_1
        meteor_1.y = random.randint(150, 650)     # Randomize the y-coordinate of the meteor_1
        lives -= 1      # Reduce the lives by 1
        sounds.crashing_sound.play()      # Play crashing sound
        
    # Checkibg collision between the aircraft and the meteor2
    if meteor_2.colliderect(aircraft) and get_x(aircraft) < 200:
   
        meteor_x = get_x(meteor_1)      # Take x coordinate of meteor_1
        meteor_2.x = meteor_x + 900     # Reset the x-coordinate of mateor_2  
        meteor_2.y = random.randint(150, 650)     # Randomize the y-coordinate of the meteor_2 
        lives -= 1      # Reduce the lives by 1
        sounds.crashing_sound.play()      # Play the crashing sound
        
    # Checking collision between the aircraft and fuel tank
    if repair.colliderect(aircraft) and get_x(aircraft) < 200:
           # Increase the x-coordinate of the fuel tank
        repair.x = 10000       # Reset the x-coordinate of the fuel tank
        repair.y = random.randint(150, 650)       # Randomize the y-coordinate of the fuel tank
        if lives < 5:       # Increase the lives by 1 when lives are less than 5
            lives += 1  
        sounds.repair_sound.play()        # Play the crashing sound   

    # Checking collision between the aircraft and stone_1
    if i > 3 and stone_1.colliderect(aircraft) and get_x(aircraft) < 200:
        meteor_x = get_x(meteor_1)      # Take x-coordinate of meteor_1 
        stone_1.x = meteor_x + 450      # Reset x-coordinate of stone_1
        stone_1.y = random.randint(150, 650)        # Randomize the y-coordinate of the stone_1
        lives -= 1      # Increase the lives by 1   
        sounds.crashing_sound.play()      # Play the crashing sound
    
    # Checking the collision between the aircraft and stone_2    
    if i > 4 and stone_2.colliderect(aircraft) and get_x(aircraft) < 200:
        meteor2_x = get_x(meteor_2)     # Take x-coordinate of meteor_2
        stone_2.x = meteor2_x + 450     # reset x-coordinate of stone_2
        stone_2.y = random.randint(150, 650)        # Randomize the y-coordinate of the stone_2
        lives -= 1      # Increase the lives by 1 
        sounds.crashing_sound.play()      # Play the crashing sound

    # Checking collision between the aircraft and star
    if star.colliderect(aircraft) and get_x(aircraft) < 200:
            # Increase the x-coordinate of the star
        star.x = 3000       # Reset the x-coordinate of the star
        star.y = random.randint(150, 650)       # Randomize the y-coordinate of the star
        score += 10       # Increase the score by 10
        sounds.star_sound.play()        # Play the crashing sound 
                
    # Move the aircraft up and down    
    if keyboard.down:
        if aircraft.y < 650:    # Limit bottom movement
            aircraft.y += 10
            
    elif keyboard.up:
        if aircraft.y > 150:    # Limit top movement
            aircraft.y -= 10
            
# Define the function to play the background music
def play_music():
    music.play("aircraft_sound")
    music.set_volume(1.0)
     
# Run the game
pgzrun.go()