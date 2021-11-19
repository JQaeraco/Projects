# Pygame collecting_blocks
# Author: Ubial
# 2021 Version


import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
BLUE = (0,   0, 255)
VIRIDIAN_GREEN = (14, 149, 148)
ORANGE_SODA = (242, 84, 45)
WHEAT = (245, 223, 187)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Collecting Blocks"


class Block(pygame.sprite.Sprite):
    """"describes a block object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual representation of our Block
        rect: numerical represention of our block [x, y, width, height]"""

    def __init__(self, colour: tuple, width: int, height: int) -> None:
        """
        Arguements:
        :param colour: 3-tuple(r,g,b)
        :param width: width in pixels
        :param height: height in pixels
        """
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # Based on the image, create a rect for a block
        self.rect = self.image.get_rect()


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # Create a group of sprites to store ALL SPRITES
    all_sprites = pygame.sprite.Group()

    # Create the Player block
    player = Block(ORANGE_SODA, 20, 15)

    # Add the player to all_sprites groups
    all_sprites.add(player)

    # pygame.mouse.set_visible(False)

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect = mouse_pos

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(WHITE)      # fill with bgcolor

        # Draw all sprites


        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()