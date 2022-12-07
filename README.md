# automation/
This folder contains the file `magic_card_converter.py` which is our attempt at automating the conversion of cards so as to follow the format presented in M15.
Instructions for adding a trigger to this file are outlined in comments in `magic_card_converter.py`

The file `test_magic.txt` contains the card that need to be converted and they follow the following format:

- {_card_name_} **NAME_END** {_card_attack_} **ATK_END** {_card_defend_} **DEF_END** {_mana_} **COST_END** {_dur_end_} **DUR_END** {_card_type (enchantment, instant, creature)_} **TYPE_END** {_'player_cls_end'_} **PLAYER_CLS_END** {_'race_end'_} **RACE_END** {_card_rarity_} **RARITY_END** {_card_text_}

The file `magic_card_conversion.txt` contains the output from the automation script `magic_card_converter.py`

**Future plans involve:** 
- Finishing all trigger implementations and adding simple functions like gain life or draw card
  - Initial work to be done on this involves figuring out how to nest needed functions within triggers or how to add functions that aren't trigger based

- Add `map_abilities` function
  - Add upon completion of `map_triggers`
- Add script for effects
  - Must be implemented upon the completion of the above points
- Test coverage of the script
  - Can be done at anytime

# everyone's work/
This folder contains 4 textfiles, which contain the cards that we have converted so far.

A card may contain **abilities**, **triggers** and **targets** and those are derived from the card's text.

The cards follow the format of:
- Card name
- Abilities
- Triggers
  - effects or targets which call also call on existing functions within the python MTG game.

**We have not tested the conversions on the textfiles yet, we believe that most are correct, and that some may need to be revisited.**

# card-text-search-ben/
Ben has created a script that uses a massive csv file (contains lots of cards along with their text) to find key words in cards which can be used to associate with triggers, abilities and effects.

### How to use
- Replace the input in the `str.contains` call with your desired text
- Run the jupyter notebook file.

# functions-abilities-triggers/
This folder contains the *abilities*, *triggers*, *colors*, and *functions* found in the python implementation of Magic The Gathering that we are using as reference.

All the triggers that have been implemented in the MTG python game up until this point, can be found in `functions-abilities-triggers/triggers.txt`. The file contains a list of triggers and their definition following a "#".

`functions-abilities-triggers/functions.txt` contains a list of all the functions that we have encountered along with their parameters and objects.

Like `triggers.txt`, `functions-abilities-triggers/abilities.txt` and `functions-abilities-triggers/colors.txt` contain lists of card abilities, and colors with their respective definitions following a "#".

# Issues and complications

We faced some intepretation issues when we came across some triggers. Like when should use **"onControllerLifeGain"** vs **"onLifeGain"** ? We *need to make a decision* on how to go about these ambiguous triggers.

Moreover, we believe that there is a need for a trigger for controller untap... refer to card "Encase in Ice"

We also noticed that card text is different from  `test_magic` text and a lot of the current triggers may not account for that.

We could not get the python game to run. Need to either write our own (?) or figure out how to make it run, so that we can objectively test the work that we've done so far.

Another issue is that our current automation script sometimes finds two triggers instead of just one. Refer to _Sapling of colfenor_ in `ANALYSIS_OF_OUTPUT.txt`
