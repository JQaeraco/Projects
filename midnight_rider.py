# Midnight Rider

import random
import sys
import textwrap
import time
import midnight_rider_text

# A text based game of intrigue and illusion

#CONSTANTS
MAX_FUEL = 50
MAX_FOOD = 3

class Game:
    """Represent our game engine
    Attribute:
        done: describes if the game is
                finished or not - bool
        distance_traveled: Describe the distance that we've traveled so far in this game, in km
        amount_of_sustenance: How much food we have left in our inventory
        agents_distance: describes the distance between the player and the agent.
        fuel: Describe the amount of fuel remaining, starts off at 50
    """

    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_of_sustenance = MAX_FOOD
        self.agents_distance = -20
        self.fuel = MAX_FUEL

    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)


    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect."""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        time.sleep(1)
        print(midnight_rider_text.CHOICES)

    def get_choice(self) -> None:
        """Gets the user's choice and changes
        the environment"""
        # Get the user's response
        user_choice = input().strip(",.?!").lower()

        # Based on their choice, change the attribute of the class
        if user_choice == "e":
            print("---Status Check---")
            print(f"Distance traveled: {self.distance_traveled}kms")
            print(f"Fuel remaining: {self.fuel} L")
            print(f"Amount of food left: {self.amount_of_sustenance}")
            print(f"Agent's Distance: {abs(self.agents_distance)} km behind")
            print("------")
            time.sleep(1.3)

        elif user_choice == "q":
            self.done = True
        elif user_choice == "d":
            self.fuel = MAX_FUEL
            self.agents_distance += random.randrange(7, 15)
            print(midnight_rider_text.REFUEL)
            time.sleep(1.3)
def main() -> None:
    game = Game() # starting a new game
    # game.introduction()

    # Main Loop:
    while not game.done:
        # Display the choices to the player
        game.show_choices()
        # Ask the player what they want to do
        # Change the state of environment
        game.get_choice()
        # Check win/lose conditions

if __name__ == "__main__":
    main()

