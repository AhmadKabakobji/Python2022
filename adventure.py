#import all the functions from adventurelib
from adventurelib import *

#rooms
Room.item = Bag()

space = Room("you are drifting in space. you see a spaceship")
airlock = Room("you are in an airlock")
cargo = Room("you are in an cargo bay")
docking = Room("you are in the docking bay")
hallway = Room("you are in a hallway with four exits")
bridge = Room("you stand on the bridge of the ship. there is a dead body here")
mess = Room("you are in the kitchen/dining area")
quarters = Room("you are in the crew qurters. There is a locker")
escape = Room("you are in Escape pod")

#room connection
docking.west = cargo
hallway.north = cargo
hallway.east = bridge
hallway.south = mess
hallway.west = airlock
bridge.south = escape
mess.west = quarters
quarters.north = airlock

#items
Item.description = ""
keycard = Item("A red keycard","keycard","card","key","red keycard")
keycard.description = "you look at the keycardand see that it is"

note = Item("A scribbled note","note","paper","code")
note.description = "you look at the note. the number 2,3,5,4 are scribbled"

#additems to room
quarters.items.add(note)

#variables
current_room = space
inventory = bag()
body_searched = False
used_keycard = False


#binds
@when("jump")
def jump():
	print("you jump")

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("you haul yoursel into the airlock")
		current_room = airlock
	else:
		print("there is no airlock here")
print(current_room)

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
@when("look")
def look():
	print(current_room)
	print(f"there are exits, to the {current_room.exits()}")
	if len(current_room.item) > 0:
		print("you also see:")
		for item in current_room.items:
			print(item)
@when("get ITEM")
@when("take ITEM")
def get_item(item):
	#check if item is in room
	#take it out of room
	#put into inventory
	#otherwise tell user there is no ite,
	if item in current_room.item:
		t = current_room.item,take(take)
		inventory.add(t)
		print(f"you pick up the {item}")
	else:
		print(f"you don't see a {item}")




@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)

@when("search body")
@when("look at body")
@when("search man")
def search_body():
	global body_searched
	if current_room == bridge and body_searched == False:
		print("you search the body and a red keycard falls to the floor")
		current_room.item.add(keycard)
		body_searched = True 
	elif current_room == bridge and body_searched == True:
	else:
		print("there is no body here to search")


		@when("use ITEM")
		def use(item):
			if item == keycard and current_room == bridge:
				print("you use the kecard and escape pod slides open")
				print("the escape pod stands open to the south")
				used_keycard = True 
				bridge.south = escape
			else:
				print("you can't use that here")


@when("type code")
def escape_pod_win():
#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE 
#ANYTHING BELOW THIS LINE
def main():
	print(current_room)
	start()
	#staret the main loop


main()