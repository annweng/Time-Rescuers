from gameparser import *
from Map import *
from characters import *
from player import *
from Questions import *
from Introduction_quiz import *
import random

message = "Password is transtemporal mission completed."
key_used = False
greek_done = False
tudor_done = False


def sphinx_riddle():
    print("""To pass through the Gate of Elektra into the acropolis of Thebes,
you must first answer my riddle.
 
Once completed, I will throw myself from this podium.

Would you like to begin?""")
    print()
    print("Yes or No?")
    print()
    startriddle = input()
    i = 0
    hintcount = 0
    answer = False
    global greek_done
    if "yes" in normalise_input(startriddle):
        while not answer:
            if i >= 2 and hintcount == 0:
                print("Would you like a hint?")
                print("Yes or no?")
                print()
                hint = input()
                print()
                if "yes" in normalise_input(hint):
                    print("The words for day and night are both feminine in Greek")
                    hintcount = 1

                else:
                    print("Good Luck!")
                    hintcount = 1

            print("""There are two sisters; One sister gives birth to the other,
who in turn gives birth to the other.""")
            print('Who are the two sisters?')
            print()
            playeranswer = input()
            if "day" and "night" in str(normalise_input(playeranswer)):
                print("""'You have solved my riddle, good luck at facing the challenge ahead.
Do not let the horrible sights get to you, I may leave behind an item that will help you.'
                
The sphinx hits the ground and shatters into rubble,
in the wreckage you notice something shining in the sunlight.""")
                room_Elektra["items"].append(items_mirror)
                room_Elektra["description"] = """The only open gate leading to the acropolis of Thebes, the rest 
having been blocked by Medusa."

Beside the gate, there is a large, pearly white tower upon which the Sphinx previously sat.

The Sphinx now lies before you in rubble.
The city has reduced to rubble and through the gate you can see many people captured in stone. """
                character_sphinx["health"] = 0
                room_Elektra["exits"] = {"east": "Tanagra", "north": "Kadmeia"}
                greek_done = True
                answer = True

            else:
                i = i + 1

    else:
        print("Come back when you're up to the challenge, but the people won't survive much longer!")


def swap_item():
    if current_room == room_Tanagra:
        if items_medusa_head in inventory:
            inventory.remove(items_medusa_head)
            inventory.append(items_ww2_radio)
            print("""You've saved us all! Here, have this radio.""")
        else:
            print("You still haven't defeated Medusa!")


# tudor specific functions:

