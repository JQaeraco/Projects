# Pygame_Drawing
# Author: Josh
# 9 November 2021

# Get introduced to pygame and fraw objects on screen
import random
import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PINK = (255, 190, 190)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"

def main() -> None:
    """Driver of the Phython script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)
    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    # Create the main loop
    while not done:
        # Make space for the event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Change the environment

        # Draw the environment
        screen.fill(PINK)
        for i in range(11):
            pygame.draw.rect(screen, RED, [100+i*50, 100+i*10, 75, 30+i*i])
        pygame.draw.circle(screen, GREEN, [600, 300], 100)
        for i in range(10):
            pygame.draw.arc(screen, BLUE,[90,70, 1000+i*4, 8600+i*3], 180, 480*i)
        for i in range(50):
            pygame.draw.circle(screen, (134, 189, 234), [i*random.randint(0, 800), i*random.randint(30, 600)], random.randint(7, 40))
        # Update the screen
        pygame.display.flip()
        # Tick the clock
        clock.tick(75)


if __name__ == "__main__":
    main()