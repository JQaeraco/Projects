# Pygame dvd_screensaver
# Author: Josh
# 2021 Version


import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH  = 1024 * 1.3
SCREEN_HEIGHT = 683 * 1.3
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "DVD Screen Saver"


class Dvdimage:
    """REpresents a dvdimage on screen

        Atrributes:
        x, y: coordinates of top-left corner
        width: width of image in px
        height: height of image in px
        img: visual representation of our Dvdimage
        x-vel: x velocity in px/sec
        y-vel: y velocity in px/sec
    """
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 180
        self.height = 180
        self.img = pygame.image.load("./images/dvdimage.png")
        self.x_vel = 5 * 4
        self.y_vel = 3 * 4

    def rect(self) -> pygame.rect:
        """Returns pygame.rect that represents the dvd_image"""
        return [self.x, self.y, self.width, self.height ]

    def update(self) -> None:
        """Updates the Dvdimage with every tick"""
        # update the x-coordinate
        self.x += self.x_vel
        # If Dvdimage is too far to the left
        if self.x < 0:
            self.x = 0
            self.x_vel = -self.x_vel
        # If Dvdimage is too far to the right
        if self.x + self.width >SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
            self.x_vel = -self.x_vel
        if self.y < 0:
            self.y = 0
            self.y_vel = -self.y_vel
        if self.y + self.height >SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
            self.y_vel = -self.y_vel

        # update the y-coordinate
        self.y += self.y_vel


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()
    bg_image = pygame.image.load("./images/galaxy_bg.jpg")

    # Transform the size of the bg_image
    bg_image = pygame.transform.scale(bg_image, (1024 * 1.3, 683 * 1.3))
    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        dvd_image.update()

        # ----------- DRAW THE ENVIRONMENT
        # screen.fill(BGCOLOUR)     # fill with bgcolor
        screen.blit(bg_image, (0, 0))

        # pygame.draw.rect(screen, dvd_image.colour, dvd_image.rect())

        # .blit(<surface/img>, coords)
        screen.blit(dvd_image.img, (dvd_image.x, dvd_image.y))
        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
