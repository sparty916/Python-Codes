#Pj Ellis - Module 10 - Files

#For this module, we will create a program that performs file processing 
#activities. 
#use the OS library in order to validate that a directory exists before creating a file in that directory.
#Prompt the user for the directory they would like to save the file in 
#as well as the name of the file.
#Prompt the user for their name, address, and phone number.
#Write this data to a comma separated line in a file and store the file in the directory specified by the user.
#Read the file you just wrote to the file system and display the file contents to the user for validation purposes.

import os

print("Welcome to Ellis File Writing Emporium!")
print()
print("Today you are going to write a file into a directory of your choosing,"
	"\n and then we are going to make sure that the info you wrote is correct!")
print()

#shows the directory that we are currently in	
def current_path(): 
    print("\nThe Current Working Directory is:") 
    print(os.getcwd()) 
    print()

current_path()
#asks what directory they would like the file saved in
def directory():
	keep = input("Would you like to keep this directory?: (y/n)")
	if keep.lower() == "n":
		userDir = input("What Directory would you like to use?: ")
		os.chdir(userDir)
		current_path()
		directory()

directory()
#asks user to name the file that want saved
userFile = input("\nWhat would you like the name of your file to be?: ")
filename = (f"{userFile}.txt")

#all the input we need to acquire for the file
def file_input():
	print("\nPlease provide us with the following information for your file:")
	fullname = input("Full Name: ")
	strtaddy = input("Street Address: ")
	cityaddy = input("City: ")
	stateaddy = input("State: ")
	zipcode = input("Zip Code: ")
	phone = input("Phone Number: ")
	text_to_write = (f"{fullname.title()}, {strtaddy.title()}, {cityaddy.title()}, {stateaddy.upper()}, {zipcode}, {phone}")
	with open(filename, 'w') as file_object:
	    file_object.write(f"{text_to_write}")

file_input()

#verification process of entered information
while True:
	print("\nNow let us verify that this information is correct:")
	with open (filename) as file_object:
		contents = file_object.read()
	print()
	print(contents)
	correct = input("\nDoes this information look correct? (y/n)")
	if correct.lower() == ('y'):
		print("\n\tThank you for allowing us to write your file!")
		break
	else:
		print("\n\tUh Oh! I wonder what happened!  Let's try again!")
		file_input()
