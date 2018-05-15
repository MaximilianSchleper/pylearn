# Google Chrome dino game
# jump over kactus and duck under flying dinos

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1200, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chrome Dino Game")

# Loop until the user clicks the close button.
done = False

ground_level = size[1] / 2
x_speed = 0
y_speed = 0
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    ducking = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ducking = 60

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here

    # ground
    pygame.draw.line(screen, BLACK, [0, ground_level], [1200, ground_level])


    # dino
    pygame.draw.rect(screen, BLACK, [100, ground_level - (100 - ducking), 40, (100 - ducking)], 2)


    # obstacles

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()