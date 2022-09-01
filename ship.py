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
	if Choice == "a":
		Location = input ("Where would you like to go? ")
		print ("\nTravelling...")
		time.sleep(2)
		print (ShipName, "has arrived at", Location + ".")
		time.sleep(0.5)
	elif Choice == "b":
		print ("\nFiring cannons...")
		time.sleep(1)
		print ("\nBANG!")
		time.sleep(1.5)
	elif Choice == "c":
		print ("\nShip name:", ShipName)
		print ("Capain:", Captain)
		print ("Location:", Location)