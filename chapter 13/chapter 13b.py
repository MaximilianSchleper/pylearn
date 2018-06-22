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

screen_width = 700
screen_height = 400

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
        self.rect.y = random.randrange(-100, -10)
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

class Game():
    ''' Attributes '''
    # all the data we need to run the game

    # sprite lists
    block_list = None
    all_sprites_list = None
    player = None
    game_over = False

    ''' methods '''
    # setup the game
    def __init__(self):
        self.score = 0
        self.game_over = False

        # create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the block sprites
        for i in range(50):
            block = Block(BLACK, 20, 15)

            block.rect.x = random.randrange(screen_width - 20)
            block.rect.y = random.randrange(screen_height - 15)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

        # Create the player
        self.player = Player(RED, 20, 15)
        self.all_sprites_list.add(self.player)

    # closing window and restarting game
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    # this method is rin each frame. it updates positions and checks for collisions
    def run_logic(self):

        if not self.game_over:
            # move all the sprites
            self.all_sprites_list.update()

            # see if player collided with anything
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            #check list for collisions
            for block in blocks_hit_list:
                self.score += 1
                print(self.score)

            if len(self.block_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        screen.fill(WHITE)

        if self.game_over:
            # display a text in the middle of the screen
            font = pygame.font.SysFont("serif", 45)
            text1 = font.render("Game Over!", True, BLACK)
            x = (screen_width // 2) - (text1.get_width() // 2)
            y = (screen_height // 2) - (text1.get_height() // 2) - 25
            screen.blit(text1, [x, y])

            font = pygame.font.SysFont("serif", 25)
            text2 = font.render("Click to restart", True, BLACK)
            x = (screen_width / 2) - (text2.get_width() // 2)
            y = (screen_height // 2) - (text2.get_height() // 2) + 25
            screen.blit(text2, [x, y])
        # if game is not over
        else:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()

def main():

    pygame.init()

    size = [screen_width, screen_height]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)

    # create ort objects and set the data
    done = False
    clock = pygame.time.Clock()
    game = Game()

    ''' Main Loop '''
    while not done:
        # process events#
        done = game.process_events()
        # update objects
        game.run_logic()
        # draw frame
        game.display_frame(screen)
        # pause for next frame
        clock.tick(60)

    # close window and exit
    pygame.quit()

if __name__ == '__main__':
    main()