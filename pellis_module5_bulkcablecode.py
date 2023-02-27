# Pj Ellis 8/28/2022 Module 5
# Gather COMPANY NAME and FEET of cable needed and give TOTAL COST for said Company
# Factor in an IF STATEMENT to give a BULK RATE on TOTAL COST of cable
# also added a couple little extra equations just to spruce up the output!

print()
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("*                     Hello there, and welcome to                   *")
print("*                                                                   *")
print("*               'The Ellis Fiber Optic Cable Emporium'              *")
print("*              A One Stop Shop For ALL Your Cable Needs             *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print()
print("Can I interest you in buying some Fiber Optic Cable for only $.87 per foot?")
print()
print("To continue with your order, we require some additional information:")

print()

import string
name = input("What is the name of your company: ")
comp_name = string.capwords(name)
# takes the name typed in and puts it in title format, yet will not capitalize 'S as i found to happen when using title()

print()

feet = int(input("How many feet of fiber optic cable will you be requiring: "))
print()

#this if statement will determine which bulk price to use based off the input of how many feet

if feet > 100 and feet <= 250:
    bulk_price = .80
elif feet > 250 and feet <= 500:
    bulk_price = .70
elif feet > 500:
    bulk_price = .50
else:
	bulk_price = .87

#this is a little equation i played around with to show the discount they receive for ordering in bulk

import math
# 'round' will round your number to whatever amount of decimals you chooose (x)
# (round(equation), x))
# for my purposes it will only figure discount to 2 decimal points, since our prices are all under 1.00
# and total cost is set to 2 decimal points so it looks like a real price, not a number with many numbers after decimal
# i also show a percent discount they are receiving, so its set to 0 decimal points, so it a round number.

price = .87
discount = (round(price - bulk_price, 2))
perc_discount = (round(((price - bulk_price)/price) *100, 0))

if feet > 100:
    print(f"CONGRATULATIONS! You qualify for our bulk rate, which takes ${discount} off per foot!")
    print(f"This saves you {perc_discount}% off our regular rate!")

total_cost = (round(feet * bulk_price, 2))

print()

print(f"For {feet} feet of fiber optic cable, provided to {comp_name}, you are looking at a Total Cost of ${total_cost}!")

print()

print("Thank you for stopping by and look forward to working with you again soon!")
