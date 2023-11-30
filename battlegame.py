# Task 1: Declare variables for characters and their hp and damage
wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50


#  Task 2: Prompt the player to choose from a list of options
print("Welcome to the Battle Game!")
print("Choose your character: ")
print("1.", wizard)
print("2.", elf)
print("3.", human)

character = input("Enter your choice: ")

# Task 3: Set up infinite while loop to handle player choice
while True:
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break


    
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break


    
    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break


    
else:
        print("Unknown character")
        character = input("Enter your choice: ")
