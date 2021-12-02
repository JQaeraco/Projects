# Pygame collecting_blocks
# Author: Ubial
# 2021 Version

import random
import time
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


class Player(pygame.sprite.Sprite):
    """Describes a player object
    A subclass of pygame.sprite.Sprite
    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
        hp: describes how much health our player has
    """
    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.image.load("./images/kefka.png")
        self.image = pygame.transform.scale(self.image, (204 * 0.15, 304 * 0.15))
        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()

        # initial health points
        self.hp = 200

    def hp_remaining(self) -> int:
        """Return the percent of health remaining"""
        return self.hp / 200

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


class Enemy(pygame.sprite.Sprite):
    """The enemy sprites

    Attributes:
        image: Surface that is the visual representation of the sprite
        rect: Rect (x, y, width, height)
        x_vel: x velocity
        y_vel: y velocity
    """
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/enemy_spider.png")
        self.image = pygame.transform.scale(self.image, (148 * 0.5, 125 * 0.5))

        self.rect = self.image.get_rect()
        # Define the initial location
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )
        # Define initial velocity
        self.x_vel = random.choice([-4, -3, 3, 4])
        self.y_vel = random.choice([-4, -3, 3, 4])

    def update(self):
        # update the x-coordinate
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # X
        # If enemy is too far to the left
        if self.rect.left < 0:
            self.rect.x = 0
            self.x_vel = -self.x_vel
        # If enemy is too far to the right
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = -self.x_vel

        # Y
        if self.rect.y < 0:
            self.rect.y = 0
            self.y_vel = -self.y_vel
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100
    score = 0
    num_enemies = 10
    time_start = time.time()
    time_invincible = 5

    font = pygame.font.SysFont("Arial", 25)

    # Create a groups to hold sprites
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # Create all the block sprites and add to block_sprites
    for i in range(num_blocks):
        # Create a block ( set its parameters)
        block = Block(VIRIDIAN_GREEN, 20, 15)


        # Set a random location for the block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)

        # Add the block to the block_sprites Group
        # Add the block to the all_sprites Group
        block_sprites.add(block)
        all_sprites.add(block)


    # Create enemy sprites
    for i in range(num_enemies):
        # Create an enemy
        enemy = Enemy()
        # Add it to the sprites
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)


    # Create the Player block
    player = Player()

    # Add the player to all_sprites groups
    all_sprites.add(player)

    pygame.mouse.set_visible(False)

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - player.rect.width / 2
        player.rect.y = mouse_pos[1] - player.rect.height / 2

        # Update the location of all sprites
        all_sprites.update()

        # Check all collisons between the player and all blocks


        # Check all collisions between player and the ENEMIES
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)

        # Set a time for invincibility at the beginning of the game
        if time.time() - time_start > time_invincible:
            for enemy in enemies_collided:
                if player.hp > 0:
                    player.hp -= 3
                    print(player.hp) # debugging

            blocks_collided = pygame.sprite.spritecollide(player, block_sprites, True)

            for block in blocks_collided:
                score += 1

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BLACK)      # fill with bgcolor

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the score on the screen
        screen.blit(
            font.render(f"Score: {score}", True, WHITE),
            (5, 5)
        )

        # Draw a health bar
        # Draw background rectangle
        pygame.draw.rect(screen, BLUE, [580, 5, 215, 20])
        # Draw the foreground rectangle which is the remaining health
        life_remaining = 215 - int(215 * player.hp_remaining())
        pygame.draw.rect(screen, RED, [580, 5, life_remaining, 20])



        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()