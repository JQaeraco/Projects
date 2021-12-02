# Pygame relaxing snowscape
# Author: Ubial
# 2021 Version


import pygame
import random


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "<<Relaxing Snowscape>>"


class Snowflake:
    """Represents snowing on the background

    Atrributes:
    size: size of the snowflakes
    coordinate: {x: int, y: int)
    vel: speed of the snowflakes
    colour: rgb tuple
    """

    def __init__(self):
        self.size = 2
        self.coordinate = [random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)]
        self.y_vel = 1
        self.colour = WHITE

    def update(self):
        """Update the location of the snow"""
        self.coordinate[1] += self.y_vel

        if self.coordinate[1] > SCREEN_HEIGHT:
            self.coordinate = [
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(-25, 0)
            ]


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    snow = Snowflake()
    bg_image = pygame.image.load("./images/galaxy_bg.jpg")
    num_snowflakes = 250
    snowflakes = []

    # Create snowflakes in foreground
    for i in range(num_snowflakes):
        close_snowflake = Snowflake()
        close_snowflake.size = random.choice([3,4])
        close_snowflake.y_vel = random.choice([1, 2])
        snowflakes.append(close_snowflake)

    # Create snowflakes in the mid ground
    for i in range(num_snowflakes-100):
        close_snowflake = Snowflake()
        close_snowflake.size = random.choice([3, 4])
        close_snowflake.y_vel = random.choice([2, 3])
    # Create snowflakes in background
    for i in range(num_snowflakes):
        snowflakes.append(Snowflake())

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        for snow in snowflakes:
            snow.update()
        # ----------- DRAW THE ENVIRONMENT
        # screen.fill(BGCOLOUR)      # fill with bgcolor
        screen.blit(bg_image, (0, 0))
        pygame.draw.rect(screen, (150, 150, 255), [0, 500, SCREEN_WIDTH, 300])
        # Create a snowflake in foreground
        for snow in snowflakes:
            pygame.draw.circle(screen, snow.colour, snow.coordinate, snow.size)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
