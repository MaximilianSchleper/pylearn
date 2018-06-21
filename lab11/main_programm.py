"""
Pygame base template for opening a window, done with functions

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# function definition below
def draw_cart(screen, x, y):
    pygame.draw.rect(screen, RED, [x, y, 20, 20])
    pygame.draw.rect(screen, BLACK, [x, y, 4, 4])
    pygame.draw.rect(screen, BLACK, [x, y+16, 4, 4])
    pygame.draw.rect(screen, BLACK, [x+16, y, 4, 4])
    pygame.draw.rect(screen, BLACK, [x+16, y+16, 4, 4])


def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [700, 700]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("moon cart")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # load images
    background_image = pygame.image.load("moon-surface.jpg").convert()

    meteor_image = pygame.image.load("meteor.png").convert()
    meteor_image.set_colorkey(BLACK)

    ship_image1 = pygame.image.load("ship1.png").convert()
    ship_image1.set_colorkey(BLACK)
    ship_image2 = pygame.image.load("ship2.png").convert()
    ship_image2.set_colorkey(BLACK)
    ship_image3 = pygame.image.load("ship3.png").convert()
    ship_image3.set_colorkey(BLACK)

    car_sound = pygame.mixer.Sound("laser1.ogg")

    x_coord = 345
    y_coord = 345

    x_speed = 0
    y_speed = 0

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # user pressed a key down
            elif event.type == pygame.KEYDOWN:
                # if it was an arrow key adjust speed
                if event.key == pygame.K_LEFT:
                    x_speed = -4
                elif event.key == pygame.K_RIGHT:
                    x_speed = 4
                elif event.key == pygame.K_UP:
                    y_speed = -4
                elif event.key == pygame.K_DOWN:
                    y_speed = 4
                elif event.key == pygame.K_SPACE:
                    car_sound.play()

            # user let up on a key
            elif event.type == pygame.KEYUP:
                # if its an arrow key, reset speed to 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        x_coord += x_speed
        y_coord += y_speed

        # check if x_coord is out of screen bounderies
        if x_coord < 0:
            x_coord = 0
        elif x_coord > size[0]-20:
            x_coord = size[0]-20


        # check if y_coord is out of screen bounderies
        if y_coord < 0:
            y_coord = 0
        elif y_coord > size[1]-20:
            y_coord = size[1]-20
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.blit(background_image, [0, 0])

        draw_cart(screen, x_coord, y_coord)

        screen.blit(meteor_image, [500, 50])
        screen.blit(ship_image1, [50, 500])
        screen.blit(ship_image2, [200, 500])
        screen.blit(ship_image3, [500, 500])


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