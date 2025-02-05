# Import libraries
import pgzrun
import random

# Set up the screen
WIDTH = 1200
HEIGHT = 800

# Set up initial values
i = 1
lives = 2
score = 0
level = 1
speed = 5 * i

# Load the background images
background_1 = Actor('mm.png', (600, 400))
background_2 = Actor('mm.png', (1800, 400))

# Load image of the aircraft
aircraft = Actor('aircraft.png', (100, 400))

# Load image of the obstacle
meteor = Actor('ulka2.png', (1200, 400))

# Define the draw function
def draw():
    screen.clear()
    if lives > 0:
        # Draw the images
        background_1.draw()    
        background_2.draw()    
        aircraft.draw()       
        meteor.draw()           
        
        # Display the score, lives and level
        screen.draw.text(f"Score: {score}", color="White", topleft=(10, 20), fontsize=40)
        screen.draw.text(f"Lives: {lives}", color="White", topleft=(10, 50), fontsize=40)
        screen.draw.text(f"LEVEL: {level}", (500, 20), color="White", fontsize=100)
    
    elif lives == 0:
       # Display the game over message and final score
        screen.draw.text("GAME OVER", color="Red", center=(600, 400), fontsize=200)
        screen.draw.text(f"Final Score: {score}", color="Yellow", center=(600, 700), fontsize=70)
    
        
# Define the update function   
def update():
    global lives, score, level, speed
    
    # Stopping the game when game is over
    if lives == 0:
        return
    
    # Move the background_1 image to the left
    background_1.x -= 5
    
    if background_1.right < 1:       # Reset the background_1 image position
        background_1.left = 1200
    
    # Move the background_2 image to the left
    background_2.x -= 5
    if background_2.right < 1:       # Reset the background_2 image position
        background_2.left = 1200
        
    # Move the meteor image to the left
    meteor.x -= 5
    
    # Reset the meteor image position
    if meteor.right < 1:             
        meteor.left = 1200
        meteor.y = random.randint(150, 650)     # Randomize the meteor position of y-axis
        score += 1      # Increase the score by 1
        
    # Checkibg collision between the aircraft and the meteor
    if meteor.colliderect(aircraft):
        
        # Reset the meteor position
        meteor.x = 1200
        meteor.y = random.randint(150, 650)     # Randomize the meteor position of y-axis
        lives -= 1      # Reduce the lives by 1
        
    # Move the aircraft up and down    
    if keyboard.down:
        if aircraft.y < 650:    # Limit bottom movement
            aircraft.y += 10
            
    elif keyboard.up:
        if aircraft.y > 150:    # Limit top movement
            aircraft.y -= 10
       
# Run the game
pgzrun.go()