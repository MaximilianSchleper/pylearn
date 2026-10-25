"""
Pygame base template for opening a window, done with functions

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame
import random

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # calls the sprite contructor
        super().__init__()
        # create an image of the block and fill it with color
        # this could also be an image loaded from a disk
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # fetch the rectangle object that has the dimensions of the image
        # update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def reset_pos(self):
        ''' reset positon to tio at random x called by update'''
        self.rect.y = random.randrange(-300, -10)
        self.rect.x = random.randrange(screen_width - 20)

    def update(self):
        '''called each frame'''
        self.rect.y += 1
        if self.rect.y > screen_height:
            self.reset_pos()



class Player(Block):
    def update(self):
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]
        self.rect.y = pos[1]


pygame.init()

# Set the width and height of the screen [width,height]
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# list is managed by Group class
block_list = pygame.sprite.Group()

# this is a list of every sprite. all blocks aswell as player block
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(screen_width - 20)
    block.rect.y = random.randrange(screen_height - 15)

    block_list.add(block)
    all_sprites_list.add(block)

player = Player(RED, 20, 15)
all_sprites_list.add(player)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # Clear the screen
    screen.fill(WHITE)

    # Calls update() method on every sprite in the list
    all_sprites_list.update()

    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)

        # Reset block to the top of the screen to fall again.
        block.reset_pos()

    # Draw all the spites
    all_sprites_list.draw(screen)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(30)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