def start_tudor_minigame():
    global inventory
    global tudor_done
    tudor_done = True
    random_available_hints = ["None of the Catherine's have the same answer",
                              "The two wives with locations in their name have the same answer"]  # definition of available hints using a list (allowing random hint to be provided).
    print(
        "============ MINI GAME ============\n\nMatch King Henry's wives to their unfortunate ends!\n\nWere they Divorced, Executed, Widowed or did they Die?\n\n")  # primary output for introducing the game, outputs the possible words the player can input.
    if items_tudor_torch in inventory:
        print(
            "As you managed to locate a spare torch from the Battlefield, you can uncover a starter hint, you found: 'Cathrine Parr was Henry's last wife' scratched into the wall; don't forget that!")
        inventory.remove(items_tudor_torch)
    answer_correct_catherine_a = False  # pre-define all variables required for the game.
    answer_correct_anne_b = False
    answer_correct_jane = False
    answer_correct_anne_c = False
    answer_correct_catherine_h = False
    answer_correct_catherine_p = False
    answer_correct_count = 0
    attempts_completed = 1
    answer_incorrect_list = []
    while (attempts_completed <= 3) and (
            answer_correct_count != 6):  # creates the loop limiting attempts to three and checks to make sure not all questions were answered/completed correctly.
        if (
                answer_correct_catherine_a is False):  # changes if answer was correct from previously, means question can be skipped from being asked.
            answer_catherine_a = normalise_input(
                input("Catherine of Aragon: "))  # request player to provide their guess and is normalised.
            if answer_catherine_a == ['divorced']:  # checks if player has inputted the correct answer using normalised input.
                answer_correct_catherine_a = True  # amends variable for checking if question answered correctly, enables skipping of questions.
                answer_correct_count += 1  # used to check when player has finished all questions correctly.
            else:
                answer_incorrect_list.append(
                    "Catherine of Aragon")  # adds to list to output at end of the loop incorrect answers.
        if answer_correct_anne_b is False:  # (below repeats of the above notes, see above for explanation if required).
            answer_anne_b = normalise_input(input("Anne Boleyn: "))
            if answer_anne_b == ['executed']:
                answer_correct_anne_b = True
                answer_correct_count += 1
            else:
                answer_incorrect_list.append("Anne Boleyn")
        if not answer_correct_jane:
            answer_jane = normalise_input(input("Jane Seymour: "))
            if answer_jane == ['died']:
                answer_correct_jane = True
                answer_correct_count += 1
            else:
                answer_incorrect_list.append("Jane Seymour")
        if not answer_correct_anne_c:
            answer_anne_c = normalise_input(input("Anne of Cleves: "))
            if answer_anne_c == ['divorced']:
                answer_correct_anne_c = True
                answer_correct_count += 1
            else:
                answer_incorrect_list.append("Anne of Cleves")
        if not answer_correct_catherine_h:
            answer_catherine_h = normalise_input(input("Catherine Howard: "))
            if answer_catherine_h == ['executed']:
                answer_correct_catherine_h = True
                answer_correct_count += 1
            else:
                answer_incorrect_list.append("Catherine Howard")
        if not answer_correct_catherine_p:
            answer_catherine_p = normalise_input(input("Catherine Parr: "))
            if answer_catherine_p == ['widowed']:
                answer_correct_catherine_p = True
                answer_correct_count += 1
            else:
                answer_incorrect_list.append("Catherine Parr")

        attempts_completed += 1
        if answer_correct_count == 6:  # if the player has inputted six correct answers, complete the following.
            print(
                "\nCongratulations, you won! Return to the timemachine to quickly escape this time period while you can.\n A keyword for you to remember is 'Christopher'; don't forget it, it's important! \n If you ever need to look back, just use the note in your inventory.")
            inventory.append(items_keyword_note)
        elif attempts_completed <= 3:
            current_hint = random.choice(random_available_hints)  # randomly select from available hints.
            random_available_hints.remove(current_hint)  # remove randomly selected hint to prevent repeating.
            print("Looks like you got some incorrect, have another go; attempt number: " + str(
                attempts_completed) + "/3. Your incorrect answers were: " + str(
                answer_incorrect_list) + ". Here is a hint to assist you: '" + current_hint + "'\n")
            # increment attempts completed enabling maximum attempts of three.
            answer_incorrect_list.clear()  # clears list of incorrect answers for next game.
        else:
            print(
                "Unfortunately, you lost! You need to quickly escape this time period via the time machine quickly. \n A keyword for you to remember is 'Christopher'; don't forget it, it's important! \n If you ever need to look back, just use the note in your inventory.")
            inventory.append(items_keyword_note)


# ww2 specific functions:
global mc_dict
mc_dict = {' ': '/', 'A': '.-', 'B': '-...',
           'C': '-.-.', 'D': '-..', 'E': '.',
           'F': '..-.', 'G': '--.', 'H': '....',
           'I': '..', 'J': '.---', 'K': '-.-',
           'L': '.-..', 'M': '--', 'N': '-.',
           'O': '---', 'P': '.--.', 'Q': '--.-',
           'R': '.-.', 'S': '...', 'T': '-',
           'U': '..-', 'V': '...-', 'W': '.--',
           'X': '-..-', 'Y': '-.--', 'Z': '--..',
           '1': '.----', '2': '..---', '3': '...--',
           '4': '....-', '5': '.....', '6': '-....',
           '7': '--...', '8': '---..', '9': '----.',
           '0': '-----', ',': '--..--', '.': '.-.-.-',
           '?': '..--..', '/': '-..-.', '-': '-....-',
           '(': '-.--.', ')': '-.--.-', '!': '--.-.--'}


def encryption_m(plain_text):  # Plain Text to Morse Code

    global morse_gen  # this could be an item?
    morse_gen = ''

    for x in plain_text:
        x = x.upper()
        values = mc_dict[x]
        morse_gen += values  # morse_gen is
        morse_gen += ' '

    return morse_gen


def decryption_m(morse_gen):  # morse code to ciphertext
    decrypt = {a: b for b, a in mc_dict.items()}  # flips key-value pair
    radio = morse_gen
    radio = radio.split()
    morse_alphabet = ''
    for x in radio:
        values = decrypt[x]
        # morse_alphabet += ' '
        morse_alphabet += values
    return morse_alphabet


