in1 = str
print ("Command testing")
print ("Test the Windows 9x compatibility command")
print ("Type '9XRUN' to try out the command!")
print ("Warning! Commands are CaSe SeNsItIvE")
in1 = str(input("FC:\\"))
if in1 == ("9XRUN"):
	print ("Windows 9x compatibility center")
	print ("1 Windows NT 4")
	print ("2 Windows 95")
	print ("3 Windows Chicago")
	print ("4 Windows 98")
	print ("5 Windows Memphis")
	print ("6 Windows 98 Second Edition")
	print ("7 Windows Millennium")
	print ("8 Windows Millennium Edition")
	print ("Choose a number 1-8 then click enter to continue compatibility testing")
	print ("Type XE to quit")
	print (in1)
testconfirm = int(input("Did the command info look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("Test successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
   