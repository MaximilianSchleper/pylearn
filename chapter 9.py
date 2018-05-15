"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from math import pi

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BLACK, [60+x, 170+y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150+x, 170+y], [75+x, 20+y],[x, 170+y]])
    pygame.draw.polygon(screen, GREEN, [[140+x, 120+y], [75+x, y], [10+x, 120+y]])
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    # ------------------------------shapes------------------------------------------
    draw_tree(screen, 0, 0)

    for i in range(10):
        draw_tree(screen, i * 60, 5)
    # ------------------------------shapes------------------------------------------

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()   # show the drawing after drawing invisibly

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()