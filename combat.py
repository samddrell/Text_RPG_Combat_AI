import random
import os
import sys
import time
import itertools

import combat.action_list as al

# sys.path.append("/home/samddrell/sam-1/Engineering Projects/")

from game_reinforcement_ai import q_table as qt
from game_reinforcement_ai import ql_agent as ai


# TODO: Ensure all controllers have the same sequence of parameters

class combat_instance():

###############################################################################
# Print statements with delays between characters
# Helper Function
# Written by ChatGPT
###############################################################################
    def type_print(text, delay=0.1):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # move to the next line after printing the text


###############################################################################
# Player Action
###############################################################################
    def user_controlled(self,player,enemy):
        # Player Turn System
        # Set player turn to on
        turn_in_progress = True
        player.curr_mana = player.tot_mana
        encounter = True

        combat_instance.type_print(f"PLAYER HEALTH: {player.health}", delay=0.001)
        combat_instance.type_print(f"PLAYER MANA: {player.curr_mana}", delay=0.001)
        
        # Check that the player has enough mana or hasn't ended their turn
        while(player.curr_mana > 0 and turn_in_progress):
            turn_in_progress = False if player.curr_mana == 0 else True
            
            # Print player action list
            combat_instance.type_print("\nWHAT DO YOU DO?", delay=0.001)

            # Take player action input
            combat_instance.type_print("(C) FLEE CAUSE IMA COWARD\n" 
                                 "(D) CAST A SPELL\n"
                                 "(E) END TURN\n", delay=0.001)
            player_input = input()

            if (player_input.lower() == "c"):
                # Debugging/Testing Print
                encounter = False
                turn_in_progress = False
                # print(encounter)

            elif (player_input.lower() == "d"):
                combat_instance.type_print("Enter spell: ", delay=0.001)
                action_input = input()
                action_list = list(al.action_dict.keys())
                if action_input in action_list:
                    al.action_dict[action_input.lower()](player,enemy)

                    # Debugging/Testing Print
                    combat_instance.type_print(f"MANA: {player.curr_mana}", delay=0.001)
                    # Debugging/Testing Print
                    combat_instance.type_print(f"{enemy.name} health: {enemy.health}", delay=0.001)

                else:
                    combat_instance.type_print("THERE IS NO SUCH SPELL", delay=0.001)

            elif (player_input.lower() == "e"):
                combat_instance.type_print("TURN ENDED.", delay=0.001)
                turn_in_progress = False

            else:
                combat_instance.type_print("INVALID INPUT", delay=0.001)

        return encounter


###############################################################################
# Randomized Character Controller
#   This method allows either the player or the mob to be controlled by a 
#   random sequence. 
###############################################################################
    @staticmethod
    def random_controlled(attacker,defender):

        turn_in_progress = True
        attacker.curr_mana = attacker.tot_mana
        action_count = 0

        while(attacker.curr_mana > 0 and turn_in_progress and action_count < 50):
            attacker.actions[random.randrange(len(attacker.actions))](attacker,defender)
            action_count +=1

        return True
    

###############################################################################
# Set Control Agents and characters for the combat
###############################################################################
    def __init__(self,player_character,mob,player_agent,enemy_agent=random_controlled):
        self.player = player_character
        self.enemy = mob
        self.player_controller = player_agent
        self.enemy_controller = enemy_agent
        self.state_vector = []


###############################################################################
# Method for non-ai gameplay
###############################################################################
    def begin_combat_not_ai(self):

        # Clear terminal screen
        os.system('clear')

        # Begin Encounter
        combat_instance.type_print(f"YOU ENCOUNTER A {self.enemy.name}!\n", delay=0.001)
        # player_character.display_stats()

        # For simplicity's sake, begin with player action

        # Begin encounter
        encounter = True

        # Enter Combat Sequence
        while (encounter and self.player.health and self.enemy.health):
            print("PLAYER TURN!\n")
            encounter = self.player_controller(self.player,self.enemy)
            if not encounter:
                print("YOU FLED, COWARD.")
                break

            if self.enemy.health == 0:
                print(f"{self.enemy.name} has been defeated!")
                encounter = False
                break

            print('ENEMY TURN!\n')
            encounter = self.enemy_controller(self.enemy,self.player) 
            if self.player.health <= 0:
                print(f"{self.player.name} has been defeated!")
                encounter = False

            print(encounter,self.player.health,self.enemy.health,"(Debugging statement)")


###############################################################################
# Initialize AI control.
# NOTE: This is a helper function that provides the q_learning train method
#   with some of the information that it is expecting
###############################################################################
    def initialize_ai_combat(self):

        attacker = self.enemy
        defender = self.player

        # Resets the characters from the previous fights
        attacker.health = attacker.max_health
        defender.health = defender.max_health
        
        # Take player turn
        # print("PLAYER TURN!\n")
        encounter = combat_instance.random_controlled(defender,attacker)
        if not encounter:
            print("YOU FLED, COWARD.")

        if self.enemy.health == 0:
            print(f"{self.enemy.name} has been defeated!")
            encounter = False

        if (attacker.health <= 0):
            encounter=False
            if (defender.health >= 0):
                print("ai has been defeated before the battle even began!")
                initial_state = self.state_vector.index((0,
                                                    attacker.curr_mana,
                                                    defender.health))
            else:
                print("both were defeated before the battle even began!")
                initial_state = self.state_vector.index((0,
                                                    attacker.curr_mana,
                                                    0))
        elif (defender.health <= 0):
            print("the player has been defeated before the battle even began!")
            encounter=False
            if (attacker.health >= 0):
                print("the player has been defeated before the battle even began!")
                initial_state = self.state_vector.index((attacker.health,
                                                    attacker.curr_mana,
                                                    0))
            else:
                print("both were defeated before the battle even began!")
                initial_state = self.state_vector.index((0,
                                                    attacker.curr_mana,
                                                    0))
        else:
            initial_state = self.state_vector.index((attacker.health,
                                                attacker.curr_mana,
                                                defender.health))

        return encounter, initial_state


