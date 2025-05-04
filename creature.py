import combat.action_list as action
import os

class mob:
    def __init__(self,creature_name):
        self.name = creature_name
        self.health = creature_list[creature_name][0]
        self.max_health = creature_list[creature_name][0]
        self.armor = creature_list[creature_name][1]
        self.tot_mana = creature_list[creature_name][2]
        self.curr_mana = creature_list[creature_name][2]
        self.actions = creature_list[creature_name][3]
        self.status_type = creature_list[creature_name][4]

    def display_stats(self):
        with open("enemy_stats.txt", "w") as file:
            file.write(f"{self.name}:\n")
            file.write(f"HEALTH: {self.health}/{self.max_health}\n")
            file.write(f"ARMOR: {self.armor}\n")
            file.write(f"MANA: {self.curr_mana}/{self.tot_mana}\n")
            file.write("CURRENT ACTIONS: \n")
            for i in self.actions: file.write(f"{i}\n") 
        os.system('start notepad enemy_stats.txt')    

    def take_damage(self, damage_amount):
        self.health -= damage_amount

    def deplete_mana(self, used_mana):
        self.curr_mana -= used_mana

    def heal(self, heal_amount):
        self.health += heal_amount

    # TODO: Currently, this is implemented in the combat function, but I may want to move that here.
    def attack():
        # Debugging/Testing Print
        print("Attack Not Yet Implemented")
    def change_status():
        # Debugging/Testing Print
        print("Heal Not Yet Implemented")
    

creature_list = {"MEEK GHOUL" : [10, 0, 5, 
                                 [action.action_dict["copper dagger"], 
                                  action.action_dict["claws"], 
                                  action.action_dict["sana sui corporius"]], 
                                 "GND"],
                 "PLAYER" : [10, 0, 5, 
                             [action.action_dict["fulmen ictus"], 
                              action.action_dict["terrae motus"], 
                              action.action_dict["sana sui corporius"], ], 
                             "GND"],
}