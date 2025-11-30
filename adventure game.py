# Simple Text-Based Adventure Game: A choose-your-own-adventure game with multiple endings. (Uses loops, conditionals, functions – Week 3 focus)
def start_game():
    print("=== FOREST ADVENTURE ===")
    print("You're lost in a forest. Find your way out!")
    forest()

def forest():
    print("\nYou're in a dark forest.")
    print("Paths: left or right")
    
    choice = input("Which way? (left/right): ").lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Please choose 'left' or 'right'")
        forest()

def left_path():
    print("\nYou find a cabin.")
    print("Options: enter or continue")
    
    choice = input("What do you do? (enter/continue): ").lower()
    
    if choice == "enter":
        print("\nYou find food and shelter!")
        print("You survive and find your way home tomorrow.")
        game_over("GOOD ENDING: You made it home safely!")
    elif choice == "continue":
        print("\nYou continue deeper into the forest.")
        print("You get lost forever.")
        game_over("BAD ENDING: You're still lost in the forest.")
    else:
        print("Please choose 'enter' or 'continue'")
        left_path()

def right_path():
    print("\nYou come to a river.")
    print("Options: swim or bridge")
    
    choice = input("What do you do? (swim/bridge): ").lower()
    
    if choice == "swim":
        print("\nThe current is too strong!")
        print("You get swept away.")
        game_over("BAD ENDING: You drowned in the river.")
    elif choice == "bridge":
        print("\nYou find a hidden bridge.")
        print("You cross safely and find the way home!")
        game_over("GOOD ENDING: You made it home!")
    else:    
        print("Please choose 'swim' or 'bridge'")
        right_path()

def game_over(message):
    print(f"\n{message}")
    
    while True:
        again = input("\nPlay again? (yes/no): ").lower()
        if again == "yes":
            start_game()
            break
        elif again == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please answer 'yes' or 'no'")

# Start the game
start_game()