import bluetooth
import MySQLdb


class bluesniff:
	def __init__(self,DBUser,DBPword,DBName,DBHost)
        self.DBUser = DBUser
        self.DBPword = DBPword
        self.DBName = DBName
        self.host = DBHost

# defines NewList and NewListCat as the names and addresses of devices
    def create_lists():
        for name, addr in nearby_devices:
            NewList =  [addr, name]
            NewListCat = []
            # used for historical references
            NewListCat = NewListCat.append(NewList)
        return

    def write_to_db(self):
        #(host,user,password,database)
        db = MySQLdb.connect(self.host,self.DBUser,self.DBPword,self.DBName)
        cursor = db.cursor()
        sql = "SELECT * FROM ActiveBlueTooth"
        for name, addr in nearby_devices:

    	print "%s, %s" % (name, addr)
            sql = """REPLACE INTO ActiveBlueTooth (TIMESTAMP, MAC, DeviceName, SensorID)
                VALUES (CURRENT_TIMESTAMP, '%s', '%s', '%s')""" % (name, addr, self.host)
            try:
                cursor.execute(sql)
                db.commit()
            except IOError as error:
                print error
                pass
        db.close()
