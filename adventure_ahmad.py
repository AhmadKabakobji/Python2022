############
#imports
#import all the functions from adventurelib
from adventurelib import *


############
#Define rooms
Room.item = Bag()

castle main room = Room("you are in the main room of the castle and there is four exits infront of you. ")
kitchen = Room("you are in the Kitchen look for food to escape hunger.")
hidden key to main door = Room("you entered the key room,now look for the key to open the main door. ")
NPC = Room("you ")
hallway = Room("you are in a hallway with two exits")
leaving castle door = Room("you're in the last position, use the key to unlock the door.")
basement = Room("you are in the basement, there is a key to unlock the green lock on door. ")
bedroom2 = Room("you're in bedroom2, look for tools to unlock the locks on the main door. ")
bedroom1 = Room("you are in bedroom1, take a nap and then look for clue for your next step.")
dead bodies room = Room("you are in the dead bodies room. there is plenty of dead bodies.")
ghosts room = Room("you're in the most dangerous room in the castle. you should kill all the ghosts in the room and you will find the next clue in one of them.")

############
#room connection
castle main room.north = kitchen
castle main room.south = NPC
castle main room.east = bedroom2
castle main room.west = bedroom1
kitchen.east = dead bodies room search for key
kitchen.west = hidden key to main door
kitchen.south = castle main room
hidden key to main door.east = kitchen
NPC.north = castle main room
NPC.south = hallway
hallway.south = leaving castle door
leaving castle door.north = hallway
basement.north = bedroom2
bedroom2.south = basement
bedroom2.north = dead bodies room search for key
bedroom1.north = hidden key to main door
bedroom1.south = ghosts room
ghosts room.north = bedroom1
hallway.north = NPC
dead bodies room.west = kitchen

#binds
@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#cheks if the cureent room list of exits has
		#the direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"you ho {direction}")
		print(current_room)
	else:
		print("you can't go that way")