from adventurelib import *
#Roonms
space = Room("""
	You are currently drifting in the cold emptiness of space,
	 a slate-blue spaceship sits in eery silence, it's airlock open and enticing.
	 """)
spaceship = Room("""
	The bridge of the spaceship is a greasy white, with a myriad of small, red blinking lights.
	""")
hallway = 

#Directions
spaceship.east = hallway
spaceship.south= quarters
hallway.east = bridge
hallway.north = cargo
cargo.east = docking
bridge.south = escape_pods
quarters.east = mess_hall
hallway.south = mess_hall



@when("go DIRECTION")
@when("move DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room=current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)

@when("look")
@when("look around")
def look():
	global current_room
	print(current_room)
	print(f"You can go {current_room.exit()}.")

#Item Descriptions / define

Item.description = ""

knife = Item("dirty knife","knife")
knife.description = "the knife has a dull sheen to it, but it looks somewhat useable"

red_keycard =  Item("a red keycard", "keycard", "red card" , "red rank card", "card"
red_keycard.description = "It's a red keycard. It probably opens parts of the spaceship."

adamantium_katana = Item("katana", "sword", "adamantium katana", "weapon" )
adamantium_katana.description = "It's a katana, but made out of adamntium, an almost indescructible metal."

#variables
current_room = space
inventory = Bag()

#Enter Spaceship (Room 1)

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
@when("go into spaceship")
@when("go into ship")
@when("go into airlock")
def enter_spaceship():
	global current_room
	if current_room is not space:
		say("There is no airlock here.")
	
	else:
		current_room = spaceship
		print("""You heave yourself into the spaceship and slam
	 	your fist on the button to close the airlock.
	 	""")
		print(current_room)









def main():
	start()

if __name__ == '__main__':
	main()