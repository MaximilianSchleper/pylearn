# todo: Step 9 and put more stuff in objects maybe

""" collecting sprites """

''' Imports '''
import pygame
import random

''' Globals '''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400


''' Classes '''

class Block(pygame.sprite.Sprite):
    # this class represents a block
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    # this class represents the player
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #speed
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

''' Game class '''

class Game():
    ''' Attributes '''
    # all the data we need to run the game

    # setup the game
    def __init__(self):
        self.score = 0
        self.game_over = False
        # Select the font to use, size, bold, italics
        self.font = pygame.font.SysFont('Calibri', 25, True, False)

        # create sprite lists
        self.good_block_list = pygame.sprite.Group()
        self.bad_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(50):
            self.block = Block(GREEN)

            self.block.rect.x = random.randrange(SCREEN_WIDTH - 20)
            self.block.rect.y = random.randrange(300)
            self.good_block_list.add(self.block)
            self.all_sprites_list.add(self.block
                                      )
        for i in range(50):
            self.block = Block(RED)

            self.block.rect.x = random.randrange(SCREEN_WIDTH - 20)
            self.block.rect.y = random.randrange(300)
            self.bad_block_list.add(self.block)
            self.all_sprites_list.add(self.block)

        self.player = Player(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT - 20)
        self.all_sprites_list.add(self.player)

    ''' methods '''

    # closing window and restarting game
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if self.game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.__init__()

            # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 3)

            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -3)

        return False

    # this method is run each frame. it updates positions and checks for collisions
    def run_logic(self):

        # sounds (how to fix the delay????????) how to import sounds globaly?
        wall_hit_sound = pygame.mixer.Sound("sfx_sounds_impact1.wav")
        good_block_sound = pygame.mixer.Sound("sfx_coin_double1.wav")
        bad_block_sound = pygame.mixer.Sound("sfx_sounds_damage3.wav")

        if not self.game_over:
            # move all the sprites
            self.all_sprites_list.update()

            # check if x_coord is out of screen bounderies
            if self.player.rect.x < 0:
                self.player.rect.x = 0
                wall_hit_sound.play()
            elif self.player.rect.x > SCREEN_WIDTH - 20:
                self.player.rect.x = SCREEN_WIDTH - 20
                wall_hit_sound.play()

            # check if y_coord is out of screen bounderies
            if self.player.rect.y < 0:
                self.player.rect.y = 0
                wall_hit_sound.play()
            elif self.player.rect.y > SCREEN_HEIGHT - 20:
                wall_hit_sound.play()
                self.player.rect.y = SCREEN_HEIGHT - 20

            # check for collisions
            self.good_block_hit_list = pygame.sprite.spritecollide(self.player, self.good_block_list, True)
            for i in self.good_block_hit_list:
                self.score += 1
                good_block_sound.play()

            self.bad_block_hit_list = pygame.sprite.spritecollide(self.player, self.bad_block_list, True)
            for i in self.bad_block_hit_list:
                self.score -= 1
                bad_block_sound.play()

            # game over if all good sprites are collected
            if len(self.good_block_list) == 0:
                self.game_over = True


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
            text2 = font.render("Press space to restart", True, BLACK)
            #x = (SCREEN_WIDTH / 2) - (text2.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (text2.get_height() // 2) + 25
            screen.blit(text2, [x, y])

            if self.score != 0:
                font = pygame.font.SysFont("serif", 15)
                score_text = font.render("Your score is: " + str(self.score), True, BLACK)
                y = (SCREEN_HEIGHT // 2) - (text2.get_height() // 2) + 50
                screen.blit(score_text, [x, y])

        # if game is not over
        else:
            self.all_sprites_list.draw(screen)

            # display score
            # Render the text. "True" means anti-aliased text.
            # Black is the color. This creates an image of the
            # letters, but does not put it on the screen
            text = self.font.render("score: "+ str(self.score), True, BLACK)
            screen.blit(text, [20, 360])

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