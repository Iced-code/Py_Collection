import random


gameOn = True
amount_imposters = 2
Imposters = []
Votes = []
x = ""
i = 0
count = 0
yes = 0
yes = str(yes)
b = 0
you = input("\nWhat is your name? ")
Players = [you,"Joe", "Bob", "Ava", "Mia","Lena"]
while amount_imposters != 0:
    x = random.choice(Players)
    if x not in Imposters:
        Imposters.append(x)
    amount_imposters -= 1
print ("")
if you in Imposters:
    print (f"You are the Villains: {Imposters}\nVote to remove the other players to win.")
else:
    print ("You are a Player, vote to remove the villains and win.")
print ("")
while gameOn == True:
    print ("Players:", Players)
    play = input("Vote to remove someone: ")
    print ("")
    compplay = random.choice(Players)
    if play in Players:
        print (f"{you} Vote: {play}")
        Votes.append(play)
        i = 1
        while i != len(Players):
            a = random.choice(Players)
            print (Players[i],"Vote:", a)
            Votes.append(a)
            i += 1
        print ("")
        b = 0
        count = 0
        while b != len(Votes):
            if Votes.count(Votes[b]) > count:
                yes = Votes[b]
                count = Votes.count(Votes[b])
            b += 1
        if yes in Imposters:
            print (yes, "was a Villain.")
            Imposters.remove(yes)
            Players.remove(yes)
            if len(Imposters) == 0:
                break
        else:
            print (yes, "was not a Villain, they were removed.\n")
            Players.remove(yes)
        Votes = []
        if len(Players) <= 2:
            break
print ("------------------------------------------")
if len(Imposters) >= 1:
    print ("Villains Win!\nVillains:", Imposters)
elif len(Imposters) == 0:
    print ("Players Win!\nPlayers:", Players)