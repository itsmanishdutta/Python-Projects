# Simple Text-Based Adventure Game
# Title: Forest & Island Quest
# Author: Manish Kumar Dutta.
# -----------------------------------------------------------
# Game Description:
# 1. The player wakes up in a mysterious forest.
# 2. They must search treasure boxes in 4 directions (N, S, E, W).
# 3. In the Forest (Level 1), the key is hidden in East side Box 3.
# 4. After finding the key, the player travels to an Island (Level 2).
# 5. On the Island, the DIAMOND is hidden in West side Box 3.
# 6. If the player finds the diamond, they win the game.
# -----------------------------------------------------------


# Function: intro
# Purpose: Introduce the game and ask for player name
def intro():
    print("Welcome to the Adventure Game!")
    name = input("Enter your name, brave explorer: ")
    print(f"\nHello {name}! You woke up in a mysterious forest.")
    print("Your mission: Find the treasure box with a key in the forest.")
    print("Then travel to the island and use it to find the diamond!\n")
    return name


# Function: choose_direction
# Purpose: Ask player to choose a direction (N/S/E/W).
# Note: We use .upper() to handle both small and capital inputs.
def choose_direction():
    # Mapping directions to full names
    directions = {
        "N": "North",
        "S": "South",
        "E": "East",
        "W": "West"
    }

    while True:
        # Convert input to uppercase so that 'n' and 'N' are treated the same
        direction = input("Choose a direction (N/S/E/W): ").upper()
        if direction in directions:
            return directions[direction]   # Returns "North", "South", etc aka value of the dictinary directions.
        else:
            print("Invalid choice! Please enter N, S, E, or W.")


# Function: choose_box
# Purpose: Ask player to open a box (1, 2, or 3).
def choose_box(direction):
    while True:
        try:
            box = int(input("Which box do you open? (1, 2, or 3): "))
            if box in [1, 2, 3]:
                return box
            else:
                print("Only boxes 1, 2, or 3 exist. Try again.")
        except ValueError:
            # Handles invalid input (e.g., if user types letters)
            print("Please enter a number (1, 2, or 3).")


# Function: level1
# Purpose: Forest Stage, Player must find the key.
# Winning condition: East side Box 3
def level1():
    print("\n--- Level 1: The Forest ---")

    while True:
        direction = choose_direction()
        box = choose_box(direction)

        # Winning condition for Level 1
        if direction == "East" and box == 3:
            print("East side Box 3 has the key! Level 1 completed.\n")
            return True
        else:
            print(f"{direction} side Box {box} is empty. Keep searching!\n")


# Function: level2
# Purpose: Island Stage, Player must find the diamond.
# Winning condition: West side Box 3
def level2():
    print("\n--- Level 2: The Island ---")

    while True:
        direction = choose_direction()
        box = choose_box(direction)

        # Winning condition for Level 2
        if direction == "West" and box == 3:
            print("West side Box 3 has the diamond! You win the game!")
            return True
        else:
            print(f"{direction} side Box {box} is empty. Try again!\n")


# Function: game
# Purpose: Run the complete game flow
def game():
    name = intro()
    if level1():   # Proceed to level 2 only if key is found
        level2()
    print(f"\nThanks for playing, {name}!")


# Run the game only if this file is executed directly
if __name__ == "__main__":
    game()