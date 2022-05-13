from adventurelib import *
import random
Room.items = Bag()
inventory = Bag()
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
current_room = starting_room1
starting_room2 = Room("""
Lighting up the room with the torch, the room transforms. Everywhere you look
there are intricate carvings, telling tales of great heroism and oppression,
freedom and imprisonment. Along with the revelation of teh carvings, you notice
a wooden area in the stone room, along with another room, allowing you to see a few metres into the room..
It seems to be a hallway?
""")

secret_room = Room("""
	breaking the wooden trapdoor, you jump down into the storeroom, there is little 
	to see in this room apart from some rotten furniture, however, in the corner of 
	the room there is an Aztec shield, although it is a bit run down, it is still
	tough.
	""")
long_hallway= Room("""
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
There is no more traps here, only the ugly statue and the resting place of the sword
""")
fire_room = Room("""
Emerging from the stairs, you find yourself in another room full of traps, this time, you feel it before you see it.
The scorching heat of the flames sear your skin.
Through some unknown method, flames have been burning here for centuries, and are stil extremely hot.
Based on your observations, you have deduced that the flames come from four holes, two in the ceiling and two on the floor.
Each one of these halls are small yet they shoot out a large amount of heat.
""")
keyroom = Room("""
The room which you have arrived in is small and compact, made out of a black - like material, in front of you is the outline of what seems to be the Macuahuitl you got before.
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

(Top Gear Top Tip - Use your Inventory)
""")

current_room = starting_room1
print(current_room)




# Different Directions + Room Exploration



@when("look")
@when("look around")
@when("search")
@when("search around")
def look():
	global current_room
	print(current_room)
	if len(current_room.items) > 0: #if items are found in room
		print("You also find a...")
		for item in current_room.items:
			print(item) # Prints out the items in the current room
			print("Pick up?")


#Items And Bags + Inventory

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		y - inventory.find(item)
		print(y.description)
	else:
		print(f"You aren't carrying an {item}")


#Function for Picking up Items
@when("pick up ITEM")
@when("take ITEM")
@when("get ITEM")
@when("go get ITEM")
@when("pick up the ITEM")
def pickup(item):
	if item in current_room.items:
		y=current_room.items.take(item)
		inventory.add(y)
		print(f"You picked up {item}")
	elif item == "pine torch" or "torch" and current_room == starting_room1:
		print("""
			You pick up the torch and find that it still seems useable after all this time
		Do you want to set it alight?
		""")
	else:
		print(f"You don't see anytthing relating to a {item}")

#function for a player inventory
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
#This gives a description of the items.
Item.description = ""

machete = Item("machete", "sword", "old machete")
machete.description = "your trusty machete which has accompanied you on many adventures, used mainly for cutting foliage."

macuahuitl = Item("macuahuitl", "sword", "obsidian sword", "wooden sword", "obsidian bat", "wooden bat" , "wooden bat with obsidian shards", "obsidian wooden bat")
macuahuitl.description = "from your many studies on numerous different ancient civilization's cultures, you have identified this object as a macuahuitl, a wooden bat with several pieces of cut obsidian on it, in the days of the spanish conquistadors, this sword was rumoured to be able to cut a horses head off in one blow."

aztec_shield = Item("shield", "aztec shield", "coloured shield")
aztec_shield.description = "this item is a classic Aztec Shield, called a chimalli, usually covered with feathers, although the feathers have long lost all color and have started to fall out, the hard wood underneath revealed, it is still a useable item."

heavy_gold_decorations = Item("gold", "gold_decorations", "decorations")
heavy_gold_decorations.description = "Some gold decorations, may be useful later on"

blowdarts = Item("blowdarts", "blow darts", "darts", "blowing darts")
blowdarts.description = "Blowdarts"

mayan_blowgun = Item("blowgun", "mayan blow gun", "mayan blowgun", "blow gun")
mayan_blowgun.description = "Old mayan Blowgun, may be useful later."


# Items in Room
starting_room1.items.add(machete)
secret_room.items.add(aztec_shield)
open_room.items.add(heavy_gold_decorations)
open_room.items.add(mayan_blowgun)
store_room.items.add(blowdarts)
tile_traps_3.items.add(macuahuitl)

# Important Variables used

health = 100
location = starting_room1
fire_trap = 0

#Trap Deactivation variables

hallway_traps = True



#I use this here so that the items will be defined by the previous code, or else it will have an error


#Interactions in Rooms
####################################
########Starting Room 1 - 2########
###################################

@when("light pine torch")
@when("set pine torch alight")
@when("light torch")
@when("set torch alight")
@when("put torch on fire")
@when("make the torch on fire")
def pine_torch_light():
	global current_room
	if current_room == starting_room1:
		print("""
			With the torch now lit, you are able to see mroe of the 
			nearby area for a few metres, nearby, there seems to be a wooden area
			on the ground, and directly in front of you is an ominous long
			hallway.
			""")
		current_room = starting_room2






