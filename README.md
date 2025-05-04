# Text_RPG_Combat_AI
This program uses a Reinforcement-learning model and a Q-table to intelligently battle against the player.

DESCRIPTION
This program is an rpg game that allows the player to battle against a computer comtrolled enemy. The enemy is controlled by a Reinforcement-learning model that utilizes an epsilon-greedy algorithm to explore available actions and then fills in Q-table using a simplified version of the Bellman equation, allowing the model to learn the best actions to take under specific conditions.

Currently, the game is in the "demo-mode," which only allows the AI to be trained.

RUNNING THE GAME
To run the game, run the file "main_menu.py," press b and then enter. This will train the AI on 1000 combat instances, where the player character is controlled by an automoted controller that randomly selects actions until the character runs out of actions. At the end of the training, a graph will display that plots the number of actions it took to defeat the player character in each episode, as well as the maximum reward value earned in each episode. 

DESIGN 
The most significant files are the "combat.py," "q_table.py," and "ql_agent.py" files, but these will be discussed later, as it is most clear to describe the overall architecture, and describe the relevant methods and files.

This program exploited the ability to pass methods as parameters, and the entire functionality of this program relies on this ability. Below is a flowchart that demonstrates the order of method calls (excluding constructors), and it includes the location of the method definitions.

    display_menu (in main_menu.py)

    -> begin_combat_with_ai (in combat.py)
  
      -> train (in ql_agent.py)
      
          -> initialize_ai_combat (in combat.py)
          
            -> random_controlled (in combat.py)
            
          -> ai_full_combat_sequence (in combat.py)
          
              -> take_action (in ql_agent.py)
              
                  -> choose_action (in ql_agent.py)
                  
                      -> max_reward (in q_table.py)
                      
                  -> ai_action (in combat.py)
                  
                      -> action_choice (in action_list.py)
                      
                  -> update_q_table (in q_table.py)
                  
              -> random_controlled (in combat.py)

FUTURE CHANGES
Two main changes need to be made, in regards to the AI. 
1) The learning parameters need to be tuned. Currently, the program does an excellent job of maximizing reward, but it does not adequately decrease the amount of necessary actions taken.
2) Methods need to be build that can save and import a Q-table produced from a training sequence, that way the AI can be implemented to play against a user controlled player, instead of just a randomly controleld player.

AUTHORSHIP
This game was almost entirely written by myself. All relevant q-learning methods and files were entirely proprietary, and if ChatGPT was used to write a method or file, it was noted. ChatGPT was, however, used in debugging as well to fix syntax or logical errors.
