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
class Ball():
    def __init__(self):
        # position
        self.x = 0
        self.y = 0

        # vector
        self.change_x = 0
        self.change_y = 0

        self.size = 10

        self.color = [255, 255, 255]

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 12
theBall.change_y = 11
theBall.color = [255, 0, 0]


def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [400, 400]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    click_sound = pygame.mixer.Sound("tone1.ogg")

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        if theBall.x > size[0] - theBall.size or theBall.x < 10:
            theBall.change_x *= -1
            click_sound.play()
        elif theBall.y > size[1] - theBall.size or theBall.y < 10:
            theBall.change_y *= -1
            click_sound.play()
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        theBall.move()
        theBall.draw(screen)
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