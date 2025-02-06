# CO1010

# Import libraries
import pgzrun
import random

# Set up the screen
WIDTH = 1200
HEIGHT = 800

# Set up initial values
i = 1
j = 1
lives = 300
score = 0
level = 1
speed = 5 * i
start = False
show_info = False

# Draw rectangles for start and info buttons in menu
button_start = Rect((405, 480), (385, 85))
button_info = Rect((405, 635), (385, 85))

button_restart = Rect((140, 615), (385, 85))
button_menu = Rect((675, 615), (385, 85))

# Load the menu image
menu = Actor('gameinte.png', (WIDTH // 2, 400))

# Load the background images
background_1 = Actor('mm.png', (WIDTH // 2, 400))
background_2 = Actor('mm.png', (1800, 400))

# Load image of the aircraft
aircraft = Actor('aircraft.png', (100, 400))

# Load image of the obstacle
meteor = Actor('ulka2.png', (WIDTH, 400))
meteor2 = Actor('ulka2.png', (WIDTH + 900, 400))
#stone = Actor('555.png')

# Load image of the fuel 
fuel = Actor('fuel.png', (5000,600))

# Load game over image
game_over = Actor('over.png', (WIDTH // 2, 400))

# Reset initial values  
def reset_game():
    global i, j, lives, score, level, speed, start, show_info
    i = 1
    j = 1
    lives = 300
    score = 0
    level = 1
    speed = 5 * i
    show_info = False  

# Define the draw function
def draw():
    screen.clear()
    
    # Set up the menu
    if start == False and show_info == False:
        menu.draw()
        screen.draw.rect(button_start, 'black')
        screen.draw.rect(button_info, 'black')
        screen.draw.text("Start Game", center=button_start.center, color='black', fontsize=50)
        screen.draw.text("Show Info", center=button_info.center, color='black', fontsize=50)
 
    # Start the game
    elif start == True:
        if lives > 0:
            # Draw the images
            background_1.draw()    
            background_2.draw()    
            aircraft.draw()       
            meteor.draw()
            meteor2.draw()           
            fuel.draw()
        
            # Display the score, lives and level
            screen.draw.text(f"Score: {score}", color="White", topleft=(10, 20), fontsize=40)
            screen.draw.text(f"Lives: {lives}", color="White", topleft=(10, 50), fontsize=40)
            screen.draw.text(f"LEVEL: {level}", (500, 20), color="White", fontsize=100)
                
        elif lives == 0:
            # Display the game over message and final score
            game_over.draw()
            screen.draw.text("GAME OVER", color="Red", center=(600, 400), fontsize=200)
            screen.draw.text(f"Final Score: {score}", color="Yellow", center=(600, 500), fontsize=70)
            screen.draw.text("Play Again", center=button_restart.center, color='black', fontsize=50)
            screen.draw.text("Go to menu", center=button_menu.center, color='black', fontsize=50)
            
# Define the function to handle mouse cliks
def on_mouse_down(pos):
    global start, show_info
    
    if button_start.collidepoint(pos):
        start = True
        show_info = False
        
    elif button_info.collidepoint(pos):
        start = False
        show_info = True
        
    if button_restart.collidepoint(pos):
        reset_game()
        start = True
        
    elif button_menu.collidepoint(pos):
        reset_game()
        start = False

# Define the function to get x coordinate of meteors
def get_x(meteor):
    if meteor == meteor:
        return meteor.x
    
    elif meteor == meteor2:
        return meteor2.x
        
# Define the update function   
def update():
    global lives, score, level, speed, i, j, start , show_info
    
    if start == False and show_info == False:
        return
    
    # Stopping the game when game is over
    if lives == 0:
        return
    
    # Increace the level with respect to scrore
    if score == 2 * i:
        i += 1
        level += 1
        
        if i < 4:
            speed = 5 * i
            
        else:
            speed = 10
            

            
        
    # Move the background_1 image to the left
    background_1.x -= 5
    
    if background_1.right < 1:       # Reset the background_1 image position
        background_1.left = 1200
    
    # Move the background_2 image to the left
    background_2.x -= 5
    if background_2.right < 1:       # Reset the background_2 image position
        background_2.left = 1200
        
    # Move the meteor image to the left
    meteor.x -= speed
    
    # Reset the meteor image position
    if meteor.right < 1:             
        meteor.left = 1800
        meteor.y = random.randint(150, 650)     # Randomize the meteor position of y-axis
       
        score += 1      # Increase the score by 1
        
    # Move the meteor image to the left
    meteor2.x -= speed
        
    # Reset the meteor2 image position
    if meteor2.right < 1:             
        meteor2.left = 1800
        meteor2.y = random.randint(150, 650)     # Randomize the meteor position of y-axis
       
        score += 1      # Increase the score by 1
        
    # Move the fuel image to the left
    fuel.x -= speed
        
    # Reset the fuel image position
    if fuel.right < 1:
        fuel.left = 4000 * j
        fuel.y = random.randint(150, 650)
        

        
    # Checkibg collision between the aircraft and the meteor
    if meteor.colliderect(aircraft):
        
        # Reset the meteor position
        meteor2_x = get_x(meteor2)      # Get x coordinate of meteor2 
        meteor.x = meteor2_x + 900
        meteor.y = random.randint(150, 650)     # Randomize the meteor position of y-axis
        
        lives -= 1      # Reduce the lives by 1
        
    # Checkibg collision between the aircraft and the meteor2
    if meteor2.colliderect(aircraft):
        
        # Reset the meteor2 positionno
        meteor_x = get_x(meteor)        # Get x coordinate of meteor
        meteor2.x = meteor_x + 900
        meteor2.y = random.randint(150, 650)     # Randomize the meteor2 position of y-axis
        
        lives -= 1      # Reduce the lives by 1
        
    # Checking collision between the aircraft and heart
    if fuel.colliderect(aircraft):
        j += 1    # Increase the heart psotion of x-axis
        
        # Reset the heart position
        fuel.x = 4000 * j
        fuel.y = random.randint(150, 650)
        
        # Increase the lives by 1 when lives are less than 5
        if lives > 5:
            lives += 1      

    # Move the aircraft up and down    
    if keyboard.down:
        if aircraft.y < 650:    # Limit bottom movement
            aircraft.y += 10
            
    elif keyboard.up:
        if aircraft.y > 150:    # Limit top movement
            aircraft.y -= 10
       
# Run the game
pgzrun.go()