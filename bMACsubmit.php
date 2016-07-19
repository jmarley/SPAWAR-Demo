<html>
<head>
<style>
div.container {
    width: 100%;
    border: 1px solid gray;
}

header, footer {
    padding: 1em;
    color: white;
    background-color: black;
    clear: left;
}

nav {
    float: left;
    max-width: 150px;
    margin: 0;
    padding: 1em;
}

nav ul {
    list-style-type: none;
    padding: 0;
}
			
nav ul a {
    text-decoration: none;
}

article {
    margin-left: 155px;
    border-left: 1px solid gray;
    padding: 1em;
    overflow: hidden;
}
</style>
</head>
<body>

<div class="container">

<header>
   <img src="SPAWAR-PAC.jpg" alt="SSC PAC Logo" sytle="width:82px;height:75px;">
   <h1 style="text-align:center;">Bluetooth Registration Page</h1>
</header>
  
<nav>
  <ul>
    <li><a href="index.php">Home</a></li>
    <li><a href="Map.php">Map</a></li>
    <li><a href="BluetoothReg.php">Bluetooth Registration</a></li>
    <li><a href="WIFIReg.php">WIFI Registration</a></li>
  </ul>
</nav>

<article>
  <h1>Welcome to the Bluetooth Registration</h1>
  <br>
  Welcome!  
  <br>
  <p> 
  <?php
   $bMAC = $_POST["bMAC"]; // what was entered as a MAC Address
	echo "Here is your bMAC: " . $bMAC . "<br>";
  $username = $_POST["username"]; // what was entered as a username
	echo "Here is your username: " . $username . "<br>";
  $dbhost = getenv("OPENSHIFT_MYSQL_DB_HOST");
	//echo "Here is your dbhost variable: " . $dbhost . "<br>";
  $dbport = getenv("OPENSHIFT_MYSQL_DB_PORT");
	//echo "Here is your dbport variable: " . $dbport . "<br>";
  $dbuser = getenv("OPENSHIFT_MYSQL_DB_USERNAME");
	//echo "Here is your dbuser variable: " . $dbuser . "<br>";
  $dbpwd = getenv("OPENSHIFT_MYSQL_DB_PASSWORD");
	//echo "Here is your dbpwd variable: " . $dbpwd . "<br>";
  $dbname = phpwork;
	//echo "Here is your dbname variable: " . $dbname . "<br>";
  $connection = mysql_connect($dbhost.":".$dbport, $dbuser, $dbpwd);
	//echo "Here is your connection variable: " . $connection . "<br>";
  if (!$connection) {
    echo "Could not connect to database";
  } else {
    echo "Connected to database.<br>";
  }

  // Check that the input is valid
  $validCheck = 0;
  if(!preg_match("/^[0-9a-fA-F]{2}(?=([:;.]?))(?:\\1[0-9a-fA-F]{2}){5}$/",$bMAC)) { // check if valid MAC
     
     
     echo "<br><br> ERROR: Please enter a valid Bluetooth MAC Address <br><br>"; // failed valid MAC Address

  } else {


    if(!preg_match("/^[0-9a-zA-Z ]*$/",$username)) { // check if valid username

        echo "<br><br> ERROR: Please enter a valid username <br><br>"; // failed username

    } else {

	$dbconnection = mysql_select_db($dbname);
	$sql = "SELECT COUNT(*) AS total FROM UserMACs WHERE MAC = '" . $bMAC . "'";
	$results = mysql_query($sql);
	$row = mysql_fetch_assoc($results);
	$total = $row['total'];

	echo "<br><br> total = " . $total . "<br><br>";

	if($total == 1) {

            echo "<br><br> ERROR: Please enter a unique MAC Address <br><br>"; // failed unique MAC Address

        } else {

     
        $validCheck = 1;

        }

    }
  }



  echo "<br><br> Your validCheck is: " . $validCheck . "<br><br>";

  if($validCheck == 1) { // only insert data, if data is valid
      	$dbconnection = mysql_select_db($dbname);
	$sql = "INSERT INTO UserMACs " . "(MAC, User) " . "VALUES ('" . $bMAC . "', '" . $username . "' )";
        $retval = mysql_query($sql);

        echo "<br><br> Query is: " . $sql . " <br><br> and results are: " . $retval . " <br><br>";

	if (! $retval ) {
		echo "<br><br> ERROR: Could not enter data <br><br>";
	} else {
		echo " <br><br> Data successfully enetered <br><br>";
	}
 
  }


  
  mysql_close();
?>
  <br><br><br>
  <h1>Would you like to register another Bluetooth MAC address?</h1>
  Please type in the MAC address of your BlueTooth device, and the username you would like to have associated with it:
  <form action="bMACsubmit.php" method="post">
	Bluetooth MAC: <input type="text" name="bMAC"><br>
	Username: <input type="text" name="username"><br>
	<input type="submit">
  </form>
  <br>
  <br>
  <a href="BluetoothReg.php">Click Here to return to the Bluetooth Registration page</a></li>

</article>

<footer><p style="text-align:center;">Thank You, Team SDE</p></footer>

</div>

</body>
</html>