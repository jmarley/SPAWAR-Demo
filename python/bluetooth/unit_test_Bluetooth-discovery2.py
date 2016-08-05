import bluetooth
import MySQLdb
import os
import bluesniff
import DiscoverBluetoothDevices

# pulls environement variables needed for connection to the database from openshift
DBUser = os.getenv("OPENSHIFT_MYSQL_DB_USERNAME")
DBPword = os.getenv("OPENSHIFT_MYSQL_DB_PASSWORD")
DBName = os.getenv("DBName")
DBHost = os.getenv("OPENSHIFT_MYSQL_DB_HOST")
DBPort  = os.getenv("OPENSHIFT_MYSQL_DB_PORT")
