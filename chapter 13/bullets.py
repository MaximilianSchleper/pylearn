""" Pygame base template """

''' Imports '''
import pygame
import random

''' Globals '''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

''' Classes '''

class Block(pygame.sprite.Sprite):
    # this class represents a block
    def __init__(self, color):
        super.__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()

''' Game Class '''

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

            block.rect.x = random.randrange(SCREEN_WIDTH - 20)
            block.rect.y = random.randrange(SCREEN_HEIGHT- 15)

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
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [x, y])
        # if game is not over
        else:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()

''' Main function '''

def main():

    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
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