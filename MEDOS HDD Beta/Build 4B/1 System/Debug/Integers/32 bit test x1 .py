count = int
in1 = str
print ("Opening debug tool: 32 bit count")
print ("This command tests your system to see if it can count to an 32 bit integer of 2147483647")
print ("{system} file selected: 32BITTESTX1.PY")
print ("Ready to launch!")
print ("|Your system has to have at least 16 Megabytes of RAM to run this command")
print ("Estimated time:")
print ("16 MB RAM = 1980 seconds")
print ("32 MB RAM = 1780 seconds")
print ("64 MB RAM = 1600 seconds")
print ("128 MB RAM = 1550 seconds")
print ("256 MB RAM = 1440 seconds")
print ("512 MB RAM = 1200 seconds")
print ("1028 MB RAM = 800 seconds")
print ("1500 MB RAM = 500 seconds")
print ("2056 MBB RAM = 400 seconds")
print ("Are you ready?")
print ("Type 'OPEN' to try out command")
in1 = str(input("FC://"))
if in1 == ("OPEN"):
	count = 0
	count = int
	count =+ 1
	print (count)
while not (count > 2147483647):
    count += 1
    print (count)
else:
        print ("You have successfully counted to a 32 bit integer")
testconfirm = int(input("Did the setup look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("System setup successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
    