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
j = 1
lives = 5
score = 0
level = 1
speed = 6
start = False
show_info = False

# Draw rectangles for start and info buttons in menu
button_start = Rect((405, 480), (385, 85))
button_info = Rect((405, 635), (385, 85))

# Draw rectangle for buttons shown after the game over
button_restart = Rect((140, 615), (385, 85))
button_menu = Rect((675, 615), (385, 85))

# Load the menu image
menu = Actor("menu_image.png", (WIDTH // 2, HEIGHT // 2))

# Load the background images
background_1 = Actor("background.png", (WIDTH // 2, HEIGHT // 2))
background_2 = Actor("background.png", (WIDTH // 2 + WIDTH, HEIGHT // 2))

# Load image of the aircraft
aircraft = Actor("aircraft.png", (100, HEIGHT // 2))

# Load image of the obstacle
meteor_1 = Actor("meteor.png", (WIDTH, HEIGHT // 2))
meteor_2 = Actor("meteor.png", (WIDTH + 900, HEIGHT // 2))
stone_1 = Actor("stone.png", (WIDTH + 450, HEIGHT // 2))
stone_2 = Actor("stone.png", (WIDTH + 1350, HEIGHT // 2))

# Load image of the fuel tank 
fuel = Actor("fuel_tank.png", (5000,600))

# Load game over image
game_over = Actor("game_over.png", (WIDTH // 2, HEIGHT // 2))

# Reset initial values  
def reset_game():
    global i, j, lives, score, level, speed, start, show_info
    i = 1
    j = 1
    lives = 5
    score = 0
    level = 1
    speed = 6
    show_info = False  

# Define the draw function
def draw():
    screen.clear()
    
    # Set up the menu
    if not start and not show_info:
        menu.draw()
        screen.draw.rect(button_start, 'black')
        screen.draw.rect(button_info, 'black')
        screen.draw.text("Start Game", center=button_start.center, color='black', fontsize=50)
        screen.draw.text("Show Info", center=button_info.center, color='black', fontsize=50)
 
    # Start the game
    elif start:
        if lives > 0:
            # Draw the images
            background_1.draw()    
            background_2.draw()    
            aircraft.draw()       
            meteor_1.draw()
            meteor_2.draw()           
            fuel.draw()
            if i > 3:       # Draw the image of stone_1 after passing level 3
                stone_1.draw()
            if i > 4:       # Draw the image of stone_2 after passing level 4
               stone_2.draw()
                
            # Display the score, lives and level
            screen.draw.text(f"Score: {score}", color="White", topleft=(10, 20), fontsize=40)
            screen.draw.text(f"Lives: {lives}", color="White", topleft=(10, 50), fontsize=40)
            screen.draw.text(f"LEVEL: {level}", (500, 20), color="White", fontsize=100)
                
        elif lives == 0:
            music.stop()        # Stop the music
            # Display the game over message and final score
            game_over.draw()
            screen.draw.text("GAME OVER", color="Red", center=(600, 200), fontsize=200)
            screen.draw.text(f"Final Score: {score}", color="Black", center=(600, 400), fontsize=70)
            screen.draw.text("Play Again", center=button_restart.center, color='black', fontsize=50)
            screen.draw.text("Go to menu", center=button_menu.center, color='black', fontsize=50)
       
# Define the function to handle mouse cliks
def on_mouse_down(pos):
    global start, show_info
    
    if button_start.collidepoint(pos):
        start = True
        show_info = False
        play_music()        # Play the background music
        
    elif button_info.collidepoint(pos):
        start = False
        show_info = True
        
    if button_restart.collidepoint(pos):
        reset_game()
        start = True
        play_music()        # Play the background music
        
    elif button_menu.collidepoint(pos):
        reset_game()
        start = False

# Define the function to take x-coordinate of meteors
def get_x(meteor):
    if meteor == meteor_1:      # Take the x-coordinate of meteor_1
        return meteor_1.x
    elif meteor == meteor_2:    # Take the x-coordinate ot meteor_2
        return meteor_2.x
        
# Define the update function   
def update():
    global lives, score, level, speed, i, j, start , show_info
    
    # Stopping the start of the game in the mune
    if not start and not show_info:
        return
    
    # Stopping the game after game is over
    if lives == 0:
        return
    
    # Increace the level with respect to scrore
    if score == 5 * i:
        i += 1
        level += 1      
        
        if i < 3:       # Increace the speed with respect to scrore
            speed = 4 * i
            
        else:           # Keeping the speed at a constant value
            speed = 12
    
    # Move the background_1 image to the left
    background_1.x -= 5
    
    if background_1.right < 1:       # Reset the background_1 image position
        background_1.left = 1200
    
    # Move the background_2 image to the left
    background_2.x -= 5
    
    if background_2.right < 1:       # Reset the background_2 image position
        background_2.left = 1200
        
    # Move the meteor_1 image to the left
    meteor_1.x -= speed

    if meteor_1.right < 1:        # Reset the meteor_1 image position             
        meteor_1.left = 1800
        meteor_1.y = random.randint(150, 650)     # Randomize the y-coordinate of the mateor_1
        score += 1      # Increase the score by 1
        
    # Move the meteor_2 image to the left
    meteor_2.x -= speed

    if meteor_2.right < 1:       # Reset the meteor_2 image position             
        meteor_2.left = 1800
        meteor_2.y = random.randint(150, 650)     # Randomize the y-coordinate of the mateor_2
        score += 1      # Increase the score by 1
        
    # Move the fuel image to the left
    fuel.x -= speed

    if fuel.right < 1:      # Reset the fuel image position
        fuel.left = 4000 * j
        fuel.y = random.randint(150, 650)
            
    if i > 3:
        # Move the stone_1 image to the left
        stone_1.x -= speed
        
        if stone_1.right < 1:       # Reset the stone_1 image position
            meteor_x = get_x(meteor_1)      # Take x-coordinate of meteor_1
            stone_1.x = meteor_x + 450
            stone_1.y = random.randint(150, 650)        # Randomize the y-coordinate of the stone_1
            score += 1      # Increase the score by 1
            
    if i > 4:
        # Move the stone_2 image to the left
        stone_2.x -= speed
        
        if stone_2.right < 1:       # Reset the stone_2 image position
            meteor_2_x = get_x(meteor_2)     # Take x-coordinate of meteor_2
            stone_2.x = meteor_2_x + 450
            stone_2.y = random.randint(150, 650)        # Randomize the y-coordinate of the stone_2
            score += 1      # Increase the score by 1    
        
    # Checkibg collision between the aircraft and the meteor
    if meteor_1.colliderect(aircraft):
      
        meteor_2_x = get_x(meteor_2)      # Take x coordinate of meteor_2 
        meteor_1.x = meteor_2_x + 900     # Reset the x-coordinate of mateor_1
        meteor_1.y = random.randint(150, 650)     # Randomize the y-coordinate of the meteor_1
        lives -= 1      # Reduce the lives by 1
        sounds.crashing.play()      # Play crashing sound
        
    # Checkibg collision between the aircraft and the meteor2
    if meteor_2.colliderect(aircraft):
   
        meteor_x = get_x(meteor_1)      # Take x coordinate of meteor_1
        meteor_2.x = meteor_x + 900     # Reset the x-coordinate of mateor_2  
        meteor_2.y = random.randint(150, 650)     # Randomize the y-coordinate of the meteor_2 
        lives -= 1      # Reduce the lives by 1
        sounds.crashing.play()      # Play the crashing sound
        
    # Checking collision between the aircraft and fuel tank
    if fuel.colliderect(aircraft):
        j += 1      # Increase the x-coordinate of the fuel tank
        fuel.x = 4000 * j       # Reset the x-coordinate of the fuel tank
        fuel.y = random.randint(150, 650)       # Randomize the y-coordinate of the fuel tank
        if lives > 5:       # Increase the lives by 1 when lives are less than 5
            lives += 1  
        sounds.fuel_crashing.play()        # Play the crashing sound   

    # Checking collision between the aircraft and stone_1
    if i > 3 and stone_1.colliderect(aircraft):
        meteor_x = get_x(meteor_1)      # Take x-coordinate of meteor_1 
        stone_1.x = meteor_x + 450      # Reset x-coordinate of stone_1
        stone_1.y = random.randint(150, 650)        # Randomize the y-coordinate of the stone_1
        lives -= 1      # Increase the lives by 1   
        sounds.crashing.play()      # Play the crashing sound
    
    # Checking the collision between the aircraft and stone_2    
    if i > 4 and stone_2.colliderect(aircraft):
        meteor2_x = get_x(meteor_2)     # Take x-coordinate of meteor_2
        stone_2.x = meteor2_x + 450     # reset x-coordinate of stone_2
        stone_2.y = random.randint(150, 650)        # Randomize the y-coordinate of the stone_2
        lives -= 1      # Increase the lives by 1 
        sounds.crashing.play()      # Play the crashing sound
        
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