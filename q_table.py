########################################################################################
# This is a q-table object
# Written by Sam Drell
########################################################################################

import numpy as np
import random
import pandas as pd

class qt:
    def __init__(self,state_num,action_num):
        self.q_table = np.zeros((state_num,action_num))
    
    def print_qt(self):
        # print(f"Num of rows: {self.q_table.shape[0]}")
        print(self.q_table)
    
    def max_reward(self, state):
        max_index = 0
        max_value = self.q_table[state][0]
        matching_indices = [max_index]

        for i in range(1, len(self.q_table[state])):
            if self.q_table[state][i] > max_value:
                max_value = self.q_table[state][i]
                max_index = i
            elif self.q_table[state][i] == max_value:
                matching_indices.append(i)

        if len(matching_indices) > 1:
            # print("too many equal values. Picking random") # FIXME Debug print
            return random.choice(matching_indices)
        else:
            # print("choosing best action") # FIXME Debug print
            return max_index
        
    def maximum_overall_reward(self):
        return np.max(self.q_table)
    
########################################################################################
# Written by ChatGPT
########################################################################################
    def export_to_excel(self, filename="q_table.xlsx"):
        df = pd.DataFrame(self.q_table)
        df.to_excel(filename, index=True, header=True)
        print(f"Q-table exported to '{filename}' successfully.")

    
########################################################################################
# Parameters:
#    new_state = state num of new state (after taking action), int
#    prev_state = state num of prev state (before taking action), int
#    action_reward = reward from new location, int
#    action_taken = int, corresponds to maze.ACTIONS [0,3]
########################################################################################
    def update_q_table(self,new_state, prev_state, action_reward, action_taken):
        
        s = prev_state                                  # previous state
        # s = int(self.q_table[prev_state][action_taken]) # previous state
        A = action_taken                                # action taken
        ss = new_state                                  # new state

        AA = int(np.argmax(self.q_table[ss]))           # best next action in state ss
        r = action_reward                               # reward for taking action A in state S
        y = 0.5                                         # discount factor
        a = 0.5                                         # learning rate

        # Debugging Prints
        # print(ss)
        # print(s)
        # print(A)
        # print(AA)

        # Bellman Equation? I haven't found this exact version except from chatgpt
        self.q_table[s,A] += 0 + a*(r + y * self.q_table[ss,AA] - self.q_table[s,A])