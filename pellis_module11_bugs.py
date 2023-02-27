#pj ellis - module 11 - ewww bugs!
#Finding daily income based off quantity of items sold at a local coffee
#shop.

print("It sure was a busy day at Cafe Pjae!!")
print("Let's see how much money we made today!")
print()

#dictionary of cafe items and costs
goods = (
	"signature coffee": 2.2, 
	"chai tea latte": 1.5, 
	"chocolate cake": 2.5, 
	"strawberry refresher": 3.75
	)

#loop to find out how many of each item we sold and calculate income
for item in goods.keys()
     income = 0
      qty = input(f"How many {item.title}s have you sold? ")
     income = income + qty * goods[item]

#message to give grand total
print(f"\nToday we made a total of ${income:0.2f}!!!\nGREAT JOB EVERYONE!")
