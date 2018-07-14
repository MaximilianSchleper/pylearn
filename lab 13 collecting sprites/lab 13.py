""" collecting sprites """

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
        super().__init__()                     # super()

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    # this class represents the player
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = SCREEN_HEIGHT - 30

''' Game class '''

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

        for i in range(50):
            self.block = Block(GREEN)

            self.block.rect.x = random.randrange(SCREEN_WIDTH - 20)
            self.block.rect.y = random.randrange(300)
            self.block_list.add(self.block)
            self.all_sprites_list.add(self.block)


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


    def display_frame(self, screen):
        screen.fill(WHITE)

        if self.game_over:
            # display a text in the middle of the screen
            # display a text in the middle of the screen
            font = pygame.font.SysFont("serif", 45)
            text1 = font.render("Game Over!", True, BLACK)
            x = (SCREEN_WIDTH // 2) - (text1.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (text1.get_height() // 2) - 25
            screen.blit(text1, [x, y])

            font = pygame.font.SysFont("serif", 25)
            text2 = font.render("Click to restart", True, BLACK)
            x = (SCREEN_WIDTH / 2) - (text2.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (text2.get_height() // 2) + 25
            screen.blit(text2, [x, y])
        # if game is not over
        else:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()

''' Main function '''

def main():

    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Collecting Sprites")
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