#####################################
##########Trapdoor Function##########
#####################################

#gives more details on the trapdoor
@when("go to wooden area")
@when("examine wooden area")
@when("check out wooden area")
@when("look for trapdoor")
@when("look at wooden area")
@when("investigate wooden area")
def investigate_trapdoor():
	global current_room
	global location
	if current_room == starting_room2:
		print("""You examine the wooden area and find out it is what seems to be a trap
		door, it seems to be quite rotten.
		""")
	else:
		print("wah?")
#entering trap door
@when("break trapdoor")
@when("enter trapdoor")
@when("kick trapdoor")
@when("kick wooden area")
@when("break wooden area")
def break_trap():
	global current_room
	if current_room is not starting_room2:
		print("How the hell can you break it if you're not even near it?")
	else:
		current_room = secret_room
		print(current_room)


#####################################
######### Hallway Functions #########
####################################

@when("go into hallway")
@when("go into room")
@when("walk into hallway")
@when("walk into next room")
@when("walk into room")
@when("go into next room")
@when("go into long hallway")
@when("go through long hallway")
def enter_hallway():
	global current_room
	if current_room is not starting_room2:
		say("I don't understand")
	else:
		current_room = long_hallway
		print(current_room)


@when("pick up the rocks")
@when("throw rock")
@when("chuck rock")
@when("chuck rock into hallway")
@when("throw rock into hallway")
@when("throw rocks")
@when("chuck rocks")
@when("throw rocks into hallway")
@when("chuck rocks into hallway")
def hallway_trap():
	global hallway_traps
	if current_room == long_hallway:
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
@when("carry on")
def hallway_death():
	global current_room
	global hallway_traps
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
		inventory.remove(aztec_shield)

	elif current_room == long_hallway and hallway_traps == False: #Checks if you have deactivated Trap
		print("""You carry on through the hallway, thankfully, no more traps activate.
		""")
		current_room = open_room
		print(current_room)



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
	arrows_luck == random.randint(1,2)
	if aztec_shield in inventory and current_room == starting_room2 and arrows_luck == 1:
		print("Hefting your shield, you run through the hallway, suddenly a hail of arrows slam into your side, you faced the wrong way.")
		health - 100
	elif aztec_shield in inventory and current_room == starting_room2 and arrows_luck == 2:
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
	if aztec_shield in inventory and current_room == starting_room2 and hallway_traps == False:
		print("""You sprint through the hallway using your shield to block any incoming arrows. Collapsing at the end of the hallway, you stub your toe
		and realise there was no more arrows, you did that for nothing.""")
		health -= 1
		current_room = open_room



@when("go into storeroom")
@when("enter storeroom")
@when("go into store room")
@when("enter store room")
@when("go into the storeroom")
@when("enter the storeroom")
@when("go into the store room")
@when("enter the store room")
def store_room_entry():
	global current_room
	if current_room == open_room:
		print("you go into the store room")
		current_room = store_room
		print(current_room)




@when("go to to open room")
@when("leave store room")
@when("leave storeroom")
@when("go back to the open room")
@when("go back to the openroom")
@when("go to the openroom")
@when("go back")
def exit_storoom():
	global current_room
	if current_room == store_room:
		current_room = open_room
		print("You duck back into the open room, the only place still unknown is the shadowed stairs.")


# Entering Another Room From The "Open Room"
@when("go down stairs")
@when("go down shadowed stairs")
@when("go down stair")
@when("go down shadowed stair")
@when("go to stairs")
@when("go to stair")
@when("go to shadowed stairs")
@when("go to shadowed stair")
@when("go down shadowed steps")
@when("go down steps")
@when("go down the steps")
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
@when("put the light on the torches")
@when("use torch")
@when("light torches")
def tiles_room():
	global current_room
	if current_room == tile_traps:
		print("After lighting one of the torches, all of them burst into flame immediately, revealing the full room")
		current_room = tile_traps_2
		print(current_room)

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
@when("step on a tile")
@when("run ontop of tiles")
@when("walk ontop of tiles")
@when("step ontop of tile")
@when("step ontop of a tile")
@when("step ontop of some tiles")
@when("step on several tiles")
@when("step on some tiles")
@when("run on some tiles")
@when("walk on a tile")
@when("step ontop of tiled area")
@when("step on the tiled area")
@when("carry on")
@when("carry on walking")
@when("step on the tiles")
@when("walk on the tiles")
@when("step on tiles")
def tiled_trap():
	global current_room
	if current_room == tile_traps_2:
		print("""
		hefting your shoulders up, you step onto the tiles, thankfully, no traps activate, allowing you to traverse across the room safely and leaving you
		in front of a large statue of an ugly looking deity, this statue is extremely recognisible, looking like an exact copy of one which was found before,
		the statue of Coatlicue, famous for being so ugly that the man who found it instantly buried it again. In front of this statue seems to be some sort of wooden bat.
		""")
		current_room = tile_traps_3
		print("You see some stairs going up next to the statue.")

