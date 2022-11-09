import re

# Emanuel
def map_abilities(ability):
    f_out.write("\n\t\tAbilities:\n")

#Anyone
def map_targets(target):
    f_out.write("\n\t\tAbilities:\n")

# Ben
# map a trigger keyword to write the correct trigger in MTG/triggers.py
def map_trigger(trigger):
    f_out.write("\n\t\tTriggers:\n")

    # depending on regex, may have to check if keyword is in the extract trigger
    # for some, it helps to put the card name in the regex string
    #   e.g. 'When _______ attacks' is different than having just 'attacks' on the card
    #   here, we have to check if the keyword is in the extracted string

    # onControllerLifeGain
    #   you gain life
    if trigger == "you gain life":
        f_out.write("\t\t\t\tonControllerLifeGain\n")

    # onEtB
    #   enters the battlefield
    if "enters the battlefield" in trigger:
        f_out.write("\t\t\t\tonEtB\n")

    # onUpkeep
    #   beginning of ____ upkeep
    if "upkeep" in trigger:
        f_out.write("\t\t\t\tonUpkeep\n")

    # onAttack
    #   attacks
    if "attacks" in trigger:
        f_out.write("\t\t\t\tonAttack\n")

    # onTakeCombatDamage
    #   is dealt combat damage
    if trigger == "is dealt combat damage":
        f_out.write("\t\t\t\tonTakeCombatDamage\n")

    # onControllerDrawCard
    #   you draw a card
    if trigger == "you draw a card":
        f_out.write("\t\t\t\tonControllerDrawCard\n")
    
    # onDeath
    #   dies
    if trigger == "dies":
        f_out.write("\t\t\t\tonDeath\n")
    
    #Zaber. not tested yet
    #   if trigger =="as long as":
    #   get next line = 'enchanted' 'artifact'
    #   f_out.write("lambda eff: eff.source.controller.controls()")

#################################################################
# main:                                                         #
#   uses regex to search for keywords                           #
#   passes keywords to functions above to *try to* write        #
#        the corresponding code for the m15_cards.txt file      #
#                                                               #
#   add to above functions as you encounter new cases           #
#   the goal is to only have to check the majority of the cards #
#################################################################
if __name__ == "__main__":
    f_in = open("test_magic.txt", "r")
    global f_out
    f_out = open("magic_card_conversions.txt", "w")

    for line in f_in:
        # write 30 '#'s
        f_out.write("#" * 30)
        f_out.write("\n")

        # extract and write card name
        name_match = re.search(r"(.*?)( NAME_END)", line)
        name = name_match.group(1)
        f_out.write(name)

        # extract and map any ability keywords -- work in progress
        ability_string = "" # look for colors as those usually are followed by an ability + do study of ability cards to determine pattern
        abilities = re.findall(re.compile(ability_string), line)

        for a in abilities:
            map_abilities(a)

        # extract and map any trigger keywords
        trigger_string = "(you gain life|{0} enters the battlefield|beginning of.*?upkeep|{0} attacks|{0} is dealt combat damage|you draw a card|{0} dies)".format(name)
        triggers = re.findall(re.compile(trigger_string), line)
        if triggers: # if triggers list is not empty
            for t in triggers:
                map_trigger(t)

        
        # write 30 '#'s; newline for next card
        f_out.write("\n\n")
        f_out.write("#" * 30)
        f_out.write("\n\n")


    f_in.close()
    f_out.close()
