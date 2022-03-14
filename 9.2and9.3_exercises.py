#9.2
#Question 1
order_complete = "False"
toppings_available = ["vanilla","strawberry","chocolate","sprinkles","nuts","raisins","flake","m&ms"]
x = toppings_available.join("\n")
topping_count = 0
while order_complete == "False":
	choice = input("What sort of toppings do you want? pick from - \n" + x)
	if choice.lower() == toppings_available:
		print(f"We've added {choice}")
		topping_count=topping_count+1

	if topping_count == 6:
		order_complete == "True"






























