# Text_RPG_Combat_AI
This program uses a Reinforcement-learning model and a Q-table to intelligently battle against the player.

DESCRIPTION
This program is an rpg game that allows the player to battle against a computer comtrolled enemy. The enemy is controlled by a Reinforcement-learning model that utilizes an epsilon-greedy algorithm to explore available actions and then fills in Q-table using a simplified version of the Bellman equation, allowing the model to learn the best actions to take under specific conditions.

Currently, the game is in the "demo-mode," which only allows the AI to be trained.

RUNNING THE GAME
To run the game, run the file "main_menu.py," press b and then enter. This will train the AI on 1000 combat instances, where the player character is controlled by an automoted controller that randomly selects actions until the character runs out of actions. At the end of the training, a graph will display that plots the number of actions it took to defeat the player character in each episode, as well as the maximum reward value earned in each episode. 

DESIGN 
The most significant files are the "combat.py," "q_table.py," and "ql_agent.py" files, but these will be discussed later, as it is most clear to describe the overall architecture, and describe the relevant methods and files.

FUTURE CHANGES
