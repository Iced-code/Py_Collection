import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

move = [rock, paper, scissors]
play = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
print ("You Chose:\n" + move[play])
compplay = random.randint(0,2)
print ("Computer Chose:\n" + move[compplay])

if play > 2 or play < 0:
    print ("Not a Real Option. You Lose.")
if play == compplay:
    print ("DRAW.")
elif play == 0 and compplay == 1:
    print ("You Lose.")
elif play == 1 and compplay == 2:
    print ("You Lose.")
elif play == 2 and compplay == 0:
    print ("You Lose.")
else:
    print ("You Win!")

    
