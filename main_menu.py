import time
import os
import intro
import sys

from combat import combat

# sys.path.append("/home/samddrell/sam-1/Engineering Projects/")

# from reinforcement_ai import q_table as qt
# from reinforcement_ai import q_learning as ai


sys.path.append("/home/samddrell/sam-1/Engineering Projects/In Line Game/")

from combat import combat
from characters import creature

script_dir = os.path.dirname(__file__)  # gets current script directory
file_path = os.path.join(script_dir, "main_menu.txt")

def display_menu():
    os.system('clear')
    menu_file = open(file_path,"r")
    menu_text = menu_file.readlines()
    usr_input = ""

    for i in menu_text:
        if i.strip() == ("END OPTIONS"):
            usr_input = input()

            # STORY MODE
            if usr_input.lower() == "a":
                os.system('clear')

                # Story mode is disabled. Uncomment the follow command to enable.

                # intro.display_intro()
                break

            # TRAIN AI
            elif usr_input.lower() == "b":
                os.system('clear')
                
                sam = creature.mob("PLAYER")
                mob1 = creature.mob("MEEK GHOUL")

                combat_episode = combat.combat_instance(sam,
                                       mob1,
                                       combat.combat_instance.random_controlled)
                
                combat_episode.begin_combat_with_ai()

            # PLAY AGAINST RANDOM ENEMY
            elif usr_input.lower() == "d":
                os.system('clear')

                sam = creature.mob("PLAYER")
                mob1 = creature.mob("MEEK GHOUL")
                player_controller = combat.combat_instance.user_controlled
                
                # Note: enemy controller is defaulted to random
                combat.combat_instance(sam,
                                       mob1,
                                       player_controller)

        else:
            for char in i:
                print(char, end="", flush=True)
                time.sleep(0.001)

# DISPLAY THE MENU
display_menu()