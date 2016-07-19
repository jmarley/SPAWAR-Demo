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
   <h1 style="text-align:center;">Register Your Bluetooth MAC</h1>
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
  <h1>Listing of known Bluetooth Devices</h1>
  <p> 
  <?php
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
  $dbconnection = mysql_select_db($dbname);
  $query = "SELECT * from UserMACs";
  $rs = mysql_query($query);
  while ($row = mysql_fetch_assoc($rs)) {
    echo $row['MAC'] . " " . $row['User'] . "\n<br>";
  }
  mysql_close();
?>
  <br><br><br>
  <h1>Register your BlueTooth MAC</h1>
  Please type in the MAC address of your BlueTooth device, and the username you would like to have associated with it:
  <form action="bMACsubmit.php" method="post">
	Bluetooth MAC: <input type="text" name="bMAC"><br>
	Username: <input type="text" name="username"><br>
	<input type="submit">
  </form>

</article>

<footer><p style="text-align:center;">Thank You, Team SDE</p></footer>

</div>

</body>
</html>