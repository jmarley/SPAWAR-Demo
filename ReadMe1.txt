Is written in PHP 5.3 and MySQL 5.5

Is a part of OpenShift on redhat.com
   - Also uses phpMyAdmin 4.0 for database management

Within MySQL:
  - Title the DB: phpwork
      - Title the Table: UserMACs
           - Create 2 columns:
                - "MAC" = char, 17 in length
                - "User" = char, 24 in length

Pages still provide alot of troubleshooting information... need to clean them up
   - Need to incorporate reading Piper's file for the home page 
   - Need to incorporate a Map and results of Piper's file on the Map page
   - Clean up the Bluetooth Registration page
   - On the WIFI registration page, duplicate the logic (new terminology and SSID inclusion) for the WIFI registration setup

page details:

index.php (Home) = homepage, plan to use the text file from Piper to build out a table of active MACs (and other info?), and then look up the MAC addresses in the MySQL Database to provide a registered name

Map.php (Map) = to put the map, and some alert/information on how many active MACs exist

BluetoothReg.php (Bluetooth Registration) = (a) provides a listing of currently registered Bluetooth MAC addresses, and the assocatied username / name and (b) provides a place a user can type in a new Bluetooth MAC and desired username to be registered

bMACsubmit.php = page that actually enters the desired bluetooth MAC into the DB
  (a) first checks that the input is valid (i) valid MAC address, (ii) username is only letters, numbers, and spaces, and (iii) it is a unique MAC address... before even attempting to enter the requested MAC as a registered MAC with username
  (b) it then asks the user if they would like to enter another

WIFIReg.php (WIFI Registration) = page to act in a similar way as the BluetoothReg.php page

index-PHPinfo.php = page that provides environmental variables