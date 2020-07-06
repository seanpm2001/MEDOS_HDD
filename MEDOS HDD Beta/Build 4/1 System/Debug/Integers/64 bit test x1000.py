count = int
in1 = str
print ("Opening screensaver: CNT64SPACE")
print ("Type 'OPEN' to try out the screensaver!")
in1 = str(input("FC://"))
if in1 == ("OPEN"):
	count = 0
	count = int
	count =+ 1000
	print (count)
while not (count > 9223372036854775807):
    count += 1000
    print (count)
else:
        print ("You have successfully counted to a 64 bit integer")
testconfirm = int(input("Did the setup look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("System setup successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
    