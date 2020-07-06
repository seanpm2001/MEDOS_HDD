in1 = str
print ("Command testing")
print ("Test the Windows 3.x compatibility command")
print ("Type '3.RUN' to try out the command!")
print ("Warning! Commands are CaSe SeNsItIvE")
in1 = str(input("FC:\\"))
if in1 == ("3.RUN"):
	print ("Windows 3 compatibility center")
	print ("1 Windows 3.0")
	print ("2 Windows 3.1")
	print ("3 Windows 3.11")
	print ("4 Windows 3.2")
	print ("5 Windows 3.5")
	print ("6 Windows NT 3.5")
	print ("7 Windows NT 3.1")
	print ("8 Windows NT 3.11")
	print ("9 Windows NT 3.51")
	print ("Choose a number 0-9 then click enter to continue compatibility testing")
	print ("Type XE to quit")
	print (in1)
testconfirm = int(input("Did the command info look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("Test successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
   