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
def main(): #what does this mean?
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
		#Want to give a point if they spell it wrong but tell them the right way to spell it
	else:
		wrong += 1
		# incorrect_answers.append(choice)
		print "Close, but no cigar."
		print "The correct answer is",correct_answer+"."
		del state_capitals_d[choice]

number_correct = float(right)
number_incorrect = float(wrong)
total = number_correct+number_incorrect
percent_correct = (number_correct/total)*100
# print float(total)
# print float(right/total) #WHY WON'T THIS WORK???!?!?
# percent_right = (right/(right+wrong))*100 #why is my percentage right calc not working?!?!?!
if percent_correct <=50:
	print "You missed",wrong,"states.\nThat's only",percent_correct,"percent correct. Maybe you should study a little before you try this again. Better luck next time!"	
elif percent_correct > 50 or percent_correct<80:
	print "You only missed",wrong,"states.\nNot bad. Not bad! Keep practicing!"
elif percent_correct > 80 or percent_correct<100:
	print "\nYou only missed",wrong,"states.\nSomebody paid attention in school! Maybe next time you'll get them all correct!"
else:
	print "You got them all right!\nAmazing!"
	print "You missed",len(incorrect_answers),"states.\n"

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