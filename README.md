# magic-card-conversion-automation

The function `map_<card characteristic>` takes a parameter <characteristic> and outputs the text with the relevant characteristics onto *magic_card_conversions.txt*

The variable(s) `<characteristic>_string` contain the common patterns for a given characteristic. We use those patterns to determine if the text on the card is an ability, trigger, etc. Once that is determined, the code calls on `map_<characteristic>`
