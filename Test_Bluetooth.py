# Test if lists are the same
def test_lists():
  if set(OldList) == set(NewListCat) is False:
    print "test_lists: Error"

# Test if Bluetooth-discovery2.py has finished its first iteration
def test_first():
  if first == 2 is False: 
    print "test_first: Error"
