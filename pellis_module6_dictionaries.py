#PJ Ellis - Module 6 - Dictionaries
#For this assignment, we will work with dictionaries. 
#Create a program that includes a dictionary of a topic that interests you. 
#Your dictionary should include at least 10 different key-value pairs. 
#For this program, the key values may be a number or string. 
#Display all the key values to the user asking them to select one, 
#and then display the value paired to the key.

import time 
#wanted to have a dramatic pause so imported this feature
#udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html

oscar_win = {
    2012: "Argo", 
    2013: "12 Years a Slave", 
    2014: "Birdman or (The Unexpected Virtue of Ignorance",
    2015: "Spotlight",
    2016: "Moonlight",
    2017: "The Shape of Water",
    2018: "Green Book",
    2019: "Parasite",
    2020: "Nomadland",
    2021: "CODA",
    }
  
print("Please select a year from the following options, "
    "and I will show you the movie that won The Oscar for Best Picture!")
print()
print("The nominees are:")
for year in oscar_win:
    print(year)
print()

user_pick = int(input("Which year would you like to see?: "))
print()
print()

if user_pick in oscar_win:
	print("May I have the envelope please...")
	print()
	time.sleep(2) #wanted to have a dramatic pause so added this in
	print("...(paused for dramatic effect)...")
	time.sleep(2) #just to build up anticipation
	print()
	print(f"...And the Academy Award for Best Picture in {user_pick} went to:")
	print()
	time.sleep(2) #once more just like it would be at the Oscars
	print("\t" + oscar_win[user_pick])
else:
	print("I'm sorry, but the year you entered was not a valid option, "
	"please read the instructions and try again.")
	
