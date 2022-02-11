from items import *
from characters import *

room_time_machine = {
    "name": "The Time Machine",
    "description": """Your base of Operations. Use this Time Machine to travel to the different
time periods to solve puzzles and return history back to normal. """, 
    "exits": {"ww2":"The Listening Station", "greek":"Tanagra", "tudors":"Hampton Court"},
    "items": [], 
    "npc": []
}

# ww2 rooms:

# intercept message in this room
room_listening_station = {
    "name": "The Listening Station",
    "description": """You are in the listening station.
Around you there's people in uniform writing away whilst listening to a radio phone.
You wonder why none of it is in English? Use a radio to listen in on the message.
East of you is the general's office, where you can translate the messages when needed.""",
    "exits": {"south": "The Time Machine", "east": "Your Office", "west": "Hut 4"},
    "items": [],
    "npc": []
}

# change from morse code to ciphertext in this room
room_morse_code = {
    "name": "The Office",
    "description": """You have entered the office, opening every drawer to check for
the piece of paper that will help you decode the message. Where is it?! 
Upon opening the bottom most drawer of the desk, you see the morse alphabet chart
that you were looking for. This will bring you one step closer to going home!
West of the office is the Listening Station, 
Bletchley park hut 4 is situated north of you.
    """,
    "exits": {"west": "The Listening Station", "north": "Hut 4"},
    "items": [items_morse_alphabet],
    "npc": []
}

# decrypt message in Bletchley Park using Colossus computer in this room
room_decryption = {
    "name": "Hut 4",
    "description": """You are standing in front of a computer named Colossus, 
next to a group of some of the most famous cryptographers of the war.
They inform you that using this computer is your only hope of deciphering the
message you intercepted from the germans, assuming you have translated it from
morse code already. Let's hope this computer can figure out the secret message!
The office is to the south of you, and the time machine is to the east.""",
    "exits": {"south": "Your Office", "east": "The Time Machine"},
    "items": [items_computer],
    "npc": []
}


# Greek rooms:

# Main Lobby area will be near Thebes, so I have chosen Tanagra as a starting area, as it is near ancient Thebes
room_Tanagra = {
    "name": "Tanagra",
    "description": """The city is on a height and looks over many green, beautiful meadows known for their fertility.
You are surrounded by chalky, white buildings in the middle of the city.
There are plenty of vendors selling local wines.
You see a sign saying that Thebes can be found to the west.

You are approached by a startled man.
'Hello, my name is Perseus, I can tell from your wardrobe that you're not from this time...

Maybe that means you can help me! I had previously killed the beast Medusa; however,
a man who also wasn't from this time came back and unleashed her wrath upon the nearby town of Thebes!

She is currently terrifying Kadmeia, the acropolis of Thebes. The man from the future left behind this
weird item'
 
 (It looks just like a radio to you) 
 
'If you can end Medusa's wrath and bring me her head,
I will give it to you!'""",
    "exits": {"west": "Elektra", "north":"The Time Machine"},
    "items": [],
    "npc": "Perseus"
}


room_Elektra = {
    "name": "Elektra",
    "description": """The only open gate leading to the acropolis of Thebes, the rest having been blocked by Medusa.

Beside the gate, there is a large, pearly white tower upon which the Sphinx sits and watches.

The city has reduced to rubble and through the gate you can see many people captured in stone.""",
    "exits": {"east": "Tanagra"},
    "items": [],
    "npc": "Sphinx"
}
# Conversation here with Sphinx giving riddle, mirror added to room after solving riddle

# Perseus must say in conversation that Elektra is the only passable gate

room_Kadmeia = {
    "name": "Kadmeia",
    "description": """The acropolis and most important part of Thebes.

On every side of you there are the faces of those petrified by the beast Medusa.
Full families turned to stone whilst cowering together in fear.

You see some men who challenged her, now in stone, who tried in vain to protect others.

Ahead of you stands the one behind it all, Medusa.""",
    "exits": {"south": "Elektra"},
    "items": [],
    "npc": "Medusa"
}


#tudor rooms:

room_court = {
    "name": "Hampton Court",
    "description": """The main residence of King Henry VIII. All around you astronomical clocks and tapestries decorate the walls.
Outside, you can see acres of twisting hedge mazes and the bank of the River Thames.
You turn to find King Henry standing in the corner of the room...

King Henry VIII: "Do NOT speak to me peasant until you bring me my prized tudor key and USE it.""",
    "exits": {"east": "The Tower of London", "north": "The Time Machine", "west": "Windsor Castle"}, #Have a Machine exit to go to a different map?? - will need to rely on global room most likely.
    "items": [],
    "npc": "King Henry VIII"
    }
    
#need to come here to play mini game
room_tower = {
    "name": "The Tower of London",
    "description": """Built by the Romans, the Tudors used this fortress as a place of imprisonment and torture. The Tower of London held many executions, including a few
of King Henry's wives....""",
    "exits": {"west": "Hampton Court", "north": "Bosworth Field", "south": "Windsor Castle" },
    "items": [],
    "npc": []
    }


room_battlefield = {
    "name": "Bosworth Field",
    "description": """Location of the infamous 'Battle of Bosworth',
the last battle in the War of the Roses. The House of
Lancaster beat the House of York and started the Tudor
Monarchy. Henry VIII assumed the throne and would later pass down the title to his son, King Henry VIII""",
    "exits": {"south": "The Tower of London", "west": "Windsor Castle"},
    "items": [items_tudor_spears, items_tudor_torch],#Torch to uncover another hint within game
    "npc": []
    }

room_castle = {
    "name": "Windsor Castle",
    "description": """The oldest occupied castle to date,
containing the burial place of ten monarchs,
including Henry and his beloved wife Jane Seymour.""", 
    "exits": {"east": "Hampton Court", "south": "The Tower of London", "north": "Bosworth Field"},
    "items": [items_tudor_room_key], # use room key to speak with Henry VIII about the minigame.
    "npc": []
    }

#dictionary of all room names:
rooms = {
    "The Time Machine": room_time_machine,
    "The Listening Station": room_listening_station,
    "Your Office": room_morse_code,
    "Hut 4": room_decryption,
    "Hampton Court": room_court, 
    "The Tower of London": room_tower, 
    "Bosworth Field": room_battlefield, 
    "Windsor Castle": room_castle ,
    "Elektra": room_Elektra,
    "Kadmeia": room_Kadmeia,
    "Tanagra": room_Tanagra
}

