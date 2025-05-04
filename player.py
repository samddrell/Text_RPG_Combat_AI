import os

# NOTE: This is legacy

class player_character:
    def __init__(self):
        self.name = "player_name"
        self.health = 10
        self.max_health = 10
        self.armor = 10
        self.tot_mana = 5
        self.curr_mana = 5
        self.items = []
        self.actions = []
        self.status_type = "GND"
        self.action_list = ["ITEM 1", "ITEM 2", "ESCAPE", "CAST", "END TURN"]
        
            
    def deplete_mana(self, used_mana):
        self.curr_mana -= used_mana

    def take_damage(self, damage_amount):
        self.health -= damage_amount
        # Debugging/Testing Print
        print(f"{damage_amount} damage taken!")

    def display_stats(self):
        # os.system('start notepad player_stats.txt')
        with open("player_stats.txt", "w") as file:
            file.write("PLAYER STATS:\n")
            file.write(f"HEALTH: {self.health}/{self.max_health}\n")
            file.write(f"ARMOR: {self.armor}\n")
            file.write(f"MANA: {self.curr_mana}/{self.tot_mana}\n")
            for i in self.items: file.write(f"CURRENT ITEMS: {i}") 
        os.system('start notepad player_stats.txt')

    def heal(self, heal_amount):
        self.health += heal_amount

        