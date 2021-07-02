# Go on a Choose your Own Adventure style game made with Python.
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("There's two directions you can go, left or right. Which way do you want to go? \n")
if direction.upper() == "LEFT":
    travel = input("You went left and now there's a river in front of you. You can swim or wait. \nWhat will you do? \n")
    if travel.upper() == "WAIT":
        door = input("You were patient and waited. Now there's 3 doors ahead of you, red, blue, \nyellow, which will you go through? \n")
        if door.lower() == "red":
            print ("You got burned by fire. GAME OVER.")
        elif door.lower() == "blue":
            print ("You got attacked and eaten by monsters. GAME OVER.")
        elif door.lower() == "yellow":
            print ("You got the Treasure. YOU WIN.")
        else:
            print ("GAME OVER.")
    else:
        print ("You got attacked by a shark. GAME OVER.")
else:
    print ("You fell in a hole. GAME OVER.")
