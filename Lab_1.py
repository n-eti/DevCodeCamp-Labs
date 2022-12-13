favorite_number = 5

#Declare a variable called favorite_number and store your favorite or lucky number within it. 
#Use the random module to generate a random number between a range that includes your favorite number.
#Determine how many numbers away the random number was from your favorite number
#Send a screenshot of your completed code to your instructor chat channel.

import random
random_number=random.randrange(0,10)

result=random_number - favorite_number
print(result)
