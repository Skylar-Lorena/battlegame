import sys

# Task 1: Declare variables for characters and their stats
#   - Name, HP, and damage
wizard = "Wizard"  # Stores the character name
wizard_hp = 70    # Initial HP of the wizard
wizard_damage = 150  # Damage dealt by the wizard

# Similar declarations for elf and human

dragon_hp = 300  # Dragon's HP
dragon_damage = 50  # Damage dealt by the dragon

# Task 2: Welcome message and character selection
print("Welcome to the Battle Game!")
print("Choose your warrior:")
print("1.", wizard)  # Display character options with numbers
print("2.", elf)
print("3.", human)
print("4. Exit")

character_input = input("Enter your choice: ")  # Get player's choice

# Task 3: Handle player input and set character stats
while True:
    # Check for exact match or numeric input for each character
    if character_input.lower() == wizard.lower() or character_input == "1":
        character = wizard
        my_hp = wizard_hp  # Set player's HP and damage based on chosen character
        my_damage = wizard_damage
        break

    # Similar conditions for elf and human

    # Check for exit option
    elif character_input.lower() == "exit" or character_input == "4":
        print("Goodbye!")
        sys.exit(0)

    # Handle invalid input and prompt again
    else:
        print("Unknown character")
        character_input = input("Enter your choice: ")

# Task 4: Battle loop
while True:
    # Player attacks dragon
    dragon_hp -= my_damage
    print(f"The {character} damaged the Dragon!")  # Use f-string for dynamic text
    print(f"Dragon's HP: {dragon_hp}")

    # Check if dragon is defeated
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break

    # Dragon attacks player
    my_hp -= dragon_damage
    print(f"{character} was damaged by the Dragon!")
    print(f"Your HP: {my_hp}")

    # Check if player is defeated
    if my_hp <= 0:
        print("You have lost the battle!")
        break

    # Ask if player wants to play again after each round
    while True:
        play_again = input("Do you want to play again? (Y/N): ")

        if play_again.lower() == "y":
            break  # Restart the game if player chooses yes
        elif play_again.lower() == "n":
            sys.exit(0)  # Exit if player chooses no
        else:
            print("Invalid input. Please enter Y or N.")