def createKey(text, keyword):
    """This function takes a string of text that needs to be decrypted
    and the keyword with which it has been encrypted to generate the 
    key to decrypt it with. Generates the key (Vigenere cipher) from the 
    keyword in a cycle, until it matches the length of the string of text. 
    """
    if len(keyword) > len(text):
        print("Error key is larger than ciphertext")
    elif len(keyword) == len(text):  # if the length matches up already nothing has to be done
        return keyword.lower()
    else:
        key = list(keyword.lower())  # change type so letters can easily be appended
        for i in range(len(text) - len(key)):  # len changes with spaces???
            key.append(key[i % len(key)])  # mod keeps track of which letter needs to be added to the key
        return ("".join(key))  # return string version of key


def decrypt(cipher_text, keyword):  # gets parameters as input from user in use function
    """This function takes the ciphertext and key and decrypts the ciphertext
    into its original text according to the Vigenère cipher. 
    Assumes the alphabet to be denoted as [A-Z] = [0-25], with punctuation added on
    Returns original text in form of a string.
    """
    original_text = []
    cipher_text = cipher_text.lower()
    key = createKey(cipher_text, keyword)
    alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8,
                "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
                "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25,
                " ": 26, ".": 27, ",": 28, "!": 29, "?": 30}
    for i in range(len(cipher_text)):
        char_index = (alphabet[cipher_text[i]] - alphabet[key[i]] + 31) % 31
        next_char = ""
        for letter in alphabet:
            if alphabet[letter] == char_index:
                next_char = letter
                original_text.append(next_char)
    return "".join(original_text)


