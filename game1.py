# Import libraries
import pgzrun

# Set up the screen
WIDTH = 1200
HEIGHT = 800

# Load the background images
background_1 = Actor('mm.png', (600, 400))
background_2 = Actor('mm.png', (1800, 400))

# Load image of the aircraft
aircraft = Actor('aircraft.png', (200, 400))

# Load image of the obstacle
meteor = Actor('ulka2.png', (1200, 400))

# Define the draw function
def draw():
    screen.clear()
    background_1.draw()     # Draw the background_1 image
    background_2.draw()     # Draw the background_2 iamge
    aircraft.draw()         # Draw the aircraft image
    meteor.draw()           # Draw the meteor image
    
# Define the update function   
def update():
    
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
    if meteor.right < 1:             # Reset the meteor image position
        meteor.left = 1200
# Run the game
pgzrun.go()