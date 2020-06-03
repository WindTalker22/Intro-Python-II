from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name?: "), room["outside"])


# Write a loop that:
while True:
    try:
# * Prints the current room name
        print(f"\nCurrent room: {player.current_room.name}")

# * Prints the current description (the textwrap module might be useful here).
        print(f"\nRoom description: {player.current_room.description}")

# * Waits for user input and decides what to do.
        commands = ["n - north", "s - south", "e - east", "w - west", "q - quit"]
        print("\nCommands are as follows...")
        for i in commands:
            print(i)

        print("\n**********************************************")
        command = input("\nChoose a command: ")
        print("\n**********************************************\n")

# If the user enters "q", quit the game.
        if command == "q":
            print("\n**********************************************")
            print(f"\nThanks for playing {player.name}")
            print("\n**********************************************\n")
            break

# If the user enters a cardinal direction, attempt to move to the room there.
        if command == "n":
                if player.current_room.n_to == None:
                    print("\n The way through is blocked find another way")
                else:
                    player.change_room(player.current_room.n_to)


        if command == "s":
                if player.current_room.s_to == None:
                    print("\nThe way through is blocked find another way")
                else:
                    player.change_room(player.current_room.s_to)


        if command == "e":
                if player.current_room.e_to == None:
                    print("\n The way through is blocked find another way")
                else:
                    player.change_room(player.current_room.e_to)


        if command == "w":
                if player.current_room.w_to == None:
                    print("\nThe way through is blocked find another way")
                else:
                    player.change_room(player.current_room.w_to)
        
# Print an error message if the movement isn't allowed.
    except AttributeError:
        print("Something must have went wrong")

