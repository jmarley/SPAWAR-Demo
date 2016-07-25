import bluetooth
import Test_Bluetooth.py

first = 1
NewList = []
NewListCat = []
OldList = []

# writes data to a file
def write_to_file ():
    filewrite = open("BluetoothData.txt", "wr+")
    no = str(len(nearby_devices))
    filewrite.write(no + '\n' + '\n')
    for name, addr in nearby_devices:
        filewrite.write("%s - %s\n" % (addr, name))
    filewrite.close()
    return

# defines NewList and NewListCat as the names and addresses of devices
def create_lists()
    for name, addr in nearby_devices:

        NewList =  [addr, name]
        # used for historical references
        NewListCat = NewListCat + NewList
    
    return 
    
while True:              #Loops code infinitely.

    nearby_devices = bluetooth.discover_devices(lookup_names = True)
    
    # Defines lists for each iteration.
    OldList = NewListCat
    test_lists()
    NewListCat = []
    NewList = []

    # Begins first iteration.
    if first == 1:

# possiblity of simplifying conditionals
        if len(nearby_devices) == 1:

            print "Found %d device:" % len(nearby_devices)

        elif len(nearby_devices) == 0:

            print "Found %d devices." % len(nearby_devices)

        else:

            print "Found %d devices:" % len(nearby_devices)
        
        # Creates lists of devices
        create_lists()

        # Tests that the lists are correct
        test_lists()

# Writes number of devices and mac addresses to a file Bluetoothdata.txt
        write_to_file()
        
        first = 2

        # testing
        test_first()

    elif len(nearby_devices)== 0:

        print "Found 0 devices."

        # Write data to a file
        write_to_file()

#If one or more devices is connected:
#    Writes NewList to OldList
#    Compares NewList and OldList

    else:
        
        # Creates lists of devices
        create_lists()

        if len(nearby_devices) == 1:

            print "Found %d device:" % len(nearby_devices)

        else:

            print "Found %d devices:" % len(nearby_devices)

        # Tests Lists
        test_lists()

# Writes data to file
        write_to_file()
