#Tip percentage calculator
print ("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = float(input ("How many people to split the bill? "))
percent = float(input("What percentage would you like to give? "))
percent = percent / 100 + 1
total_per_person = round (bill / people * percent, 2)
total_per_person = str(total_per_person)
print ("Each person should pay: $"+total_per_person)

