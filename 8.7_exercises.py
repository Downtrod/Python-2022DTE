#Question 1
fibonacci = [0,1,1,2,3,4,5,13,21,34]
print(fibonacci)
print("")
#Question 2
favouritefoods = ["Tomato", "Beetroot", "Apples", "Banana", "Coconut"]
print(favouritefoods)
print("")
#Question 3
youtoobers = ["ashanedesilva", "ninja", "dobrebrothers", "fortnite_youtuber69_9", "ricegum"]
print(youtoobers)
print("")
#Question 4
favouritesongs = []
favouritesongs.append("Sabaton-NightWitches")
favouritesongs.append("PoloGBadMan")
favouritesongs.append("EminemWithoutMe")
favouritesongs.append("WeDrinkYourBlood")
favouritesongs.append("RedSunInTheSky")
print(favouritesongs)
print("")

#Question 5
books = []
books.append(input("What are your favourite songs ( five of them)\n"))
books.append(input("\n"))
books.append(input("\n"))
books.append(input("\n"))
books.append(input("\n"))
print(books)
#Question 6
pizza_topping = []
pizza_topping.append(input("What pizza toppings do you want? (Up to 6?\n"))
pizza_topping.append(input())
pizza_topping.append(input())
pizza_topping.append(input())
pizza_topping.append(input())
pizza_topping.append(input())

while "" in pizza_topping:
	pizza_topping.remove("")
print(pizza_topping)
print("")

#Question 7
fruits = ["tomato", "apple", "coconut", "banana", "beetroot"]
playerfruit = input("What type of fruit do you want? If We have it we will give it to you.")
if playerfruit.lower() in fruits:
	print("We have that!")
else:
	print("Unfortunately we do not have that fruit")
	fruits.append(playerfruit)
print(fruits)
print("")

#Question 8
names = ["John", "Dave", "Matt", "Amy", "Poppy", "Ahmed"]
names.sort()
print(names)
names.reverse()
print(names)
print("")

#Question 9
prime_numbers= [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,]
print(prime_numbers)
print(f"The length of the list is")
print(len(prime_numbers))

#Question 10 
common_verbs = ["be", "have", "do", "say", "get", "make", "go"]
print(common_verbs)
print("")









