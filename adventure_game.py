from adventurelib import *
import random
# Title
print("""
	#######################################################################################
	############################### ||-{ Han's Descent }-|| ###############################
	#######################################################################################
	\n \n \n
	""")

################################################
##################### Rooms ####################
################################################




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
	gazing at you with the stony eyes of a predator, Apart from a couple rocks near you,
	there is nothing else.
	""")
open_room = Room("""
	Collapsing after sprinting through the hallway, you find yourself in 
	an open room which seems to be the lunch room of the temple.
	Unfortunately, most of the chairs and items seem to have disintegrated,
	unable to handle the vices of time, yet, there seems to still be some
	items around.

	To your right you see another room, it seems to be a storeroom, you also
	see some shadowed steps going down to your left.
	""")
store_room = Room("""
	As you step into what seems to be a storage room, you remain uncorrected.
	What you see right now seems to be the remnants of a food storage room, with pits of straw
	and remnants of food which have almost been disintegrated, on the floor, you find several blow darts.
	
	""")

tile_traps = Room("""
	Looking around, you see several more torches nearby along with some gray and black tiles in a diagonal format.
	""")
tile_traps_2 = Room("""
	Suddenly, all the torches lit up in a line, allowing you a illuminated warm-looking room. To your right and left you see several stone jaguar heads, with tiles all along the floor
	until the end of the room, where a massive, hideous statue stands. the jaguar heads are quite large, will they be able to take your weight? What about the tile path?
	""")
tile_traps_3 = Room("""
	Stepping off of the tiles, you encounter a sword on what seems to be an altar, as well as a knife
	""")









print("""
	You are Adam Han, an infamous explorer and daredevil, 
	famous for your exploits in the Zhangjiajie Mountain Range in China, and 
	thus recieving a lot of attention of wealthy and powerful people. \n
	Unfortunately, you are poor. \n
	Yes, Adam 'Deathstep' Han, is poor. \n
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
	print(base_descripton)
	if len(current_room.items) > 0: #if items are found in room
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
macuahuitl.description("""from your numerous studies on numerous different ancient civilization's cultures, you have 
	identified this object as a macuahuitl, a wooden bat with several pieces of cut obsidian on it,
	in the days of the spanish conquistadors, this sword was rumoured to be able to cut a horses head off in one blow.""")

aztec_shield = item("shield", "aztec shield", "coloured shield")
aztec_shield.description("""
	this item is a classic Aztec Shield, called a chimalli, usually covered with feathers, although the feathers have long lost all 
	color and have started to fall out, the hard wood underneath revealed, it is still a useable item.

	""")

heavy_gold_decorations = item("gold", "gold_decorations", "decorations")
heavy_gold_decorations.description("")

blowdarts = item("blowdarts", "blow darts", "darts", "blowing darts")
blowdarts.description("")

mayan_blowgun = item("blowgun", "mayan blow gun", "mayan blowgun", "blow gun")
mayan_blowgun.description("The blowgun ")


# Items in Room
secret_room.items.add(aztec_shield)
tomb.items.add(silver_key)
tomb.items.add(turqouise_cloak)
open_room.items.add(heavy_gold_decorations)
open_room.items.add(mayan_blowgun)
store_room.items.add(blowdarts)
large_room.items.add(macuahuitl)

# Important Variables

health = 100
location = startingroom

#Traps

hallway_traps = True



#Interactions in Rooms
####################################
########Starting Room 1 - 2########
###################################




@when("take torch")
@when("get torch")
@when("lift torch")
@when("pick up torch")
def torch_pickup():
	global current_room
	if current_room is not starting_room1:
		print("wha")
	elif pine_torch_check == False:
		print("You've already got a pine torch retard.")
	else:
		inventory.add(pine_torch)
		print("""
			You pick up the torch and find that it still seems useable after all this time
			Do you want to set it alight?
			""")



#####################################
##########Trapdoor Function##########
#####################################


@when("go to wooden area")
@when("examine wooden area")
@when("check out wooden area")
@when("look for trapdoor")
@when("look at wooden area")
@when("investigate wooden area")
def investigate_trapdoor():
	global current_room
	global location
	if current_room is not starting_room2:
		say("That's like 20 chapters back? Alzheimers?")
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
		print("How the hell can you break it if you're not even near it?")
	else:
		current_room = wooden_trapdoor


#####################################
######### Hallway Functions #########
####################################

@when("go into hallway")
@when("go into room")
@when("walk into hallway")
@when("walk into next room")
@when("walk into room")
@when("go into next room")
def enter_hallway():
	if current_room is not starting_room2:
		say("I don't understand")

	else:
		global current_room
		current_room = long_hallway


