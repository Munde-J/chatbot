ShipName = "Ethiopian"
Captain = "Richard Luther"
Location = "Carlifonia"
Password = "!qwer!tyui!op[!"
PasswordAttempt = input("Ship Password: ")
while PasswordAttempt != Password:
	print("Incorrect password")
	PasswordAttempt = input("Ship Password: ")
print ("Password correct. Welcome aboard the", ShipName + ".")
print("\nThe spaceship", ShipName, "is currently at", Location + ".")
Choice = ""
while Choice != "d":
	print ("\nWhat would you like to do", Captain + "?\n")
	print ("1. Travel to another Country")
	print ("2. Fire cannons")
	print ("3. View your details")
	print ("4. Exit\n")
	Choice = input ("Enter your choice:  ")