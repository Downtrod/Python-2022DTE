from adventurelib import *
current_room = space
space = room("""
	You are currently drifting in the cold emptiness of space,
	 a slate-blue spaceship sits in eery silence, it's airlock open and enticing.
	 """)
spaceship = room("""
	The bridge of the spaceship is a greasy white, with a myriad of small, red blinking lights.
	""")

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
@when("go into spaceship")
@when("go into ship")
@when("go into airlock")
def enter_spaceship():

	
def main():
	start()

if __name__ == '__main__':
	main()