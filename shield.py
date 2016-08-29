#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

import os
import sys
import subprocess
import pickle
import random

# Display the usage
def man_usage():
	print("\033[36;1m", "Usage:", "\033[0m", sep='')
	print("       ", sys.argv[0], " [change | reset] INTERFACE", sep='')
	print("")
	print("\033[36;1m", "Description:", "\033[0m", sep='')
	print("       ", "change INTERFACE", "    ", "Change INTERFACE mac address.", sep='')
	print("       ", "reset  INTERFACE", "    ", "Reset INTERFACE mac address.", sep='')

# Display help page, by using man_usage()
def man_help():
	print("\033[36;1;4m", "Shield - Network Guardian", "\033[0m", sep='')
	print("")
	man_usage()
	print("")
	print("\033[36;1m", "Examples:", "\033[0m", sep='')
	print("       ", sys.argv[0], " change wlan0", " # Change wlan0 mac address.", sep='')
	print("       ", sys.argv[0], " reset wlan0", "  # Reset wlan0 mac address.", sep='')
	print("")
	print("\033[36;1m", "See also:", "\033[0m", sep='')
	print("       ", "ifconfig (8)", sep='')
	print("")
	print("\033[36;1m", "Author:", "\033[0m", sep='')
	print("       ", "Valentin Berger <valentin.berger38@gmail.com>", sep='')

# Convert a number bounded by 0 and 15 in base 10 into the respective hexadecimal digit
def number10_to_digit16(digit10 : int = 0):
	if (digit10 < 0 or digit10 >= 16):
		raise ValueError("Error: " + str(digit10) + " is not an hexadecimal digit! The digit must be between <0>10 (<0>16) and <15>10 (<F>16)")
	
	if (digit10 >= 0 and digit10 <= 9):
		return str(digit10)
	else:
		return chr(ord('A') + (digit10 - 10))



### CHECKING ARGUMENT AND PRIVILEGES ###
# If the only argument is either '-h' or '--help', display man page and exit.
if (len(sys.argv) == 2):
	if (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
		man_help()
		sys.exit(0)

# If there are a number of argument different of 3, exit
if (len(sys.argv) != 3):
	print("\033[31m", sys.argv[0], ": Error: Wrong number of argument.", "\033[0m", sep='')
	man_usage()
	sys.exit(1)

# If the first argument is not change nor reset, exit.
if (sys.argv[1] != "change" and sys.argv[1] != "reset"):
	print("\033[31m", sys.argv[0], ": Error: Wrong argument.", "\033[0m", sep='')
	man_usage()
	sys.exit(2)

# If the second argument is not an interface, exit.
if (sys.argv[2] not in subprocess.Popen("ifconfig", shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8")):
	print("\033[31m", sys.argv[0], ": Error: ", sys.argv[2], " is not an interface available. Please check your available interface by typing ", "\033[31;1m", "ifconfig", "\033[31m", " in a terminal.", "\033[0m", sep='')

if (os.geteuid() != 0):
	print("\033[31m", sys.argv[0], ": Error: This application must be run as root.", "\033[0m", sep='')
	sys.exit(3)


### LOADING DATABASE ###
database = []

# If the compiled database is not available, compile it:
if not os.path.isfile("mac_producer.list"):
	try:
		database_file = open("mac_producer", "r")
		# Reading the file line  by line
		for line in database_file.readlines():
			mac_address = line.split('|')[0]
			producer = line.split('|')[1]
			producer = producer.replace('\n', '')
			database.append((mac_address, producer))
		
		# Save the database in compiled file, with pickle
		database_pickle_file = open("mac_producer.list", "wb")
		database_pickler = pickle.Pickler(database_pickle_file)
		database_pickler.dump(database)
		database_pickle_file.close()
		
		database_file.close()
		
	except FileNotFoundError:
		print("\033[31m", sys.argv[0], ": Fatal Error: The file \'mac_producer\' is necessary.", "\033[0m", sep='')
		sys.exit(2)
	except:
		print("\033[31m", sys.argv[0], ": Fatal Error: The file \'mac_producer.list\' is corrupted. PLease delete it, make sure the file \'mac_changer\' is in the same directory of this application and launch this one again.", "\033[0m", sep='')
		sys.exit(-1)
	
# If it exists, use it:
else:
	try:
		database_pickle_file = open("mac_producer.list", "rb")
		database_unpickler = pickle.Unpickler(database_pickle_file)
		database = database_unpickler.load()
		database_pickle_file.close()
	except:
		print("\033[31m", sys.argv[0], ": Fatal Error: The file \'mac_producer.list\' is corrupted. PLease delete it, make sure the file \'mac_changer\' is in the same directory of this application and launch this one again.", "\033[0m", sep='')
		sys.exit(-1)

# Create the mac address from the prefix database, and random hexadecimal number
random.seed(None)
(mac_address, producer) = database[random.randrange(0, len(database) - 1)]
mac_address += ":"
mac_address += number10_to_digit16(random.randrange(0, 15))
mac_address += number10_to_digit16(random.randrange(0, 15))
mac_address += ":"
mac_address += number10_to_digit16(random.randrange(0, 15))
mac_address += number10_to_digit16(random.randrange(0, 15))
mac_address += ":"
mac_address += number10_to_digit16(random.randrange(0, 15))
mac_address += number10_to_digit16(random.randrange(0, 15))


# Disabling the network interface
os.system("ifconfig " + sys.argv[2] + " down")
# If we have to change the mac address...
if (sys.argv[1] == "change"):
	os.system("ifconfig " + sys.argv[2] + " hw ether " + mac_address)
	print(sys.argv[2] + " mac address changed as " + mac_address + " (" + producer + ")")
# Else, if we have to reset it...
else:
	permanent_mac_address = subprocess.Popen("cat /sys/class/net/" + sys.argv[2] + "/address", shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8")
	os.system("ifconfig " + sys.argv[2] + " hw ether " + permanent_mac_address)
	print(sys.argv[2] + " mac address restored as " + permanent_mac_address)
# Enabling again the network interface
os.system("ifconfig " + sys.argv[2] + " up")

