print "How well do you know the famous capitals from around the world?"
print "With this game, you can either test your knowledge of US state capitals, capitals of world countries, or both US state capitals AND world country capitals."
#game_option = raw_input("To test your knowledge of US state capitals, please type A. For world country capitals, please type B. For both, please type C.")

import random

all_capitals_d = {}
with open("world_capitals.csv") and open("state_capitals.csv") as f:
	capitals_list = f.readlines()[0].split("\r")
	for line in capitals_list:
		(key, val) = line.split(",")
		all_capitals_d[key] = val
count = 0
right = 0
wrong = 0
def main(): #what does this mean?
	incorrect_answers=[]
while len(all_capitals_d)>0 and count<10:
	choice=random.choice(all_capitals_d.keys())
	correct_answer=all_capitals_d.get(choice)

	print "What is the capital city of",choice+"?"
	answer=raw_input("# ")
	if answer.lower()==correct_answer.lower():
		right += 1
		count += 1
		print "Correct!\n"
		del all_capitals_d[choice]
		#Want to give a point if they spell it wrong but tell them the right way to spell it
	else:
		# incorrect_answers = [] #NOT WORKING
		wrong += 1
		count +=1
		# incorrect_answers.append(choice)
		print "Close, but no cigar."
		print "The correct answer is",correct_answer+"."
		del all_capitals_d[choice]

number_correct = float(right)
number_incorrect = float(wrong)
total = number_correct+number_incorrect
percent_correct = (number_correct/total)*100

if percent_correct <=50:
	print "You missed",wrong,"capitals.\nThat's only",percent_correct,"percent correct. Maybe you should study a little before you try this again. Better luck next time!"	
elif percent_correct > 50 or percent_correct<80:
	print "You only missed",wrong,"capitals.\nNot bad. Not bad! Keep practicing!"
elif percent_correct > 80 or percent_correct<100:
	print "\nYou only missed",wrong,"capitals.\nSomebody paid attention in school! Maybe next time you'll get them all correct!"
else:
	print "You got them all right!\nAmazing!"