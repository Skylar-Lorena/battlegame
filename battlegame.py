wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 90
human_hp = 88
dragon_hp = 300

wizard_damage = 150
elf_damage = 90
human_damage = 99
dragon_damage = 50

while True:

    print(wizard)
    print(elf)
    print(human)

    answer = input("Choose your character (1-Wizard, 2-Elf, 3-Human): ")
    if answer == "1":
        character = wizard

        while wizard_hp > 0 and dragon_hp > 0: