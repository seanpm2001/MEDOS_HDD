in1 = str
print ("Command testing")
print ("Test the credits command")
print ("Type 'CRED' to try out the command!")
in1 = str(input("FC://"))
if in1 == ("CRED"):
	print ("MEDOS Credits")
	print ("=============")
	print ("Programming")
	print ("Sean P. Myrick")
	print (" ")
	print ("Concept")
	print ("Sean P. Myrick")
	print (" ")
	print ("Graphics")
	print ("Sean P. Myrick")
	print (" ")
	print ("Inspirations")
	print ("MS-DOS 6.2.2")
	print ("The Linux Kernel")
	print ("Western digital hard drives")
	print ("Trying to not be like Seagate")
	print ("The Windows CMD")
	print ("The BIOS")
	print ("Dell")
	print ("Intel")
	print ("Ubuntu 14.04")
	print (" ")
	print (" ")
	print (" ")
	print ("The command worked!")
print (in1)
testconfirm = int(input("Did the setup look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("System setup successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
    