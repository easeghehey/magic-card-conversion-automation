# automation/
This folder contains the file `magic_card_converter.py` which is our attempt at automating the conversion of cards so as to follow the format presented in M15.

# everyone's work/
This folder contains 4 textfiles, which contain the cards that we have converted so far.

A card may contain **abilities**, **triggers** and **targets** and those are derived from the card's text.

The cards follow the format of:
- Card name
- Abilities
- Triggers
  - effects or targets which call also call on existing functions within the python MTG game.

# card-text-search-ben/
Ben has created a script that uses a massive csv file (contains lots of cards with their text) to find key words in cards which use to associate with triggers, abilities and effects.

### How to use
Replace the input in the `str.contains` call with your desired text and run the jupyter notebook file.

# functions-abilities-triggers/
This folder contains the *abilities*, *triggers*, *colors*, and *functions* found in the python implementation of Magic The Gathering that we are using as reference.

All the triggers that have been implemented in the MTG python game up until this point, can be found in `functions-abilities-triggers/triggers.txt`. The file contains a list of triggers and their definition following a "#".

`functions-abilities-triggers/functions.txt` contains a list of all the functions that we have encountered along with their parameters and objects.

Like `triggers.txt`, `functions-abilities-triggers/abilities.txt` and `functions-abilities-triggers/colors.txt` contain lists of card abilities, and colors with their respective definitions following a "#".

# Issues and complications

We faced some intepretation issues when we came across some triggers. Like when should use **"onControllerLifeGain"** vs **"onLifeGain"** ? We need to make a decision on how to go about these ambiguous triggers.

Moreover, we believe that there is a need for a trigger for controller untap... refer to card "Encase in Ice"