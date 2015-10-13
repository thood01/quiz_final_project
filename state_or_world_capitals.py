print "How well do you know the famous capitals from around the world?\n"
print "With this game, you can either test your knowledge of US state capitals or capitals of world countries. Have fun!"

import random

print "\nNOTE: Do not use abbreviations. Letter case doesn't matter in your responses, but a misspelled city will be counted as incorrect.\n"
option = raw_input("Which do you want to play? Enter 1 for state capitals and 2 for world capitals.\n")

if option == "1":
	import random

	state_capitals_d = {}

	with open("state_capitals.csv") as f:
		capitals_list = f.readlines()[0].split("\r")
		for line in capitals_list:
			(key, val) = line.split(",")
			state_capitals_d[key] = val

	count = 0
	right = 0
	wrong = 0
	incorrect_answers=[]

	while len(state_capitals_d)>0 and count<20:
		choice=random.choice(state_capitals_d.keys())
		correct_answer=state_capitals_d.get(choice)

		print "What is the capital city of",choice+"?\n"
		answer=raw_input("# ")
		if answer.lower()==correct_answer.lower():
			right += 1
			count += 1
			print "Correct!\n"
			del state_capitals_d[choice]
			#Want to give a point if they spell it wrong but tell them the right way to spell it
		else:
			wrong += 1
			count +=1
			incorrect_answers.append(choice)
			print "\nClose, but no cigar."
			print "The correct answer is",correct_answer+"."
			del state_capitals_d[choice]

	number_correct = float(right)
	number_incorrect = float(wrong)
	total = number_correct+number_incorrect
	percent_correct = (number_correct/total)*100
	
	if percent_correct == 100:
		print "WOW! You got them all right!\nAmazing!"
	elif percent_correct >=90:
		print "\nYou only missed",wrong,"states. That's",percent_correct,"percent.\nSomebody paid attention in school! Maybe next time you'll get them all correct!"
	elif percent_correct > 60 and percent_correct<80:
		print "\nYou only missed",wrong,"states.\nNot bad. Not bad! Keep practicing!"
	else:
		print "\nYou missed",wrong,"states.\nThat's only",percent_correct,"percent correct. Maybe you should study a little before you try this again. Better luck next time!"	
	
elif option == "2":
	import random
	world_capitals_d = {}
	with open("world_capitals.csv") as f:
		capitals_list = f.readlines()[0].split("\r")
		for line in capitals_list:
			(key, val) = line.split(",")
			world_capitals_d[key] = val
	count = 0
	right = 0
	wrong = 0	
	incorrect_answers=[]
	
	while len(world_capitals_d)>0 and count<20:
		choice=random.choice(world_capitals_d.keys())
		correct_answer=world_capitals_d.get(choice)

		print "What is the capital city of",choice+"?\n"
		answer=raw_input("# ")
		if answer.lower()==correct_answer.lower():
			right += 1
			count += 1
			print "Correct!\n"
			del world_capitals_d[choice]
			
		else:			
			wrong += 1
			count +=1
			incorrect_answers.append(choice)
			print "\nSorry. That's incorrect."
			print "The correct answer is",correct_answer+"."
			del world_capitals_d[choice]

	number_correct = float(right)
	number_incorrect = float(wrong)
	total = number_correct+number_incorrect
	percent_correct = (number_correct/total)*100
	
	if percent_correct == 100:
		print "That's quite a feat!! You got them all right!"
	elif percent_correct >=90:
		print "\nYou only missed",wrong,"capitals. That's",percent_correct,".\nSomebody paid attention in school! Maybe next time you'll get them all correct!"
	elif percent_correct > 60 and percent_correct<80:
		print "\nYou only missed",wrong,"capitals.\nNot bad. Not bad! Keep practicing!"
	else:
		print "\nYou missed",wrong,"capitals.\nThat's only",percent_correct,"percent correct. Maybe you should study a little before you try this again. Better luck next time!"

print "Here are the ones you got wrong:\n"
for i in incorrect_answers:
	print i