@when("go up stairs")
@when("go to stairs")
@when("climb up stairs")
@when("go up stairs next to the statue")
@when("continue up the stairs")
@when("go up steps")
@when("go up the step")
def fire_room_entry():
	global current_room
	if current_room == tile_traps_3:
		print("""
		Climbing up the stairs, you emerge into another room.

		""")
		current_room = fire_room
		print(current_room)


# Exiting Trap Door Area
@when("leave wooden area")
@when("go back out of trap door")
@when("exit trap door area")
@when("exit trap door")
@when("leave trap door")
@when("go out of trap door")
@when("go back")
@when("go out")
def exit_trapdoor():
	global current_room
	if current_room == secret_room:
		current_room = starting_room2
		print("You heave yourself out of the hole and arrive to your intial location, the long hallway is in front of you.")


#firetrap deactivation

@when("use machete and aztec shield")
def aztec_machete_trap():
	global health
	global current_room
	if machete and aztec_shield in inventory:
		print("""You use the machete and the aztec shield to deactivate two of the traps, the aztec shield is used to block the below trap, and
		you use the machete to stab the other one in the cieling, sustaining injuries while doing so.""")
		health - 15
		inventory.remove(aztec_shield)
		inventory.remove(machete)
		current_room == keyroom
		print(current_room)
	else:
		print("you don't have this item")



@when("use machete and macuahuitl")
@when("use machete and sword")
@when("use sword and machete")
@when("use macuahuitl and machete")
def machete_sword_trap():
	global health
	if current_room == fire_room and machete and macuahuitl in inventory:

		print("""
		You use the machete to stab one of the traps, and the macuahuitl to do the same to the others, doing this you sustain a lot of injuries
		from the burns.
		""")
		print("""passing through the narrow gap in the flames, you see a large door, with an outline similar to that of the macuahuitl, looking back,
		you find out it has become a complete puddle.
		congrats, you melted your only way in.""")
		health -100
	else:
		print("you don't have this item")




@when("use aztec shield and sword")
def aztec_sword_trap():
	if macuahuitl and aztec_shield in inventory:
		print("""
		Using the Aztec Shield to block the bottom flame and the Macuahuitl to block the top one, you walk into the next room,
		coming to your senses, you realise this is a keyroom, in front of you is a faint outline similar to that of the macuahuitl, looking back
		you see the sword melted on the bottom of the floor, blocking your exit as well. Congrats, you can now either starve or suffer extreme burning.
		""")
		health - 100
	else:
		print("you don't have this item")

#
@when("use machete")
def machete_trap():
	global current_room
	if current_room == fire_room and machete in inventory:
		print("Using the machete, you block one of the flames.")
		fire_trap += 1
	if fire_trap == 2:
		current_room = keyroom
		print("With two of the fires blocked, you go into the next room.")
		print(current_room)
	else:
		print("you don't have this item")

#Sword Failure
@when("use sword")
def sword_failure():	
	global health
	if current_room == fire_room and macuahuitl in inventory:
		print("""
		Using the macuahuitl, you block one of the holes, using another item, you block the other one, with this small gap
		you are able to go past and into the next room. This room seems to be a keyroom. In front of you, you see the outline of what seems to be the macuahuitl.
		Looking back at the fire trap, you notice the sword completely melted. There goes your way out.
		""")
		health - 10000
	else:
		print("you don't have this item")



#Aztec Shield Route 1
@when("use aztec shield")
def aztec_trap():
	global current_room
	if current_room == fire_room and aztec_shield in inventory:
		print("Using the shield, you block one of the flames.")
		fire_trap += 1
	if fire_trap == 2:
		print("Since two fire traps were blocked, you are able to squeeze through the gap in the fire and make it to the next room.")
		current_room = keyroom
		print(current_room)
	else:
		print("you don't have this item")


#Ending Of Game - Keyroom
@when("use macuahuitl")
@when("use sword in key")
@when("use sword")
@when("use macuahuitl in key")
@when("use sword in outline")
@when("use macuahuitl in outline")
def keyroom():
	if current_room == keyroom:
		print("""
			Placing the Macuahuitl in the keyhole, it slips perfectly into the hole,
		rumbling, the door in front of you opens up revealing.....
		The scene which will be in the next game.
		""")
		restart == input("Restart? Y or N\n")
		if restart.lower() == "y":
			health - 100
		elif restart.lower() == "n":
			print(" k cya")




#Start of Game








def main():
	start()

if __name__ == '__main__':
	main()