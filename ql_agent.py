import random as rand
import numpy as np
import matplotlib.pyplot as plt

# import q_table as qt

# Goal: I don't want to use this at all.
# import maze as mz

class agent:
    def __init__(self):
        self.epsilon = 0.1

########################################################################################
# Parameters
#   actions_list - List, the various actions that may be choosen in each state.
#   curr_state - The current state (row) of the state table that the agent is on.
#   q_table - qt object This is the q-table object that the agent interacts with
########################################################################################
    def choose_action(self, actions_list, curr_state, q_table):
    # Choose action based on e-greedy policy
        # Exploration
        if rand.random() < self.epsilon:
            chosen_action = rand.choice(actions_list)
            # print("Choosing random action") # FIXME Debug print
        # Exploitation
        else:
            # Choose action with highest reward in current state.
            index = q_table.max_reward(curr_state)
            chosen_action = actions_list[index]

        index = actions_list.index(chosen_action)
        return chosen_action, index
    
########################################################################################
# Parameters
#   actions_list - List, the various actions that may be choosen in each state.
#   my_action - Method, this allows the desired action to be passed in, improving 
#       modularity
#   curr_state FIXME I'm not sure if this is a tuple, int, or what
#   q_table - qt object This is the q-table object that the agent interacts with

# Perhaps done?

########################################################################################

    def take_action(self,actions_list,my_action,curr_state,q_table,num_actions):
        # Choose action
        action_choice, num_of_choice = self.choose_action(actions_list, curr_state, 
                                                          q_table)

        # Submit action choice to game and take action
        new_state, reward, gameplay = my_action(curr_state,action_choice,num_actions)

        # Update q-table based on action outcomes
        q_table.update_q_table(new_state, curr_state, reward, num_of_choice)

        # Update current state
        curr_state = new_state

        return new_state, gameplay
    

########################################################################################
# Plots a line chart from a list of integers.
    
# Parameters:
#   data: list of integers
#   title: (optional) chart title
#   x_label: (optional) label for x-axis
#   y_label: (optional) label for y-axis

# Written by ChatGPT
########################################################################################
    def plot_data(paired_data, title="Line Chart", x_label="Index", y_label="Value"):
        # Validate input
        if (not isinstance(paired_data, list) or
            not all(isinstance(pair, list) and len(pair) == 2 for pair in paired_data) or
            not all(isinstance(x, (int, float)) for pair in paired_data for x in pair)):  # Allow int or float
            raise ValueError("Input must be a list of [int, float] pairs.")

        # Transpose: split into two lists — one for each line
        agent_actions, enemy_actions = zip(*paired_data)

        plt.figure(figsize=(10, 6))
        plt.plot(agent_actions, marker='o', linestyle='-', label="Agent Actions", color='blue')
        plt.plot(enemy_actions, marker='s', linestyle='--', label="Reward", color='red')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

########################################################################################
# Parameters
#   episodes - int, num of training session
#   episode_gameplay - Method, one game "session"
#   my_action - Method, this allows the desired action to be passed in, improving 
#       modularity
#   -   In the context of the maze, this could be the play game loop.
#   actions_list - List, the various actions that may be choosen in each state.
#   enemy_turn - Method, this is how to enemy takes it's turn
#   q_table - qt object This is the q-table object that the agent interacts with
#   g_start - This is a method of the game object that indicates the start of an episode

# Perhaps Done?

########################################################################################
    def train(self,episodes,episode_gameplay,my_action,actions_list,enemy_turn,
              q_table,g_start):
        
        episode_log = [[0, 0] for _ in range(episodes)]

        for i in range(episodes):
            print(f"Episode {i}")

            # Get start state
            gameplay, curr_state = g_start() # Begin Game

            if gameplay:
                # this calls into an episode method of the combat method
                episode_log[i][0] = episode_gameplay(self.take_action,enemy_turn,
                                                           actions_list,my_action,curr_state,
                                                           q_table,episode_log,i)
            episode_log[i][1] =q_table.maximum_overall_reward()

        # for row in episode_log:
        #     print(row)

        agent.plot_data(episode_log,"Episode Action Count","Episode","Num of Actions")
        q_table.export_to_excel()