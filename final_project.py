#Tiffany Price
#Code overview: This is an application to allow users to answer trivia questions about US state and world capitals.
#All rights reserved.

#TO DO
# combine state and world capitals
# give option to enter 'quit' to stop playing game but still output number right and wrong
# show percentage correct of number did

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

right = 0
wrong = 0
def main():
	incorrect_answers=[]
while len(state_capitals_d)>0:
	choice=random.choice(state_capitals_d.keys())
	correct_answer=state_capitals_d.get(choice)
	
	print "What is the capital city of",choice+"?"
	answer=raw_input("# ")
	if answer.lower()==correct_answer.lower():
		right += 1
		print "Correct!\n"
		del state_capitals_d[choice]
	else:
		wrong += 1
		# incorrect_answers.append(choice)
		print "Close, but no cigar."
		print "The correct answer is",correct_answer+"."
		del state_capitals_d[choice]
	percent_right = float(right/wrong)*100
if percent_right <=80:
	print "You missed",wrong,"states.\nThat's only",percent_right,"percent correct. Better luck next time."
elif percent_wrong<=90:
	print "You missed",wrong,"states.\nThat's pretty good!"
else:
	print "You only missed",wrong,"states.\nAmazing!"
	# print "You missed",len(incorrect_answers),"states.\n"

# if incorrect_answers:
# 	print "Here are the ones that you missed:\n"
# 	for each in incorrect_answers:
# 		print each
# 	else:
		# print "Perfect!"

        
# response=""
# while response<>"n":
#     main()
#     response=raw_input("\n\nPlay again?(y/n)\n# ")


#dictionary.items will give list of items so I can provide the 'value' and ask for the 'key'.