###############################################################################
# Game episode
#   This is a wrapper function, of sorts, to integrate the agent action and 
#   choice mechanic with the game turn mechanic.

# NOTE: 
# This architecture style is unideal because the agent file and the combat
#   file jump back and forth, calling different methods in each other,
#   which is confusing and hard to track.
###############################################################################
    def ai_full_combat_sequence(self,agent_action,enemy_action,actions_list,
                                my_action,curr_state,q_table,
                                episode_action_count,episode_num):
        attacker = self.enemy
        defender = self.player

        encounter = True

        while encounter:

            attacker.curr_mana = attacker.tot_mana
            while(self.enemy.curr_mana > 0 )and encounter:
                curr_state, encounter = agent_action(actions_list,my_action,
                                                    curr_state,q_table,
                                                    episode_action_count[episode_num][0])
                episode_action_count[episode_num][0] += 1
                
            if encounter:
                # print("\PLAYER TURN\n") # FIXME DEBUGGING PRINT
                enemy_action(self.player,self.enemy)

        return episode_action_count[episode_num][0]

###############################################################################
# AI Action Mechanic
###############################################################################
    def ai_action(self,curr_state,action_choice,num_actions):

        # Redefine Variables for redability
        attacker = self.enemy
        defender = self.player

        reward = 0

        if (attacker.health <= 0):
            print("ai has been defeated!")
            encounter=False
            new_state = self.state_vector.index((0,
                                                attacker.curr_mana,
                                                defender.health))
            reward = -1000
            return new_state, reward, encounter
        
        # print("\nAI TURN\n") # FIXME DEBUGGING PRINT
        encounter = True

        # Take Action
        action_choice(attacker,defender)  

        # Determine Reward
        if (defender.health < self.state_vector[curr_state][2]):
            reward = 30
        elif (attacker.health > self.state_vector[curr_state][0]):
            reward = 50
        elif (defender.health == self.state_vector[curr_state][2] 
                and attacker.health == self.state_vector[curr_state][0]):
            reward = -30
        elif (defender.health <= 0):
            reward = 1000

        # Decrease reward as number of actions increases
        reward -= (num_actions * 1.5)

        # print(f"\nAI HAS {attacker.health} HEALTH REMAINING\n")
        # print(f"PLAYER HAS {defender.health} HEALTH REMAINING\n")

        # Determine new State and Encounter Value
        if (defender.health <= 0):
            print("PLAYER HAS BEEN DEFEATED")
            encounter=False
            new_state = self.state_vector.index((attacker.health,
                                                attacker.curr_mana,
                                                0))
        else:
            new_state = self.state_vector.index((attacker.health,
                                                attacker.curr_mana,
                                                defender.health))
            
        return new_state, reward, encounter


###############################################################################
# AI control interface
# Wrapper function that allows the implementation to be consistent with the 
#   other functions
###############################################################################
    
    # WRAPPER

    def begin_combat_with_ai(self):
        attacker = self.enemy
        defender = self.player

        # BEGIN HERE


        # STEP 1 - Initialize q-table
        # Make State Vector
        self.state_vector = list(itertools.product(range(attacker.max_health + 1),
                                                range(attacker.tot_mana + 1),
                                                range(defender.max_health + 1)))

        # Initialize q table with the appropriate dimensions
        state_num = len(self.state_vector)
        action_num = len(attacker.actions)
        table = qt.qt(state_num,action_num)

        # table.print_qt()

        # STEP 2 - Initialize agent
        bot = ai.agent()

        # STEP 3 - Begin Training
        episodes = 1000
        q_table = table
        actions_list = attacker.actions
        g_start = self.initialize_ai_combat
        enemy_turn = self.random_controlled
        my_action = self.ai_action

        # FIXME: This is defined later.
        episode_gameplay = self.ai_full_combat_sequence

        # This calls into the train method of the ai agent
        bot.train(episodes,episode_gameplay,my_action,actions_list,enemy_turn,
                 q_table,g_start)
        

'''
###############################################################################
# Combat Sequence
# NOTE: legacy
###############################################################################
    def combat(player_character,mob):
        # Clear terminal screen
        os.system('clear')

        # Begin Encounter
        print(f"YOU ENCOUNTER A {mob.name}!")
        player_character.display_stats()

        # Decide if the player of mob attacks first
        mob_attacks = random.randrange(0,2)
        if (mob_attacks == 0):
            pass
        else:
            combat_instance.mob_action(player_character,mob)

        encounter = True
        
        while (encounter and player_character.health and mob.health):
            print("PLAYER TURN!")
            encounter = combat_instance.player_action(player_character,mob,encounter)
            if not encounter:
                print("YOU FLED, COWARD.")
                break

            if mob.health == 0:
                print(f"{mob.name} has been defeated!")
                encounter = False
                break

            print(f'ENEMY TURN!\n')
            combat_instance.mob_action(mob,player_character) 
            if player_character.health == 0:
                print(f"{player_character.name} has been defeated!")
                encounter = False

'''