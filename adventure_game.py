from adventurelib import *

# Different Rooms + Start 
starting_room = Room(

	)

print("""
	You are Adam Hay, an infamous explorer and daredevil, 
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
	small team of cameramen and guides.

	""")

current_room = starting_room
print(current_room)




# Different Directions
starting_room.north =

@when("go DIRECTION")
@when("move DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room=current_room.exit(direction)
		print(f"You can go {direction}")
		print(current_room)

@when("look")









#Items And Bags + Inventory









# Important Variables











#Start of Game








def main():
	start()

if __name=__ == '__main__':
	main()