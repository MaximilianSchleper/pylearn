"""
Pygame base template for opening a window, done with functions

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

# right x movement for space invaders
# when right is pressed and left is pressed and realesed it still goes right

import pygame

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_flo(screen, x, y):
    pygame.draw.ellipse(screen, GREEN, [x, y, 20, 30])



def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    x_coord = 340
    y_coord = 480

    x_speed = 0
    y_speed = 0

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                # if it was an arrow key adjust speed
                if event.key == pygame.K_LEFT:
                    x_speed -= 4
                elif event.key == pygame.K_RIGHT:
                    x_speed += 4


            # user let up on a key
            elif event.type == pygame.KEYUP:
                # if its an arrow key, reset speed to 0
                if event.key == pygame.K_LEFT:
                    x_speed += 4
                elif event.key == pygame.K_RIGHT:
                    x_speed -= 4

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        x_coord += x_speed
        y_coord += y_speed

        # check if x_coord is out of screen bounderies
        if x_coord < 0:
            x_coord = 0
        elif x_coord > size[0] - 20:
            x_coord = size[0] - 20

        # check if y_coord is out of screen bounderies
        if y_coord < 0:
            y_coord = 0
        elif y_coord > size[1] - 30:
            y_coord = size[1] - 30
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        draw_flo(screen, x_coord, y_coord)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


if __name__ == "__main__":
    main()