@when("pick up rocks")
@when("throw rock")
@when("chuck rock")
@when("chuck rock into hallway")
@when("throw rock into hallway")
def hallway_trap():
	global hallway_traps
	if rock in inventory and current_room == long_hallway:
		y - inventory.remove(rock)
		print("""
			You throw the rock into the hallway, the rock bounces once on the floor once,
			suddenly numerous arrows come into your vision as the rock gets slammed into,
			flinging it futher into the hallway

			""")
		hallway_traps = False
	else:
		print("You don't have any rocks in your inventory right now.")




# Going Thru Hallway + 1st Death
@when("go through long hallway")
@when("go through hallway")
@when("walk through long hallway")
@when("walk through hallway")
@when("run through long hallway")
@when("run through hallway")
@when("carry on walking")
def hallway_death():
	global current_room
	if current_room == long_hallway and hallway_traps == True:
		print("""
			You go through the hallway and immediately get shot to oblviion
			by dozens of arrows, your mutilated corpse falls to the ground with
			a resounding, soppy slap.

			What sort of idiot runs straight into a long hallway obviously filled with traps?
			""")
		current_room = starting_room1
		pine_torch_check = True
		hallway_traps = True
		inventory.remove(pine_torch)
		inventory.remove(rock)
		inventory.remove(aztec_shield)

	elif current_room == long_hallway and hallway_traps == False: #Checks if you have deactivated Trap
		print("""You carry on through the hallway, thankfully, no more traps activate.

			""")
		current_room = open_room
		print(current_room)

	else:
		print("I don't understand, stupid.")

@when("run through hallway using shield")
@when("go through long hallway using shield")
@when("walk through long hallway using shield")
@when("walk through hallway using shield")
@when("run through long hallway using shield")
@when("run through hallway using shield")
@when("carry on walking using shield")
@when("use shield through hallway")
@when("use shield through long hallway")
@when("use shield while going through long hallway")
def arrows_shield():
	global current_room
	global health
	global hallway_traps
	arrows_luck = random.randint(1,2)
	if aztec_shield is in inventory and current_room == starting_room2 and arrows_luck == 1:

	elif aztec_shield is in inventory and current_room == starting_room2 and arrows_luck == 2:
		print("""Hefting your shield up, you sprint through the hallway, your heavy boots striking the booby-trapped floor, shielding your body from the sides of the hallway,
			you feel several arrows striking your shield. Stumbling, you collapse at the end of the hallway. Your feeling of relief is quickly replaced with a wave of pain as the arrow in your side
			aches. Trembling, you break it off and continue on.""")
		current_room = open_room
		hallway_traps = False
		health -= 25
		damaged_shield = True

#Alternative Shield Ending (Traps are Deactivated)
@when("run through hallway using shield")
@when("go through long hallway using shield")
@when("walk through long hallway using shield")
@when("walk through hallway using shield")
@when("run through long hallway using shield")
@when("run through hallway using shield")
@when("carry on walking using shield")
@when("use shield through hallway")
@when("use shield through long hallway")
@when("use shield while going through long hallway")
def noarrows_shield():
	global current_room
	global health
	if aztec_shield is in inventory and current_room == starting_room2 and hallway_traps == False:
		print("""You sprint through the hallway using your shield to block any incoming arrows. Collapsing at the end of the hallway, you stub your toe
			and realise there was no more arrows, you did that for nothing.""")
		health -= 1
		current_room = open_room






# Entering Another Room From The "Open Room"
@when("go down stairs")
@when("go down shadowed stairs")
@when("go down stair")
@when("go down shadowed stair")
@when("go to stairs")
@when("go to stair")
@when("go to shadowed stairs")
@when("go to shadowed stair")
def stairs_down():
	global current_room
	if current_room == open_room: 
		print("""Steeling yourself, you go down the cold steps, the darkness around slowly being
			pushed away by your torchlight, it receeded, revealing a huge room.""")
		current_room = tile_traps


# Tiled Room Which is Lit Up
@when("light up torches")
@when("light the torches")
@when("set fire to the torches")
def tiles_room():
	global current_room
	if current_room == tile_traps:
		print("")

#Tiled Room - Easy way out.
@when("walk on")
@when("carry on walking")
@when("go through tiled area")
@when("carry on through tiled area")
@when("move through tiled area")
@when("carry on through tiled area")
@when("walk on tiles")
@when("walk on tiled area")
@when("carry on throguh tiles")
@when("walk through tiles")
@when("run ontop of tiles")
@when("run through tiled area")
@when("walk on a tile")
@when("step on a tile.")
@when("run ontop of tiles")
@when("walk ontop of tiles")
@when("step ontop of tile")
@when("step ontop of a tile")
@when("step ontop of some tiles")
@when("step on several tiles")
@when("step on some tiles")
@when("run on some tiles")
@when("walk on a tile.")
@when("step ontop of tiled area")
@when("step on the tiled area")
def tiled_trap():
	global current_room



# Exiting Trap Door Area
@when("")

#Start of Game








def main():
	start()

if __name=__ == '__main__':
	main()