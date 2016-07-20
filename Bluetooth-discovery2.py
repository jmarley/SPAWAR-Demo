import bluetooth

search = 1
first = 1
# TODO look at moving upper level scope
NewList = []
NewListCat = []
OldList = []

while search == 1:              #Loops code infinitely.

# TODO Reset device list to null each iteration
    nearby_devices = bluetooth.discover_devices(lookup_names = True)

# On first iteration, prints initial device number reading with weird face.

    if first == 1:

# possiblity to simplifying conditinoals
        if len(nearby_devices) == 1:

            print "Found %d device:" % len(nearby_devices)

        elif len(nearby_devices) == 0:

            print "Found %d devices." % len(nearby_devices)

        else:

            print "Found %d devices:" % len(nearby_devices)

        # TODO look into using/creating method
        for name, addr in nearby_devices:

            NewList =  [addr, name]
            # used for historical references
            NewListCat = NewListCat + NewList

            # testing
            print NewList

# Writes number of devices and mac addresses to a file Bluetoothdata.txt
        filewrite = open("BluetoothData.txt", "wr+")
        no = str(len(nearby_devices))
        # writes number of near by devices
        filewrite.write(no + '\n' + '\n')

        for name, addr in nearby_devices:
            filewrite.write("%s - %s\n" % (addr, name))
        # TODO close file when done writing
        # tracking variable
        first = 2

        # testing
        print ":-P"

# If no devices are connected, resets NewList to (none, none).

    elif len(nearby_devices)== 0:

        # track historical device list
        OldList = NewListCat

        # null list of devices
        NewList = []

    #If NewList and OldList are the same, prints sad face.

        # conditional block used for local testing
        # TODO create unit test for conditional block
        if set(OldList) == set(NewList):
            print ":-("

    #If a difference in NewList occurs, prints difference with a smiley face.

        else:

            # print "Found 0 devices."

            print "NewList: "
            print NewListCat
            print "OldList: "
            print OldList
        #
        OldList = NewListCat

        #Writes data to file
        # TODO write method for opening and writing to a file
        filewrite = open("BluetoothData.txt", "wr+")
        no = str(len(nearby_devices))
        filewrite.write(no + '\n' + '\n')
        for name, addr in nearby_devices:
            filewrite.write("%s - %s\n" % (addr, name))
        # TODO close file
        # TODO look at moving upper level scope
        NewListCat = []

#If one or more devices is connected:
#    Writes NewList to OldList
#    Compares NewList and OldList
#    If the same, prints smiley face.
#    If different, prints number of devices with NewList and OldList.

    else:
        OldList = NewListCat
        # TODO look at moving upper level scope
        NewListCat = []
        # TODO look into using/creating method
        for name, addr in nearby_devices:

            NewList =  [addr, name]

            NewListCat = NewListCat + NewList

        # TODO create unit test for conditional block
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
# TODO use existing method for block below            
        filewrite = open("BluetoothData.txt", "wr+")
        no = str(len(nearby_devices))
        filewrite.write(no + '\n' + '\n')
        for name, addr in nearby_devices:
            filewrite.write("%s - %s\n" % (addr, name))