def encrypt(original_text, keyword):  # not actually accessed by player, just for us to encrypt message
    """This function takes the original text and key and encrypts the original text
    into its cipher text according to the Vigenère cipher. 
    Assumes the alphabet to be denoted as [A-Z] = [0-25], with punctuation added on
    Returns cipher text in form of a string.
    """
    cipher_text = []
    original_text = original_text.lower()
    key = createKey(original_text, keyword)
    alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8,
                "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
                "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25,
                " ": 26, ".": 27, ",": 28, "!": 29, "?": 30}
    for i in range(len(original_text)):
        char_index = (alphabet[original_text[i]] + alphabet[key[i]]) % 31
        next_char = ""
        for letter in alphabet:
            if alphabet[letter] == char_index:
                next_char = letter
                cipher_text.append(next_char)
    return "".join(cipher_text)


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([items_tudor_torch, items_ww2_radio])
    'a torch, a radio'

    >>> list_of_items([items_tudor_spears])
    'a spear'

    >>> list_of_items([])
    ''

    """
    items_list = []
    for item in items:
        items_list.append(item["name"])
    items_string = ", ".join(items_list)
    return items_string


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Your Office"])
    There is a morse alphabet chart here.
    <BLANKLINE>

    >>> print_room_items(rooms["The Time Machine"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if not room["items"]:
        return
    else:
        print("There is " + list_of_items(room["items"]) + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.".
    """
    if not inventory:
        return
    else:
        print("You have " + list_of_items(items) + ".\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["The Listening Station"])
    <BLANKLINE>
    THE LISTENING STATION
    <BLANKLINE>
    You are in the listening station.
    Around you there's people in uniform writing away whilst listening to a radio phone.
    You wonder why none of it is in English? Use a radio to listen in on the message.
    Return South to go back to the time machine, 
    East to your office or west to Bletchley park hut 4.
    <BLANKLINE>
    There is a radio here.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    # Display items in the room, if there are any
    if print_room_items(room) is None:
        return
    else:
        print(print_room_items(room))
        print()


def exit_leads_to(exits, direction):  # might need the rooms as parameter to specify time periods
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["The Listening Station"]["exits"], "east")
    'Your Office'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "The Time Machine")
    GO EAST to The Time Machine.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["The Time Machine"]["exits"], "greek")
    True
    >>> is_valid_exit(rooms["The Time Machine"]["exits"], "south")
    False
    >>> is_valid_exit(rooms["The Listening Station"]["exits"], "west")
    True
    >>> is_valid_exit(rooms["Elektra"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def print_menu(exits, room_items, inv_items, room_characters):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "USE <ITEM ID> to use <item name>."

    For example, the menu of actions available at the listening station may look like this:

    You can:
    GO EAST to your office.
    GO WEST to hut 4.
    GO SOUTH to the time machine.
    TAKE RADIO to take a radio.
    USE RADIO to use your id card.
    What do you want to do?

    """
    print("You can:\n")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        if item != items_keyword_note:
            print("USE " + item["id"].upper() + " to use your " + item["name"] + ".")
    for character in room_characters:
        if character == "speech" and character:
            print("SPEAK to " + character["id"].upper() + ".")
    if items_keyword_note in inventory:
        print("SHOW NOTE to remind yourself of the cipher.")
    print()
    print("What do you want to do?")


def print_time_machine_menu(exits):
    global tudor_done
    global greek_done
    print("You can:\n")
    print("ENTER PASSWORD to try and return home.")
    for direction in exits:
        if direction != "ww2":
            print("GO", direction.upper(), "to travel to", direction.upper(), "time period.")
        elif direction == "ww2":
            if tudor_done is True and greek_done is True:
                print("GO", direction.upper(), "to travel to", direction.upper(),
                      "time period.")  # Print the exit name and where it leads to
    print()
    print("What do you want to do?")


def print_elektra(exits, room_items, inv_items):
    global greek_done
    print("You can:\n")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        if item != items_keyword_note:
            print("USE " + item["id"].upper() + " to use your " + item["name"] + ".")
    if not greek_done:
        print("SOLVE RIDDLE, if you're up to the challenge!")
    if items_keyword_note in inventory:
        print("SHOW NOTE to remind yourself of the cipher.")
    print()
    print("What do you want to do?")


def print_tower(exits, room_items, inv_items):
    global key_used
    global tudor_done
    print("You can:\n")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        if item != items_keyword_note:
            print("USE " + item["id"].upper() + " to use " + item["name"] + ".")
    if key_used is True and tudor_done is False:
        print("PLAY Mini-game (if you dare)")
    if items_keyword_note in inventory:
        print("SHOW NOTE to remind yourself of the cipher.")
    print()
    print("What do you want to do?")


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    if is_valid_exit(current_room["exits"], direction):
        print("Moving to ", exit_leads_to(current_room["exits"], direction))
        current_room = move(current_room["exits"], direction)
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    global current_room
    global inventory
    for item in current_room["items"]:
        if item_id == item["id"]:
            current_room["items"].remove(item)
            inventory.append(item)
            print(item["description"])
            return
    print("You cannot take that out of this room.")


def execute_use(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    global current_room
    global inventory
    global key_used
    for item in inventory:  # check whether item is in player's inventory first
        if item_id == item["id"]:
            if item_id == "computer":  # use function specific to one item
                if current_room == room_decryption:
                    cipher_text = input("Please enter the message you want to decrypt (copy paste from above): ")
                    keyword = input("Please enter the cipher used to encrypt the message (from the note): ")
                    print("The original message was (copy paste from above): ")
                    print(decrypt(cipher_text, keyword))
                    inventory.remove(item) #once used and has no use anymore, drop item
                    current_room["items"].append(item)
                    return
                else:
                    "Go to Hut 4 to use this item."
                    return
            elif item_id == "mirror":
                if current_room == room_Kadmeia:
                    print("""You approach Medusa, mirror in hand. She doesn't notice you, as you approached from behind.
You close your eyes and, after taking a deep breath, tap Medusa on the back.

She turns around, and instantly gazes into the mirror. You keep your eyes closed until you're
certain the monster has become petrified. You open your eyes and the village around you is returning to
life.

You swiftly punch at her head, which falls off much easier than you expected.""")
                    character_medusa["health"] == 0  # kills medusa
                    character_medusa["inventory"].remove(items_medusa_head)
                    current_room["items"].append(items_medusa_head)
                    inventory.remove(items_mirror)
                    current_room["items"].append(items_mirror)
                    room_Kadmeia["description"] = """The acropolis and most important part of Thebes.
                
All the families treat you like a hero.
                 
Other families are still grieving the loss of prized possessions"""

                    room_Tanagra["description"] = """The city is on a height and looks over many green, beautiful meadows known for their fertility.
                
You are surrounded by chalky, white buildings in the middle of the city.
                
There are plenty of vendors selling local wines.
                
You see a sign saying that Thebes can be found to the west.
                
Perseus is looking at you with pride in his eyes and reaches the radio out towards you."""
                    return
                else:
                    print("You stare at yourself. How vain... The Sphinx said this would help with Medusa in Kadmeia.")
                    return

            elif item_id == "radio":
                if current_room == room_listening_station:
                    print("You are listening to the radio, hearing lots of alternating beeps.\n Incoming message:")
                    print(encryption_m(encrypt(message, "christopher")))
                    inventory.remove(items_ww2_radio)
                    current_room["items"].append(items_ww2_radio)
                    return
                else:
                    print("Go to the listening station to use this item.")
                    return
            elif item_id == "morse":
                if current_room == room_morse_code:
                    encrypted_text = input("Please enter the message you'd like to translate (copy paste from above): ")
                    print("You are comparing the message to the morse alphabet chart, translating letter by letter")
                    print("The final message still makes no sense, but at least it's in the English alphabet:")
                    print(decryption_m(encrypted_text))
                    inventory.remove(items_morse_alphabet)
                    current_room["items"].append(items_morse_alphabet)
                    return
                else:
                    print("Go to the office to use this item")
                    return
            elif item_id == "medusa":
                if current_room == room_Tanagra:
                    swap_item()
                    print("You now have the radio and the people of Greece have been saved! Finish your mission!")
                    return
                else:
                    print("You must save this for Perseus in Tanagra!")
                    return
            elif item_id == "key":
                if current_room == room_court:
                    key_used = True
                    print('King Henry VIII: "Ah! My key! You have proven yourself a worthy contender for my challenge. ')
                    print('Very well, head to the Tower of London and help me decide the fates of my many wives. Only then will you find what you are looking for."')
                    print('You may find something helpful at Bosworth field...')
                    inventory.remove(items_tudor_room_key)
                    current_room["items"].append(items_tudor_room_key)
                    return
                else:
                    print("Go to Hampton Court to use this item.")
                    return
            elif item_id == "spear":
                print("Good job you just stabbed your foot and now you're bleeding !")
                return
            elif item_id == "torch":
                print("A torch! That'll come in handy in the mini-game.")
                return
            else:
                print("You cannot use that.")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    global victory
    if 0 == len(command):
        return

    if command == ["enter", "password"]:
        print("So you think you've cracked the message?")
        guess = input("Let's see if you have. Enter the password: ")
        if guess == "transtemporal mission completed":
            victory = True
        else:
            print("Incorrect password. Complete the challenges and try again.")

    elif command == ["play", "minigame"]:
        start_tudor_minigame()

    elif command == ["solve", "riddle"]:
        sphinx_riddle()

    elif command == ["show", "note"]:
        print(items_keyword_note["description"])

    elif command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items, room_characters):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """
    global current_room
    # Display menu depending on room
    if current_room == room_time_machine:
        print_time_machine_menu(exits)
    elif current_room == room_Elektra:
        print_elektra(exits, room_items, inv_items)
    elif current_room == room_tower:
        print_tower(exits, room_items, inv_items)
    else:
        print_menu(exits, room_items, inv_items, room_characters)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["The Time Machine"]["exits"], "greek") == rooms["Tanagra"]
    True
    >>> move(rooms["The Listening Station"]["exits"], "west") == rooms["Your Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    global victory
    victory = False
    print("Welcome to Time Rescuers!")
    print("We are in desperate need of your assistance.")
    print("""A group of villains have gotten hold of a time machine and altered certain events in history,
    in order to change the outcome of the Second World War. You have been chosen to counter this organisation.
    Your mission is to go back in time, complete the challenges you encounter in each time period
    and fix these altered historical events to keep disasters from taking place in the present.
    Before you can do this however, you will need a time machine. Unfortunately there is only one way of getting it:
    Convince Kirill Sidorov that you know him well enough to be his friend and get him to give you his machine.
    Best of luck to you! You're going to need it...""")
    start_game_intro()
    # Main game loop
    # Show game objective
    print("""Game objective: Complete mini-games and travel to different time periods using your keyboard to type commands :)
    Follow the prompts and watch for spelling to change the storyline of the game.

    Fix history and collect items and reach the final stage to decrypt a password and get back home!\n""")
    while not victory:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # if current room == time machine!!!
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory, current_room["npc"])

        # Execute the player's command
        execute_command(command)

        # change victory to True once game objective is achieved to exit this loop!
    print("\nCONGRATULATIONS YOU'VE DONE IT!")
    print("You have fixed history and made it back safely to the present.\n Well done time rescuer!")


if __name__ == "__main__":
    main()
