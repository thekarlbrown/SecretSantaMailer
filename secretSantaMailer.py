# Secret Santa SMTP Emailer
# By Karl Brown (www.thekarlbrown.com) 11/16/2016

import sys
import random
import smtplib

# Open up our email list and convert it into a 2-dimensional array
# Note that any email past the first is an email that cannot be matched as a secret Santa
# For optimal usage, place all emails with email restrictions at the top of the list
with open('emailList.txt', 'r') as inputFromFile:
	emailArray = []
	emailArray.append([])
	arrayPosition = 0
	for line in inputFromFile:
		if line == '*\n':
			arrayPosition += 1
			emailArray.append([])
		else:
			if "\n" in line:
				line = line[:-1]
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
	
	matchingList.append(randomChoice)
	remainingNames.remove(randomChoice)
	arrayPosition += 1
	
# Print out the list of successful pairs
print("Provide a TLS and SMTP enabled email account, password, server, and port to use to mail. If you are using email, you will need to enable access for less secure apps: https://www.google.com/settings/security/lesssecureapps \n\r")
emailAddressToUse = input("Email Address to Use: ")
emailAddressPassword = input("Email Password to Use: ")
emailServer = input("SMTP/TLS Enabled Server to Use: ")
emailServerPort = input("Email Server TLS Port: ")

# Create the mailer object
mailer = smtplib.SMTP(emailServer, emailServerPort)
mailer.ehlo()
mailer.starttls()
mailer.ehlo()
mailer.login(emailAddressToUse, emailAddressPassword)

# Iterate over the list of emails and actually send the emails
for email in prioritizedNames:
	mailer.sendmail(emailAddressToUse, email, "The individual that you need to give a gift to is " + matchingList[prioritizedNames.index(email)])