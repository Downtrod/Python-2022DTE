from adventurelib import *


print("""
	########################################################################################
	############################### ༒☬༒ ℌ𝔞𝔫'𝔰 𝔇𝔢𝔰𝔠𝔢𝔫𝔱 ༒☬༒ ###############################
	########################################################################################
	\n \n \n
	""")
# Different Rooms + Start 
starting_room1 = Room(""" 
	The room you step into is wide and damp, the absence of light
	preventing the talons of nature taking back the interior of the ruins. Yo your right, 
	still bathed in a small amount of light you see what seems to be a pine torch.
	""")
starting_room2 = Room("""
	Lighting up the room with the torch, the room transforms. Everywhere you look
	there are intricate carvings, telling tales of great heroism and oppression,
	freedom and imprisonment. Along with the revelation of teh carvings, you notice
	a wooden area in the stone room, along with another room, allowing you to see a few metres into the room..
	It seems to be a hallway?
	""")
secret_room = Room(f"""
	After breaking the wooden trapdoor, you jump down into what seems to be a small storeroom,
	there seems to be a couple items around. Will you take {current_room.items()}?	""")

long_hallway= room("""
	As you step into the hallway, your view becomes more clear.
	The hallway is long and narrow, with carvings on both sides of the wall,
	gazing at you with the stony eyes of a predator.
	""")
open_room = Room("""
	Collapsing after sprinting through the hallway, you find yourself in 
	an open room which seems to be the lunch room of the temple.
	Unfortunately, most of the chairs and items seem to have disintegrated,
	unable to handle the vices of time, yet, there seems to still be some
	items around.

	To your right you see another room, it seems to be a storeroom, you also
	see some shadowed steps to your left.



	""")






print("""
	You are Adam Han, an infamous explorer and daredevil, 
	famous for your exploits in the Zhangjiajie Mountain Range in China, and 
	thus recieving a lot of attention of wealthy and powerful people. \n
	Unfortunately, you are poor. \n
	Yes, Adam 'Deathstep' Hay, is poor. \n
	Due to the fact that you acted as if you had money to improve your reputation
	most of the rich and influential people you had been relying on in order to
	maintain wealth had decided that you would not care if they gifted you
	with excessively expensive products, and as a result, you are currently 
	bankrupt, in order to counter this, you have decided one last great
	adventure in order to regain your wealth without losing your reputation,
	as well as a perfect track record for your retirement. \n \n

	Once again, you are met with misfortune. \n
	After thinking that there would be little risk and high reward once breaking
	news reached you first of a newly discovered Mayan Temple, you set off with a 
	small team of cameramen and guides. \n

	Now, with most of your team at the bottom of a ravine, the ruin sits right in fron of you, tall and imposing.
	Most of the ancient carvings are covered up by foliage, yet you can still see the menacing 
	remains of a jaguar statue, seemingly watching you. \n

	Gulping, you enter the Mayan Temple. \n

	""")

current_room = starting_room
print(current_room)




# Different Directions + Room Exploration

@when("go DIRECTION")
@when("move DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room=current_room.exit(direction)
		print(f"You can go {direction}")
		print(current_room)

@when("look")
@when("look around")
@when("search room")
@when("search")
@when("search around")
def look():
	global current_room
	print(current_room)
	if len(current_room.items) > 0 #if items are found in room
	print("You also find a...")
	for item in current_room.items:
		print(item) # Prints out the items in the current room
		print("Pick up?")










#Items And Bags + Inventory

@when("look at ITEM")
@when("ITEM")
def look_at(item):
	if item in inventory:
		y - inventory.find(item)
		print(y.description)
	else:
		print(f"You aren't carrying an {item}")

@when("pick up ITEM")
@when("take ITEM")
@when("get ITEM")
@when("go get ITEM")
def pickup(item):
	if item in current_room.items:
		y=current_room.items.take(item)
		inventory.add(y)
		print(f"You picked up {item}")
	else:
		print(f"You don't see anytthing relating to a {item}")


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


# Different Items

Item.description = ""

machete = item("machete", "sword", "old machete")
machete.description = "your trusty machete which has accompanied you on many adventures, used mainly for cutting foliage."

silver_key = item("silver key", "key", "keys")
silver_key.description("")

turqouise_cloak = item("turqoise cloak", "cloak")
turqouise_cloak.description("")

macuahuitl = ("macuahuitl", "sword", "obsidian sword", "wooden sword")
macuahuitl.description("")

aztec_shield = item("shield", "aztec shield", "coloured shield")
aztec_shield.description("")

heavy_gold_decorations = item("gold", "gold_decorations", "decorations")
heavy_gold_decorations.description("")

blowdarts = item("blowdarts", "blow darts", "darts", "blowing darts")
blowdarts.description("")

mayan_blowgun = item("blowgun", "mayan blow gun", "mayan blowgun", "blow gun")
mayan_blowgun.description("")


# Items in Room
secret_room.items.add(aztec_shield)
tomb.items.add(silver_key)
tomb.items.add(turqouise_cloak)
open_room.items.add(heavy_gold_decorations)
open_room.items.add(mayan_blowgun)
store_room.items.add(blowdarts)
large_room.items.add(macuahuitl)

# Important Variables

location = startingroom







#Interactions in Rooms
@when("take torch")
@when("get torch")
@when("lift torch")
@when("pick up torch")
def torch_pickup():
	global current_room
	if current_room is not 


@when("go to wooden area")
@when("examine wooden area")
@when("check out wooden area")
@when("look for trapdoor")
@when("look at wooden area")
@when("investigate wooden area")
def investigate_trapdoor():
	global current_room
	if current_room is not starting_room2:
		say("There is nothing like that here.")
	else:
		location = wooden_trapdoor
		print("""You examine the wooden area and find out it is what seems to be a trap
			door, it seems to be quite rotten.
			""")

@when("break trapdoor")
@when("enter trapdoor")
@when("kick trapdoor")
@when("kick wooden area")
@when("break wooden area")
def break_trap():
	global current_room
	if location is not wooden_trapdoor:
		print("What do you mean?")
	else:
		current_room = wooden_trapdoor

@when("go into hallway")
@when("go into room")
@when("walk into hallway")
@when("walk into next room")
@when("walk into room")
@when("go into next room")
def enter_hallway():
	if current_room is not starting_room2:
		say("I don't understand")
	elif current_room is x:
		aztec_sh
	else:
		current_room = long_hallway

@when("throw rock")
@when("chuck rock")
@when("chuck rock into hallway")
@when("throw rock into hallway")
def hallway_trap():
	if rock in inventory:
		y - inventory.remove(rock)
		print("""
			You throw the rock into the hallway, the rock bounces once on the floor once,
			suddenly numerous arrows come into your vision as the rock gets slammed into,
			flinging it futher into the hallway
			""")



#Start of Game








def main():
	start()

if __name=__ == '__main__':
	main()