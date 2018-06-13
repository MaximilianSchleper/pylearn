import pygame

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# function definition below


def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [600, 375]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Slingshot racer")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    background_image = pygame.image.load("background1.jpg").convert()

    player_image = pygame.image.load("playerShip1_orange.png").convert()
    player_image.set_colorkey(BLACK)  # make backgroundcolor of ship image transparent

    click_sound = pygame.mixer.Sound("laser3.ogg")

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        player_position = pygame.mouse.get_pos()

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.blit(background_image, [0, 0])
        screen.blit(player_image, player_position)
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