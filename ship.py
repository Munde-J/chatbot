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