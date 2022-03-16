from adventurelib import *
@when("brush teeth")
@when("brush")
@when("clean teeth")
@when("use toothbrush")
def brush_teeth():
	print("You brush your teeth")

@when("comb hair")
@when("comb")
@when("use hairbrush")
def comb_hair():
	say("""
		You brush your long flowing locks with the
		gold hairbush that you have selected from
		in the red basket
		""")
def main():
	start()

if __name__ == '__main__':
	main()