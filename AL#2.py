from adventurelib import *


Room.items = Bag()
#Rooms

space = Room("""
	You are currently drifting in the cold emptiness of space,
	 a slate-blue spaceship sits in eery silence, it's airlock open and enticing.
	 """)
spaceship = Room("""
	The bridge of the spaceship is a greasy white, with a myriad of small, red blinking lights.
	\n To the east, you see a hallway, to the south you see some quarters.""")
hallway =  Room("""
	The hallway is long and sleek, gleaming in a bright white sheen, the hallway
	 splits into 3 exits, to the east being a 'bridge', the north being where the ships hold is 
	 (Storage) and the south being the mess hall.
	 """)
quarters = Room("""
	You are currently in the spaceships quarters, but the only thing you see 
	and smell are the burnt corpses of imperial soldiers, nothing but a charred body left, when you look around
	you find, held by a unburnt arm of a man who's entire body was missing, a gun. Pick it up?
	""")
cargo = Room("""
	The cargo room is largely empty, as the ship had been running light, but even so,
	a ship shouldn't have had this little equipment in the cargo hold, it's almost as if
	it all got taken. The Cargo room is roughly the size of a large house, with pieces of iron and machines lying 
	on the floor and a large sealed door seperating the spaceship from the hardships of space.
	""")
bridge = Room("""
	The 'bridge is a part of a spaceship that connects seperate parts of a spaceship, allowing faster travel within the spaceship.
	The bridge is largely transparent with a solid white floor, stained by what seems to be blood, there is nothing else.
	""")
docking = Room("""
	The docking part of the ship is where smaller ships are able to enter, the docking is normally fit
	with large machines and is tightly compact, however currently there are only a few hanging pieces of 
	old machine, most of it burnt by what seems to be a fire, but what fire can melt tungsten?
	""")
escape_pods = Room("""
	This is where the escape pods reside, if you wish, they should be able to take you to the nearest planet, 
	Currently there are three escape pods out of a total of ten, one of them seems to be severely damaged, one of them has a broken window,
	and the last one is perfectly fine, escape pods require a keycard, obtainable by getting it off of an officer in a imperial spaceship.
	""")
mess_hall = Room("""
	The mess hall is a large open area filled with many seats, all of which are turned over or
	in a splintered burnt heap, everywhere you look is a dead corpse, some killed even by large pieces of wood.
	""")

#Bags
mess_hall.items.add(red_keycard)
cargo.items.add(knife)
escape_pods.items.add(adamantium_katana)


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
	print(f"You can go {current_room.exits()}.")
	if len(current_room.items) > 0: #if items are found in room
		print("You also find a.. \n")
		for item in current_room.items:
			print(item) #Prints out each item in the current room

#Item Descriptions / define

Item.description = ""

knife = Item("dirty knife","knife")
knife.description = "the knife has a dull sheen to it, but it looks somewhat useable"

red_keycard =  Item("a red keycard", "keycard", "red card" , "red rank card", "card")
red_keycard.description = "It's a red keycard. It probably opens parts of the spaceship."

adamantium_katana = Item("katana", "sword", "adamantium katana", "weapon" )
adamantium_katana.description = "It's a katana, but made out of adamantium, an almost indestructible metal."

#variables
current_room = space
inventory = Bag()


#Inventory
@when("inventory")
@when("inv")
@when("inven")
@when("show inventory")
@when("show inv")
@when("items")
@when("backpack")
def player_inventory():
	print('You are currently carrying')
	for item in inventory:
		print(item)

@when("pick up ITEM")
@when("take ITEM")
@when("get ITEM")
def pickup(item):
	if item in current_room.items:
		y = current_room.items.take(item)
		inventory.add(y)
		print(f"You picked up {item}")
	else:
		print(f"You don't see anything relating to a {item}")

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