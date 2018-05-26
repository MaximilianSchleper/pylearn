"""
Flappy Flo
"""

import math
import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

y = 400
y_speed = 0

pygame.init()

size = (1200, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Flo")

def draw_flo(screen, x, y,):
    pygame.draw.circle(screen, BLACK, [x, y + y_speed], 20)

def fall(y, y_speed):
    y += y_speed
    y_speed += 1

def flap(y_speed):
    y_speed -= 10

def main():
    """ Main program. """

    clock = pygame.time.Clock()

    # Keep looking until someone wins
    done = False

    while not done:
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
        draw_flo(screen, 100, 400)
        fall(y, y_speed)
        if event.type == pygame.K_UP:
            flap(y_speed)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

        # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    main()