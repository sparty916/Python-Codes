# Pj Ellis 8/21/2022 Module 3
# Gather COMPANY NAME and FEET of cable needed and give TOTAL COST for said Company

print()
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("*                     Hello there, and welcome to                   *")
print("*                                                                   *")
print("*               'The Ellis Fiber Optic Cable Emporium'              *")
print("*              A One Stop Shop For ALL Your Cable Needs             *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print()

print("To continue with your order, we require some additional information:")

print()

import string
name = input("What is the name of your company: ")
comp_name = string.capwords(name)
# takes the name typed in and puts it in title format, yet will not capitalize 'S as i found to happen when using title()

print()

import math
feet = int(input("How many feet of fiber optic cable will you be requiring: "))
total_cost = (round(feet * .87, 2))
# will only print total cost to 2 decimal points so it looks like a real price, not a number with many numbers after decimal

print()

tot_cst_msg = f"For {feet} feet of fiber optic cable, provided to {comp_name}, you are looking at a Total Cost of ${total_cost}!"

print(tot_cst_msg)

print()

print("Thank you for stopping by and look forward to working with you again soon!")
