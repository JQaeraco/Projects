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
MAX_HUNGER = 50
ENDGAME_REASONS = {
    "LOSE_AGENTS": 1,
}

class Game:
    """Represent our game engine
    Attribute:
        done: describes if the game is
                finished or not - bool
        distance_traveled: Describe the distance that we've traveled so far in this game, in km
        amount_of_sustenance: How much food we have left in our inventory
        agents_distance: describes the distance between the player and the agent.
        fuel: Describe the amount of fuel remaining, starts off at 50
        hunger: describes how hungry thr player is, represented by a number between 0-50, if hunger goes beyond 50, game
        is over.
        hunger: describes how hungry our player is,
        represented by a number between 0-50,
        if hunger goes beyond 50, game is over
        endgame_reason: shows the index of the game ending text from midnight_rider_text.py
    """

    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_of_sustenance = MAX_FOOD
        self.agents_distance = -20
        self.fuel = MAX_FUEL
        self.hunger = 0
        self.endgame_reason = 0


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
        agents_distance_now = random.randrange(7, 15)
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
            self.agents_distance += agents_distance_now
            print(midnight_rider_text.REFUEL)
            time.sleep(1.3)
        elif user_choice ==  "c":
            # Move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_traveled += player_distance_now
            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # Burn the fuel
            self.fuel -= random.randrange(5, 11)
            # Give the player some feedback
            print(f"---------ZOOOOOOM.")
            print(f"----------You traveled {player_distance_now} km")
        elif user_choice == "b":
            # Move the player slowly
            player_distance_now = random.randrange(5, 10)
            self.distance_traveled += player_distance_now
            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # Burn the fuel
            self.fuel -= random.randrange(3, 8)
            # Give the player some feedback
            print(f"---------You drive conservatively.")
            print(f"----------You traveled {player_distance_now} km")
        elif user_choice == "a":
            # consume one food if we have some available
            if self.amount_of_sustenance > 0:
                self.amount_of_sustenance -= 1

                # Decrease hunger to 0
                self.hunger = 0
                # Give the player some feedback
                print(midnight_rider_text.EAT_FOOD)
            else:
                print(midnight_rider_text.NO_FOOD)

        if user_choice in ["b", "c", "d"]:
            self.hunger += random.randrange(8, 18)


    def upkeep(self) -> None:
        """Give the user reminders of hunger"""
        if self.hunger > 40:
            print(midnight_rider_text.SEVERE_HUNGER)
        elif self.hunger > 25:
            print(midnight_rider_text.HUNGER)

    def check_endgame(self) -> None:
        """Check to see if win/lose conditions are met.
        If they're met, change the self.done flag."""
        if self.agents_distance >= 0:
            # Allows us to quit the while loop
            self.done = True
            # Helps with printing the right ending
            self.endgame_reason = ENDGAME_REASONS["LOSE_AGENTS"]

def main() -> None:
    game = Game() # starting a new game
    # game.introduction()

    # Main Loop:
    while not game.done:
        game.upkeep()
        # Display the choices to the player
        game.show_choices()
        # Ask the player what they want to do
        # Change the state of environment
        game.get_choice()
        # Check win/lose conditions
        game.check_endgame()

    time.sleep(2)
    # Print out the ending
    game.typewriter_effect(
        midnight_rider_text.ENDGAME_TEXT[game.endgame_reason]
    )

if __name__ == "__main__":
    main()

