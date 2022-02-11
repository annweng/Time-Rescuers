from items import *
#give hints and allow access to the mini game
character_king_henry = {
    "id": "King Henry VIII",
    "name": "King Henry VIII",
    "room": "room_court ",
    "speech": True
    }

character_perseus = {
    "id": "Perseus",
    "name": "Perseus",
    "inventory": [items_ww2_radio],
    "room": "room_Tanagra",
    "speech": False
}
# Give function with Perseus to swap key for head
character_sphinx = {
    "id": "Sphinx",
    "name": "Sphinx",
    "health": 1,
    "inventory": items_mirror,
    "room": "room_Elektra",
    "dialogue": "test",
    "speech": False
}
# When Sphinx takes 1 damage, item in inventory is added to room and can be taken
character_medusa = {
    "id": "Medusa",
    "name": "Medusa",
    "health": 2,
    "inventory": [items_medusa_head],
    "room": "room_Kadmeia",
    "speech": False
}
# Medusa is turned to stone at 1 health, loses her head when one damage is dealt by the item used to remove her head

character = {
    "King Henry VIII": character_king_henry,
    "Perseus": character_perseus,
    "Medusa": character_medusa,
    "Sphinx": character_sphinx
}
