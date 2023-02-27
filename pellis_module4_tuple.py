#PJ ELLIS - Module 4 - Tuples
#Create a tuple with 15-25 values and complete the following steps
#Step 1 - Initialize with values
#Step 2 - Display the contents in a single statement
#Step 3 - Iterate through the collection
# displaying the output as a single complete sentence for each value
# using the f-string format to control the output
#Step 4 - Repeat the output in reverse order using a diffent contest string

print("Welcome to PJ's Tuple of National Parks!")
print()
print("For optimal viewing, please maximize your screen.")
print()
step_1 = input("When you are ready to continue, press 1 followed by enter: ")
print()

#I did this next if statement before each section of the program so you can see each step
#before it went to far up the screen
#i assume you will actually use the number 1, and not try to trick my program!

if step_1 == "1":
	print("STEP ONE: Initialize with values!")
print()

#Part 1 - Initialize with values

nat_parks = ("yosemite", "yellowstone", "everglades", "great smokey mountains", "zion", "shenandoah", "olympic", "mount rainier", "grand teton", "sequoia", "denali", "grand canyon",  "death valley", "joshua tree", "kings canyon")
print("**You'll have to read the code to see how I did that**")
print()

step_2 = input("When you are ready to continue, press 1 followed by enter: ")
print()
if step_2 == "1":
	print("STEP TWO: Display the contents in a single statement!")
print()	

#Step 2 - Display the contents in a single statement

print("Here is my list of National Parks:")
print(nat_parks)
print()

#added this in to make the first series output to be contained in a SENTENCE
#instead of a SINGLE STATEMENT, like the assignment said

print("Or I could list them this way:")
print()
print(f"You will find {nat_parks} in my list of National Parks.")
print()

print("Or if you prefer, I can also list them this way instead:")
for park in nat_parks:
    print(park)
print()


step_3 = input("When you are ready to continue, press 1 followed by enter: ")
print()
if step_3 == "1":
	print("STEP THREE - Iterate thru the collection using a f-string")
print()

#Step 3 - Iterate through the collection
#	displaying the output as a single complete sentence for each value
#   Use the f-string format to control the output

for park in nat_parks:
	print(f"The parks proper name is: {park.title()} National Park!")
print()

step_4 = input("When you are ready to continue, press 1 followed by enter: ")
print()
if step_4 == "1":
	print("STEP FOUR - Repeat the output in reverse order using a diffent contest string")
print()

#Part 4 - Repeat the output in reverse order using a diffent contest string

print("Original Tuple:")
print(nat_parks)
print()

print("Reversed Tuple:")
new_parks = reversed(nat_parks)
new_parks = tuple(new_parks)
print(new_parks)
print()

print("Reversed Tuple using f-string:")
for parks in new_parks:
	print(f"I have always wanted to visit {parks.title()} National Park!")
print()
print("*see code for a link to the webpage I learned this trick from!")
print()

#https://www.tutorialkart.com/python/python-reverse-a-tuple/
#this is where i learned about the reversed() funtion for Python

end_mes = input("When you are ready to continue, press 1 followed by enter: ")
print()
print()
if end_mes == "1":
	print("Thank you for coming to my Tuple Talk!")
print("Good Bye!")
print()
