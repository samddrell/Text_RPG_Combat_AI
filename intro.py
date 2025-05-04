import time
import sys 

sys.path.append("/home/samddrell/sam-1/Engineering Projects/In Line Game/")

import combat.combat as combat

def display_intro():
    intro_text_file = open(r"intro_script.txt","r")
    intro_text = intro_text_file.readlines()
    usr_input = ""

    for i in intro_text:
        if (i == "END OPTION 1\n"):
            usr_input = input()
            continue
        elif (i == "END OPTION 2\n"):
            usr_input = input()
            continue
        elif (i == "END OPTION 3\n"):
            usr_input = input()
            continue
        else:
            for char in i:
                print(char, end="", flush=True)
                time.sleep(.01)

    sam = player.player_character()
    mob1 = creature.mob("MEEK GHOUL")

    combat.combat(sam,mob1)