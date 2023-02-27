# Pj Ellis - Module 8 - Functions
# For this module’s assignment, write a program that uses a function to 
# convert miles to kilometers. Your program should prompt the user for 
# the number of miles driven then call a function that converts miles to 
# kilometers. Check and validate all user input and incorporate 
# Try/Except block(s). The program should then display the total miles 
# and the kilometers

km = 1.609341 #global constant

def km_conv(miles):
	"""converts miles into kilometers"""
	try: 
		miles = float(miles)
		if miles < 0:
			print("Please only put in positive numbers!")
		else:
			km_driven = miles*km
			print(f"\n\tOn your {miles} mile drive, you drove a total "
			f"of {km_driven:.{2}f} kilometers!")
	except: 
		print("Please enter a numeric value!")


print("Welcome to Conversion Control")
print("\nWe are going to convert miles into kilometers!")

while True:
	miles = input("\nHow many miles have you driven? ")
	km_conv(miles)
	print("\nWould you like to try again?")
	more = input("Press 0 to exit ")
	if more == "0": #to end the loop
		break
	
print("\nThank you, and have a great day!")
