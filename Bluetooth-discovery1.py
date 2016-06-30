import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names = True)

if len(nearby_devices) == 1:
    print "Found %d device:" % len(nearby_devices)
elif len(nearby_devices) == 0:
    print "Found %d devices." % len(nearby_devices)
else:
    print "Found %d devices:" % len(nearby_devices)

for name, addr in nearby_devices:
     print " %s - %s" % (addr, name)

