# import defender
# import player

def Fulmen_ictus(attacker,defender):
    # LIGHTNING STRIKE
    mana = 3
    damage = 2
    if(attacker.curr_mana >= mana):
        if (defender.status_type == "UGND"):
            print(f"{defender.name} is immune")
        else:
            # print("CASTING FULMEN ICTUS")
            defender.take_damage(damage)
            attacker.deplete_mana(mana)
    else:
        pass
        # print("NOT ENOUGH MANA TO CAST FULMEN ICTUS.")

def Terrae_motus(attacker,defender):
    # TREMOR
    mana = 2
    damage = 1
    if(attacker.curr_mana >= mana):
        if (defender.status_type == "AIR"):
            print(f"{defender.name} is immune")
        else:
            # print("CASTING TERRAE MOTUS")
            defender.take_damage(damage)
            attacker.deplete_mana(mana)
    else:
        pass
        # print("NOT ENOUGH MANA TO CAST TERRAE MOTUS.")

# NOTE: This is currently disabled for all creatures.
def Intellectus_Hostis(attacker,defender):
    # This is only to display defender stats
    mana = 4
    if(attacker.curr_mana >= mana):
        # print("CASTING INTELLECTUS HOSTIS")
        defender.display_stats()
        attacker.deplete_mana(mana)
    else:
        pass
        # print("NOT ENOUGH MANA TO CAST INTELLECTUS HOSTIS.")

def Sana_Sui_Corporius(attacker,defender):
    # Heal
    mana = 3
    
    if(attacker.curr_mana >= mana):
        if attacker.health <= attacker.max_health - 5:
            # print("CASTING SANA SUI CORPORIUS")
            attacker.heal(5)
            attacker.deplete_mana(mana)
        elif attacker.health < attacker.max_health:
            # print("CASTING SANA SUI CORPORIUS")
            attacker.health = attacker.max_health
            attacker.deplete_mana(mana)
        else:
            pass
            # print(f"{attacker.name} AT MAX HEALTH")
        # print(f"{attacker.name} HEALTH: {attacker.health}")
    else:
        pass
        # print("NOT ENOUGH MANA TO CAST SANA SUI CORPORIUS.")

def copper_dagger(attacker,defender):
    mana = 3
    damage = 2

    if(attacker.curr_mana >= mana):
        # print("ATTACKING WITH COPPER DAGGER")
        defender.take_damage(damage)
        attacker.deplete_mana(mana)
        # print(f"Attacker mana: {attacker.curr_mana}")
    else:
        pass
        # print("NOT ENOUGH MANA TO USE COPPER DAGGER.")

def claws(attacker,defender):
    mana = 1
    damage = 1

    if(attacker.curr_mana >= mana):
        # print("ATTACKING WITH CLAWS")
        defender.take_damage(damage)
        attacker.deplete_mana(mana)
    else:
        pass
        # print("NOT ENOUGH MANA TO USE CLAWS.")

def Gigas_muscipula(player,defender):
    print("Not yet implemented")
def Circulus_radius(player,defender):
    print("Not yet implemented")
def Aura_scutum(player,defender):
    print("Not yet implemented")
def Phantasma_miles(player,defender):
    print("Not yet implemented")
def Rejuvenescere(player,defender):
    print("Not yet implemented")
def Ver_muscipula(player,defender):
    print("Not yet implemented")
def Spectare_statistica(player,defender):
    print("Not yet implemented")
def transmittere(player,defender):
    print("Not yet implemented")
def Congelare(player,defender):
    print("Not yet implemented")

action_dict = { "fulmen ictus": Fulmen_ictus,
            "terrae motus" : Terrae_motus,
            "intellectus hostis" : Intellectus_Hostis,
            "sana sui corporius" : Sana_Sui_Corporius,
            "copper dagger" : copper_dagger,
            "claws" : claws
}