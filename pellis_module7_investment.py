# Pj Ellis Module 7 - Investment Program
# Write a program that uses a while loop to determine how long it takes 
# for an investment to double at a given interest rate. The input will 
# be an annualized interest rate and the initial investment amount, and 
# the output is the number of years it takes an investment to double.

print("\tWelcome to ELLIS INVESTMENTS")
print()
question = input("Would you like to see how long it will take for an "
    "\ninvestment to double in value? (yes or no) ")
print()

if question.lower() == "yes":
	invest = float(input("How much money were you thinking of investing? $"))
	print()
	int_rate = float(input("What % interest rate are you expecting to have? "))
	print()
else:
	print("Thank you, and have a nice day!")
	exit()
	
goal = invest*2
rate = int_rate/100
principle = invest
year = 0

while principle < goal:
	principle = principle * rate + principle
	year +=1
	
	if principle >= goal:
		print()
		print(f"It will take {year} years for your initial investment of"
		f" ${invest} \nto double in value to the amount of ${principle:.{2}f}"
		f" \nat an interest rate of {int_rate}%!")
		print()
	
print()	
print("Thank you for stopping by!")
