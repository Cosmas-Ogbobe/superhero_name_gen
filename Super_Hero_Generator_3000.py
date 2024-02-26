import random
import time
brains = 0
braun = 0
stamina = 0
wisdom = 0
power = 0
constitution = 0
dexterity = 0
speed = 0
answer = ' '
superPowers =['Flying', 'Super Strength', 'Telepathy', 'Super Speed', 'Can Eat a Lot of Hot Dogs', 'Good At Skipping Rope']
superFirstName = ['Wonder','Whatta','Rabid','Incredible', 'Astonishing', 'Decent', 'Stupendous', 'Above-average', 'That Guy', 'Improbably']
superLastName = ['Boy', 'Man', 'Dingo', 'Beefcake', 'Girl', 'Woman', 'Guy','Hero', 'Max', 'Dream', 'Macho Man','Stallion']
print("Are you ready to create a super hero with the Super Hero Generator 3000?")
print("Enter Y/N:")
answer = input()
answer = answer.upper()
while answer != "Y":
    print("I'm sorry, but you have to choose Y to continue!")
    print("Choose Y/N:")
    answer = input()
    answer = answer.upper()
    print("Great, let's get started!")

print("Randomizing name...")
# Creating suspense using the time() function
for i in range(3):
    print("...........")
    time.sleep(3)
print("(I bet you can't stand the suspense!)")
print("")
# Randomizing Super Hero Name
# We do this by choosing one name from each of our two name lists
# And adding it to the variable superName
superName = random.choice(superFirstName)+ " " +random.choice(superLastName)
print("Your Super Hero Name is:")
print(superName)

print("")
print("Now it's time to see what super power you have!)")
print("(generating super hero power...)")
# Creating dramatic effect again
for i in range(2):
    print("...........")
    time.sleep(3)
print("(nah...you wouldn't like THAT one...)")
for i in range(2):
    print("...........")
    time.sleep(3)
print("(almost there....)")
# Randomly choosing a super power from the superPowers list
# and assigning it to the variable power
power = random.choice(superPowers)
# Printing out the variable power and some text
print("Your new power is:")
print(power)
print("")
power = random.choice(superPowers)

print("Last but not least, let's generate your stats!")
print("Will you be super smart? Super strong? Super Good Looking?")
print("Time to find out!")
# Creating dramatic effect and slowing the program down again
for i in range(3):
    print("...........")
time.sleep(3)
# Randomly filling each of the below variables with a new value
# The new values will range from 1-20
brains = random.randint(1,20)
braun = random.randint(1,20)
stamina = random.randint(1,20)
wisdom = random.randint(1,20)
constitution = random.randint(1,20)
dexterity = random.randint(1,20)
speed = random.randint(1,20)
# Printing out the statistics
print("Your new stats are:")
print("")
print("Brains: ", brains)
print("Braun: ", braun)
print("Stamina: ", stamina)
print("Wisdom: ", wisdom)
print("Constitution: ", constitution)
print("Dexterity: ", dexterity)
print("Speed: ", speed)
print("")
# Printing out a full summary of the generated super hero
# This includes the hero's name, super power, and stats
print("Here is a summary of your new Super Hero!")
print("Thanks for using the Super Hero Generator 3000!")
print("Tell all your friends!")
print("")
print("Character Summary:")
print("")
print("")
print("Super Hero Name: ", superName)
print("Super Power: ", power)
print("")
print("Brains: ", brains)
print("Braun: ", braun)
print("Stamina: ", stamina)
print("Wisdom: ", wisdom)
print("Constitution: ", constitution)
print("Dexterity: ", dexterity)
print("Speed: ", speed)
