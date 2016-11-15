import sys
import random

# Open up our email list and convert it into a 2-dimensional array
# Note that any email past the first is an email that cannot be matched as a secret Santa
# For optimal usage, place all emails with email restrictions at the top of the list
with open('emailList.txt', 'r') as input:
	emailArray = []
	emailArray.append([])
	arrayPosition = 0
	for line in input:
		if line == '*\n':
			arrayPosition += 1
			emailArray.append([])
		else:
			emailArray[arrayPosition].append(line)
# We create a list of emails to use from our emailArray
prioritizedNames = []
for email in emailArray:
	prioritizedNames.append(email[0])
# Create a copy of this list to remove emails from and a blank list to insert pairings to
remainingNames = prioritizedNames[:]
matchingList = []
# Use a while loop to match everyone
arrayPosition = 0
while (len(remainingNames) > 0):
	randomChoice = random.choice(remainingNames)
	# Make sure the selected match is not in the list of email restrictions
	while (randomChoice in emailArray[arrayPosition]):
		randomChoice = random.choice(remainingNames)
		#print (randomChoice)
	matchingList.append(randomChoice)
	remainingNames.remove(randomChoice)
	arrayPosition += 1
# Print out the list of successful pairs
for email in prioritizedNames:
	print ("Secret Santa " + email + " gives a gift to " + matchingList[prioritizedNames.index(email)])