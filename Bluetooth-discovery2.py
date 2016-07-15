import bluetooth

search = 1
first = 1
NewList = []
NewListCat = []
OldList = []

while search == 1:              #Loops code infinitely.

    nearby_devices = bluetooth.discover_devices(lookup_names = True)

# On first iteration, prints initial device number reading with weird face.

    if first == 1:

        if len(nearby_devices) == 1:

            print "Found %d device:" % len(nearby_devices)

        elif len(nearby_devices) == 0:

            print "Found %d devices." % len(nearby_devices)

        else:

            print "Found %d devices:" % len(nearby_devices)
    
        for name, addr in nearby_devices:

            NewList =  [addr, name]
            NewListCat = NewListCat + NewList
            
            print NewList
            
# Writes number of devices and mac addresses to a file Bluetoothdata.txt            
        filewrite = open("BluetoothData.txt", "wr+")
        no = str(len(nearby_devices))
        filewrite.write(no + '\n' + '\n')
        for name, addr in nearby_devices:
            filewrite.write("%s - %s\n" % (addr, name))
        first = 2

        print ":-P"

# If no devices are connected, resets NewList to (none, none).

    elif len(nearby_devices)== 0:
        
        OldList = NewListCat

        NewList = []
        
    #If NewList and OldList are the same, prints sad face.
        
        if set(OldList) == set(NewList):
            print ":-("

    #If a difference in NewList occurs, prints difference with a smiley face.

        else:

            print "Found 0 devices."
        
            print "NewList: "
            print NewListCat
            print "OldList: "
            print OldList

        OldList = NewListCat
        
#Writes data to file        
        filewrite = open("BluetoothData.txt", "wr+")
        no = str(len(nearby_devices))
        filewrite.write(no + '\n' + '\n')
        for name, addr in nearby_devices:
            filewrite.write("%s - %s\n" % (addr, name))
           
        NewListCat = []

#If one or more devices is connected:
#    Writes NewList to OldList
#    Compares NewList and OldList
#    If the same, prints smiley face.
#    If different, prints number of devices with NewList and OldList.

    else:   
        OldList = NewListCat
        
        NewListCat = []
        
        for name, addr in nearby_devices:

            NewList =  [addr, name]
            
            NewListCat = NewListCat + NewList
            
        if set(OldList) == set(NewListCat):
            print "(-:"
    
        else:

            if len(nearby_devices) == 1:

                print "Found %d device:" % len(nearby_devices)

            else:

                print "Found %d devices:" % len(nearby_devices)

            print "NewList: "
            print NewListCat
            print "OldList: "
            print OldList

# Writes data to file            
        filewrite = open("BluetoothData.txt", "wr+")
        no = str(len(nearby_devices))
        filewrite.write(no + '\n' + '\n')
        for name, addr in nearby_devices:
            filewrite.write("%s - %s\n" % (addr, name))
