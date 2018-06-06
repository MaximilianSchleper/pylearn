import pygame
import random

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

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting x position of the rectangle
# Note how this is outside the main while loop.
rect_x = 50
rect_y = 50

x_speed = 5
y_speed = 5

rect_list = []

for i in range(20):
    rect_x = random.randrange(0, 700)
    rect_y = random.randrange(0, 500)
    rect_list.append([rect_x, rect_y])


# snow_list = []
#
# for i in range(400):
#     x = random.randrange(0, 700)
#     y = random.randrange(-500, 0)
#     snow_list.append([x, y])

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
    screen.fill(BLACK)

    # --- Drawing code should go here

            # bouncing rectagle

# doesnt work
    for i in range(len(rect_list)):
        pygame.draw.rect(screen, WHITE, [rect_list[i], 50, 50])
        rect_x += x_speed
        rect_y += y_speed

    if rect_y > 450:
        y_speed *= -1
    if rect_x > 650:
        x_speed *= -1


    if rect_y < 0:
        y_speed *= -1
    if rect_x < 0:
        x_speed *= -1

            # animating snow

    # for i in range(len(snow_list)):
    #     pygame.draw.circle(screen, WHITE, snow_list[i], 2)
    #
    #     snow_list[i][1] += 2
    #
    #     if snow_list[i][1] > 500:
    #         y = random.randrange(-500, 0)
    #         snow_list[i][1] = y
    #         x = random.randrange(0, 700)
    #         snow_list[i][0] = x


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()