in1 = str
print ("Opening screensaver: Platformer sky")
print ("Type 'OPEN' to try out the screensaver!")
in1 = str(input("FC://"))
if in1 == ("OPEN"):
	print ("===")
	print (" = =")
	print (" ==== ==")
	print ("== === ==== ==")
	print ("--- ===  == == = == = =-  ")
	print ("===== = == = === == = == = == =-- -== == ")
	print ("========= ===================")
print (in1)
testconfirm = int(input("Did the setup look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("System setup successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
    