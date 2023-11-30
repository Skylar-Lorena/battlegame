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


while True:
    print(wizard)
    print(elf)
    print(human)

    answer = input("Choose your character (1-Wizard, 2-Elf, 3-Human): ")
    if answer == "1":  # Check if the user chose wizard
        character = wizard  # Set the character variable to wizard
        # Start a loop for the wizard's battle with the dragon
        while (
            wizard_hp > 0 and dragon_hp > 0
        ):  # Continue the loop while both wizard and dragon are alive
            # Wizard attacks first
            dragon_hp -= wizard_damage  # Subtract wizard's damage from dragon's health
            print(
                f"{character} attacked dragon for {wizard_damage} damage."
            )  # Display message indicating wizard's attack

            if dragon_hp <= 0:  # Check if dragon is defeated after wizard's attack
                print(
                    "You have defeated the dragon!"
                )  # Congratulate the player for defeating the dragon
                break  # Break out of the loop to end the battle

            # Dragon attacks back
            wizard_hp -= dragon_damage  # Subtract dragon's damage from wizard's health
            print(
                f"Dragon attacked {character} for {dragon_damage} damage."
            )  # Display message indicating dragon's attack

            if wizard_hp <= 0:  # Check if wizard is defeated after dragon's attack
                print(
                    "The dragon has defeated you!"
                )  # Inform the player that the dragon won the battle
                break  # Break out of the loop to end the battle

    elif answer == "2":  # Check if the user chose elf
        character = elf  # Set the character variable to elf
        # Start a loop for the elf's battle with the dragon
        while (
            elf_hp > 0 and dragon_hp > 0
        ):  # Continue the loop while both elf and dragon are alive
            # Elf attacks first
            dragon_hp -= elf_damage  # Subtract elf's damage from dragon's health
            print(
                f"{character} attacked dragon for {elf_damage} damage."
            )  # Display message indicating elf's attack

            if dragon_hp <= 0:  # Check if dragon is defeated after elf's attack
                print(
                    "You have defeated the dragon!"
                )  # Congratulate the player for defeating the dragon
                break  # Break out of the loop to end the battle

            # Dragon attacks back
            elf_hp -= dragon_damage  # Subtract dragon's damage from elf's health
            print(
                f"Dragon attacked {character} for {dragon_damage} damage."
            )  # Display message indicating dragon's attack

            if elf_hp <= 0:  # Check if elf is defeated after dragon's attack
                print(
                    "The dragon has defeated you!"
                )  # Inform the player that the dragon won the battle
                break  # Break out of the loop to end the battle

    # Check if the user chose human
    elif answer == "3":
        character = human

        my_hp = human_hp
        my_damage = human_damage

        break
