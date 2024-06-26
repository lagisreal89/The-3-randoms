#literally the start of the file nothing much to see 
import pygame
import sys
from sprites import *
from config import *

# initalize pygame
class Game:
    def __innit__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("arial", 32)
        self.running = True

    def new(self):
        # add a new game start
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

# Set the width and height of the screen (width, height)
SCREEN_SIZE = (800, 600)

# Create the screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# Set the title of the window
pygame.display.set_caption("My Pygame Window")

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()
