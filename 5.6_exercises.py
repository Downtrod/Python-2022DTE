#5.6 Excersises - Modifying Variables

#Question 1 - 7
money = 200
hat = 20
top =30
pants =15 
belt =60
shoes =40

print(f"In this shop, you can either buy a hat, top, pants, a belt, and shoes, each of these things costing 20,30,15,60 and 40 dollars respectively.\n")
inshop = input("Would you like to buy anything? y or n")
if inshop == "n":
	print("Nevermind than, get out of my shop.")
elif inshop == "y":
	while inshop == "y":
		buying = input("Good!, now what would you like to buy?")
		if buying == "hat":
			money-hat
			print(f"You've bought a hat! You currently have ${money} left in your bank account.")
		elif buyinh





'''
#This code didnt work for an unknown reason, instead i decided to redo the code
print(f"You have ${money} in your bank account.")

print(f"Buying a hat will cost you ${hat}")
buyinghat = input("If you want to buy a hat, say y or n")
if buyinghat == "y":
	money-=20
	print(f"You have bought the hat, you now have ${money} in your bank account.")
elif buyinghat =="n":
	print(f"You have not bought the hat, you have ${money} in your bank account.")
else:
	print("Either pick y or n (Yes or No)")
	
print('awdad')


print(f"Buying a top will cost you ${top}")
buyingtop = input("If you want to buy a top, say y or n")
if buyingtop == "y":
	money-=30
	print(f"You have bought the top, you now have ${money} in your bank account.")
elif buyingtop =="n":
	print(f"You have not bought the top, you have ${money} in your bank account.")
else:
	print("Either pick y or n (Yes or No)")
	break

print(f"Buying pants will cost you ${pants}")
buyingpants = input("If you want to buy pants, say y or n")
if buyingpants == "y":
	money=money-pants
	print(f"You have bought some pants, you now have ${money} in your bank account.")
elif buyingpants =="n":
	print(f"You have not bought any pants, you have ${money} in your bank account.")
else:
	print("Either pick y or n (Yes or No)")
	break

print(f"Buying a belt will cost you ${belt}")
buyingbelt = input("If you want to buy a belt, say y or n")
if buyingbelt == "y":
	money=money-belt
	print(f"You have bought the belt, you now have ${money} in your bank account.")
elif buyingbelt =="n":
	print(f"You have not bought the belt, you have ${money} in your bank account.")
else:
	print("Either pick y or n (Yes or No)")
	break

print(f"Buying shoes will cost you ${shoes}")
buyingshoes = input("If you want to buy shoes, say y or n")
if buyingshoes == "y":
	money=money-shoes
	print(f"You have bought some shoes, you now have ${money} in your bank account.")
elif buyingshoes =="n":
	print(f"You have not bought any shoes, you have ${money} in your bank account.")
else:
	print("Either pick y or n (Yes or No)")
	break

print(f"You now have ${money} in your bank account.")
'''






	







