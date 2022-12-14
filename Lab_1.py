favorite_number = 5

#Task 2: Generate a Random Number

#Declare a variable called favorite_number and store your favorite or lucky number within it. 
#Use the random module to generate a random number between a range that includes your favorite number.
#Determine how many numbers away the random number was from your favorite number
#Send a screenshot of your completed code to your instructor chat channel.

import random
random_number=random.randrange(0,10)

result=random_number - favorite_number
print(result)

# Task 3: Repeat Code with Loop

# Create a while loop that generates a random number and checks if it matches your favorite number.
# Keep track of how many times the computer has guessed.
# Once the computer guesses the correct number, display a message explaining how many attempts it took the computer to guess your favorite number.
count=1
random_number=random.randrange(0,10)
while random_number != favorite_number:
    random_number=random.randrange(0,10)
    count+=1
print(f"It took the computer {count} times to match the favorite number!")