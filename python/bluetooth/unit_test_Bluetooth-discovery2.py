#python modules
import bluetooth
import MySQLdb
import os
import unittest
#project code
import bluesniff

# pulls environement variables needed for connection to the database from openshift
DBUser = os.getenv("OPENSHIFT_MYSQL_DB_USERNAME")
DBPword = os.getenv("OPENSHIFT_MYSQL_DB_PASSWORD")
DBName = os.getenv("DBName")
DBHost = os.getenv("OPENSHIFT_MYSQL_DB_HOST")
DBPort  = os.getenv("OPENSHIFT_MYSQL_DB_PORT")
class TestBluesniff(unittest.TestCase):
    def setUp(selfself,DBUser,DBPword,DBName,DBHost):
        testdb = bluesniff.bluesniff(self,DBUser,DBPword,DBName,DBHost)

    def tearDown(self):
        del tesdtdb

    def DBExistTest(self):
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
	    self.assertEqual(1,data)

    def write2dbtest(self):
        bluesniff.write_to_db()
        read from db
        assert

if __name__ == '__main__':
 	unittest.main()
