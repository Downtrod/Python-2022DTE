#6.3 Excersises

#Question 1
input("Type any key and press enter - \n")
print("")
#Question 2
input("Type your name and press enter - \n")
print("")
#Question 3
int(input("Type your age and press enter - \n"))
print("")
#Question 4
username = input("What is your name? (Press enter after typing?)")
print("")
#Question 5
userage= int(input("What is your age? - \n"))
print("")
#Question 6
favourite_movie= input("What is your favourite movie - \n")
print("")
#Question 7
favourite_book = input("What is your favourite book? - \n")
print("")
#Question 8
adjective = input("Type in an adjective. \n")
print("")
#Question 9
noun = input("Type in a noun. \n")
print("")
#Question 10
verb = input("Type a verb. \n")
print("")
#Question 11
print(f"The user's favourite book is {favourite_book}")
print(f"The user favourite movie is {favourite_movie}")
print(f"The user is {userage} years old.")
print(f"The user name is {username}")
print(f"The giant did indeed {verb}")
print(f"The cheescake was, in fact {adjective}")
print(f"Frankly, i hate {favourite_book}")
print(f"Even twilight was better than {favourite_movie}")
#Question 12
userage = int(input("How old are you? - \n"))
print("")
#Question 13

print(f"The age you will be in ten years is {userage+10}")
print("")
#Question 14
print(f"The user was born roughly {2022-userage}")
print("")
#Question 15
userapple = int(input("How much apples do you have? - \n"))
print("")
#Question 16
userfriends=int(input("How much friends do you have? - \n"))
print("")
#Question 17
sharedapples = (int(userapple/userfriends))
leftover = (userapple%userfriends)
print(f"If the apples are shared equally among the friends, they will have {sharedapples} apples each.")
print(f"The user will have {leftover} apples left over")
print("")
#Question 18
pizzas = int(input("How many pizzas do you want?\n"))
print("")
#Question 19
people = int(input("How many people are you feeding? - \n"))
print("")
#Question 20
pizzaslices = (pizzas*8)
sharedpizzaslices = (int(pizzaslices/people))
leftoverpizzas = (pizzaslices%people)
print(f"If the pizzas are shared equally among the people, they will have {sharedpizzaslices} pizza slices each.")
print(f"The user will have {leftoverpizzas} pizza slices left.")
print("")
#Question 21
userdollars = float(input("How much money do you have in your bank account? \n"))
print("")
#Question 22
tvcosts = float(input("How much does a tv which you can afford cost?\n"))
print("")
#Question 23
print(f"The user will have ${userdollars-tvcosts} left over if they buy the tv.")
print("")
#Question 24
print(f"If the tv has a 20% discount the user will have ${userdollars-tvcosts*0.8} left over.")
print("")
#Question 25
ethereum = float(input("How much Ethereum do you have?"))
print("")
#Question 26
ethereumvalue = 4136.89
print("")
#Question 27
dollarvalue_bitcoin = int(ethereum*ethereumvalue)
print(f"You current worth in Ethereum is ${dollarvalue_bitcoin}")
print("")
#Question 28
incomeweek = float(input("How much money do you earn in a week? \n"))
print("")
#Question 29
taxrate = float(input("What is the tax rate?"))
decimaltax = float(taxrate/100)
print("")
#Question 30
print(f"The user will take home ${incomeweek* (1-decimaltax)}")
print("")
#Question 31
namebook = input("Give me the name of a book. \n")
print("")
#Question 32
x = namebook.lower()
y = namebook.upper()
z = namebook.title()
print(f"{x} {y} {z}")
#Question 33
randomnumber= int(input("Give me a number"))
print("")
#Question 34
print(namebook*randomnumber)
print("")

































