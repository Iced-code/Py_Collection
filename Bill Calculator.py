# A calculator which calculates the amount paid per person given the total bill, tip precentage, and amount of people. 
print ("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people = input("How many people to split the bill? ")

amount = (float(bill) / int(people)) *  (tip + 1.00)

amount = round(amount, 2)

print (f"Each person should pay: ${amount}")

