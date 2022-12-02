import re

# this script looks for phrases on cards that corresponds with triggers from MTG/triggers.py
# it will then write the corresponding trigger for that card in the format of data/m15_cards.txt

# STEPS FOR ADDING A NEW TRIGGER PHRASE
# 1. add the phrase to phrase_string in main
# 2. add the check for that phrase in map_trigger
#      if the trigger .write line already exists in map_trigger, add the phrase to the if statement with an OR
#      if the trigger .write does not exist for the trigger, add a new if statement
# 3. update the comments


# map an extracted card text phrase to write the corresponding trigger from MTG/triggers.py
#   input: phrase - one of the extracted card text phrases from the regex string, phrase_string, in main
def map_trigger(phrase):
  f_out.write("\n\t\tTriggers:\n")

  # depending on regex, may have to check if input phrase is in the target phrase
  #   rather than if it equals the target phrase because,
  #   for some, it helps to put the card name in the regex string
  #   e.g. 'When _______ attacks' is different than having just 'attacks' on the card
  #   therefore, the regex needs to extract 'When *card name* attacks',
  #   so we have to check if the keyword is in the extracted string

  # trigger: onEtB
  # phrases: {card name} enters the battlefield
  if "enters the battlefield" in phrase:
    f_out.write("\t\t\t\tonEtB\n")

  # trigger: onDraw
  # phrases: Whenever you draw a card
  if "Whenever you draw a card" in phrase:
    f_out.write("\t\t\t\tonDraw\n")

  # trigger: onDiscard
  # phrases: Whenever you discard; Whenever you cycle or discard a card
  if "discard" in phrase:
    f_out.write("\t\t\t\tonDiscard\n")

  # trigger: onEnterGrave
  # phrases: put into a graveyard
  if "graveyard" in phrase:
    f_out.write("\t\t\t\tonEnterGrave\n")

  # trigger: onDeath
  # phrases: {card name} dies
  if "dies" in phrase:
    f_out.write("\t\t\t\tonDeath\n")

  # trigger: onLeaveBattlefield
  # phrases: {card name} leaves the battlefield
  if "leaves the battlefield" in phrase:
    f_out.write("\t\t\t\tonLeaveBattlefield\n")

  # trigger: onControllerLifeGain
  # phrases: you gain life
  if phrase == "you gain life":
    f_out.write("\t\t\t\tonControllerLifeGain\n")

  # trigger: onUpkeep
  # phrases: beginning of ____ upkeep
  if "upkeep" in phrase:
    f_out.write("\t\t\t\tonUpkeep\n")

  # trigger: onAttack
  # phrases: attacks
  if "attacks" in phrase:
    f_out.write("\t\t\t\tonAttack\n")

  # trigger: onTakeCombatDamage
  # phrases: is dealt combat damage
  if phrase == "is dealt combat damage":
    f_out.write("\t\t\t\tonTakeCombatDamage\n")

  # trigger: onControllerDrawCard
  # phrases: you draw a card
  if phrase == "you draw a card":
    f_out.write("\t\t\t\tonControllerDrawCard\n")

  # trigger: onDeath
  # phrases: dies
  if phrase == "dies":
    f_out.write("\t\t\t\tonDeath\n")

  #onCombatDamageToPlayers
  if "deals combat damage to a player" in phrase:
    f_out.write("\t\t\t\tonCombatDamageToPlayers\n")

  if phrase == "blocks":
    f_out.write("\t\t\t\tonBlock\n")

  if "is dealt combage damage" in phrase:
    f_out.write("\t\t\t\onTakeCombatDamage\n")

  if "whenever you lose a life" in phrase:
    f_out.write("\t\t\t\onControllerLifeLoss\n")

  if "target player discard" in phrases:
    f_out.write("\t\t\t\onControllerDiscard\n")

    #zaber
    '''
      if "end" in phrase:
        if next token "of combat":
          f_out.write(onEndofCombat)
        elif next token "step":
          f_out.write(onEndstep)
          f_out.write(onCleanup)
      '''
  #Could not find keywords for: onControllerDeclareAttackers, onDeclareBlockers

  #onDeclareAttackers
  if "during combat before blockers are declared" in phrase:
    f_out.write("\t\t\t\tonDeclareAttackers")
    #combat phases in order (BeginningOfCombat, DeclareAttackers, DeclareBlockers, FirstStrikeCombatDamage, CombatDamage, EndOfCombat)

  #onEnterCombat (could not find onControllerEndofCombat)
  if "during your turn , before attackers are declared" in phrase:
    f_out.write("\t\t\t\tonEnterCombat")

  #onControllerDeclareBlockers
  if "trample" in phrase:
    f_out.write("\t\t\t\tonControllerDeclareBlockers")

  #onEndofCombat
  if "end of combat" in phrase:
    f_out.write("\t\t\t\tonEndofCombat")

  #onEndstep, onCleanup
  if "end step" in phrase:
    f_out.write("\t\t\t\tonEndstep")

  #onUntap
  if "during your untap step" in phrase:
    f_out.write("\t\t\t\tonUntap")

  #"during your turn" could be on onMain1 -> this is the precombat phase

  #onUpkeep, onControllerUpkeep
  if "upkeep" in phrase:
    if "your upkeep" in phrase:
      f_out.write("\t\t\t\tonControllerUpkeep")
    else:
      f_out.write("\t\t\t\tonUpkeep")
      #Phrases: each upkeep, next turn's upkeep, each player's upkeep, first upkeep, each opponent's upkeep

  #onPermanentEtB
  if "permanent.*?enters the battlefield" in phrase:
    f_out.write("\t\t\t\tonPermanentEtB")

  #need permanent + {filler} + enters the battle field
  #Whenever a permanent enters the battlefield
  #Whenever a permanent that shares an artist with another permanent you control enters the battlefield
  #Whenever another permanent enters the battlefield
  '''      
    #onLifeGain --------- COME BACK TO IT
    if {"gain", "life"}.issubset(set(phrase.split())):
      f_out.write("\t\t\t\onLifeGain\n")
    '''


