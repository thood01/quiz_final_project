#Tiffany Price
#Code overview: This is an application to allow users to answer trivia questions about US state and world capitals.
#All rights reserved.

print "How well do you know the famous capitals from around the world?"
print "With this game, you can either test your knowledge of US state capitals, capitals of world countries, or both US state capitals AND world country capitals."
#game_option = raw_input("To test your knowledge of US state capitals, please type A. For world country capitals, please type B. For both, please type C.")

import random

state_capitals_d = {}
with open("state_capitals.csv") as f:
	capitals_list = f.readlines()[0].split("\r")
	for line in capitals_list:
		(key, val) = line.split(",")
		state_capitals_d[key] = val

def main():
	right = 0
	wrong = 0
	incorrect_answers=[]

while len(state_capitals_d)>0:
	choice=random.choice(state_capitals_d.keys())
	# correct_answer=state_capitals_d.get(choice)

	
	answer=raw_input("What is the capital city of",choice,"?")
	if answer.lower()==correct_answer.lower():
		right += 1
		print "Correct!\n"
		del state_capitals_d[choice]
	else:
		print "Close, but no cigar."
		print "The correct answer is",correct_answer
		incorrect_answers.append(choice)

	print "You missed",len(incorrect_answers),"states.\n"

if incorrect_answers:
	print "Here are the ones that you missed:\n"
	for each in incorrect_answers:
		print each
	else:
		print "Perfect!"

        
# response=""
# while response<>"n":
#     main()
#     response=raw_input("\n\nPlay again?(y/n)\n# ")


#dictionary.items will give list of items so I can provide the 'value' and ask for the 'key'.