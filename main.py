import random

health = random.randint(5, 30)
gameOn = True
print ("")
if health <= 19:
    e = "Grunt"
    print(f"A Grunt Appeared: {health} HP")
else:
    e = "Boss"
    print(f"A Boss Appeared: {health} HP")

while health > 0:
    RollDice = input("\nDefeat the enemy by rolling the die.\nRoll The Die by typing 'roll': ")
    if RollDice == "roll":
        Die = random.randint(1, 20)
        health -= Die
        print (f"\nYou rolled {Die}.")
        if health < 0:
            health = 0
        if e == "Grunt":
            print(f"The Grunt has {health} health remaining.")
        else:
            print(f"The Boss has {health} health remaining.")
    else:
        print ("Try Again.")
if e == "Grunt":
    print ("The Grunt was defeated!")
else:
    print ("The Boss was defeated!")