#################################################################
# main:                                                         #
#   uses regex to search for phrases                            #
#   passes found phrases to map_trigger() above to write        #
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

    # extract and map trigger phrases to triggers

    # each regex string should include a phrase that will map to a corresponding trigger,
    # plus the | operator which means OR;
    # this allows multiple phrases to be extracted from the same card
    phrase_string = ("(you gain life|" + "{0} enters the battlefield|" +
                     "beginning of.*?upkeep|" + "{0} attacks|" +
                     "{0} is dealt combat damage|" + "you draw a card|" +
                     "{0} dies|" + "deals combat damage to a player|" +
                     "{0} blocks|" + "Whenever you draw a card|" +
                     "Whenever you discard a card|" +
                     "Whenever you cycle or discard a card|" +
                     "put into a graveyard|" + "{0} dies|" +
                     "{0} leaves the battlefield|"+
                     "{0} is dealt combat damage|" +
                     "whenever you lose a life|" +
                     "target player discard|")
                    
    ''' Text to add
            gain.*?life)" 
        '''

    # fill in {0} holes with card name for phrases that specifically mention the card
    phrase_string = phrase_string.format(name)

    # use regex to get all extracted phrases from the card text
    phrases = re.findall(re.compile(phrase_string), line)
    if phrases:  # if phrases list is not empty, i.e. phrases were found
      # for each phrase
      for p in phrases:
        # call map_trigger with the phrase to map it to the trigger output
        map_trigger(p)

    # write 30 '#'s; newline for next card
    f_out.write("\n\n")
    f_out.write("#" * 30)
    f_out.write("\n\n")

  f_in.close()
  f_out.close()
