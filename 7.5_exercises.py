#Question 1
user_icecream = int(input("How much ice creams do you want? - \n "))
if user_icecream >= 20:
	print("We don't have enough in stock.")
print("")
#Question 2
user_distance = int(input("How far are you going to travel? - \n"))
if user_distance >= 200:
	print("Remember to fill up on petrol before you leave!")
print("")
#Question 3
user_age = int(input("How old are you? - \n"))
if user_age >= 18:
	print("You are considered an adult.")
elif user_age < 18:
	print("You are considered a minor.")
print("")
#Question 4
movie_taste = input("What is your favourite movie? - \n")
if movie_taste.lower() == "lord of the rings":
	print("Excellent taste")
else:
	print("Lord of the Rings is clearly a superior film.")
	print("")
#Question 5
thetaleof = input("Did you ever hear the tragedy of Darth Plagueis the Wise? - \n")
if thetaleof.lower() == "no":
	print("I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
else:
	print("Oh? You must be a fan then?")
print("")
#Question 6
melgib = input("Who directed Passion of the Christ? \n")
if melgib.lower() == "mel gibson":
	print("Correct")
else:
	print("Mel Gibson did.")
print("")
#Question 7
score = 0
while score < 5:
	print("Welcome back to the gameshow! Get more than 5 points to leave!")
	ques1 = int(input("What is 2+123? \n"))
	if ques1 == 125:
		score = score+1
		print("Correct! +1")
		print(f"Your score is {score}")
	else:
		print("Incorrect!")
	ques2 = int(input("What is 10 x 2? \n"))
	if ques2 == 20:
		print("Correct!")
		score= score+1
		print(f"Your score is {score}")
	else:
		print("Incorrect!")
	ques3 = input("What is obama's last name?")
	if ques3.lower() == "barack":
		print('Correct! +1')
		score = score+1
		print(f"Your score is currently {score}")
	else:
		print("Incorrect!")
	ques4 = input("What is another name for aids?")
	if ques4.lower() == "hiv":
		print("Correct!")
		score = score+1
		print(f"Your score is currently {score}")
	elif ques4.lower() == "std":
		print("Sort of correct, +1")
		score=score+1
		print(f"Your score is currently {score}")
	else:
		print("Incorrect!")
	ques5 = int(input("What is 1+1? (Trick Question?)"))
	if ques5 == 2:
		print("Correct! +1")
		score = score+1
		print(f"Your current score is {score}")
	else:
		print("Incorrect!")

print("")










