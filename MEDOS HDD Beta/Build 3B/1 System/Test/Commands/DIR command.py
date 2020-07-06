in1 = str
print ("Command testing")
print ("Test the show directory command")
print ("Type 'DIR' to try out the command!")
print ("Warning! Commands are CaSe SeNsItIvE")
in1 = str(input("FC://"))
if in1 == ("DIR"):
	print ("Contents of FC drive")
	print ("System [DIR]")
	print ("Extras [DIR]")
	print ("Logs [DIR]")
	print ("Pictures [DIR]")
	print ("Videos [DIR]")
	print ("Documents [DIR]")
	print ("Audio [DIR]")
	print ("Other [DIR]")
	print ("DIRSORT.ini  0 bytes")
	print (in1)
testconfirm = int(input("Did the command info look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("Test successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
   