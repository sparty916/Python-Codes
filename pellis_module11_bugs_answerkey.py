#pj ellis - module 11 - ewww bugs - Answer Key!
#Finding daily income based off quantity of items sold at a local coffee
#shop.

print("It sure was a busy day at Cafe Pjae!!")
print("Let's see how much money we made today!")
print()

#dictionary of cafe items and costs
goods = {
	"signature coffee": 2.2, 
	"chai tea latte": 1.5, 
	"chocolate cake": 2.5, 
	"strawberry refresher": 3.75
	}##incorrect brackets used / () instead of {}
income = 0 ##needed to be placed outside of loop

#loop to find out how many of each item we sold and calculate income
for item in goods.keys(): ##needed to add the ':'
    qty = input(f"How many {item.title()}s have you sold? ") ##needed to add () to .title
    qty = int(qty) ##needed to convert qty from str or float to int
    income = income + qty * goods[item]

#message to give grand total
print(f"\nToday we made a total of ${income:0.2f}!!!\nGREAT JOB EVERYONE!")
