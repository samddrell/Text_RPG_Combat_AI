# from characters import creature
# from characters import player

# NOTE: This is legacy


def copper_dagger(player,creature):
    mana = 3
    damage = 3

    if(creature.curr_mana >= mana):
        player.take_damage(damage)
        creature.deplete_mana(mana)
    else:
        print("NOT ENOUGH MANA.")

def claws(player,creature):
    mana = 2
    damage = 1

    if(creature.curr_mana >= mana):
        player.take_damage(damage)
        creature.deplete_mana(mana)
    else:
        print("NOT ENOUGH MANA.")

weapon_dict = {"copper dagger" : copper_dagger,
               "claws" : claws
}