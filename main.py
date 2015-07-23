import sql_init
import sql_objects
import from_and_to_csv
class InitDB(object):
    def runDB(self):
        print ("Data Anonimization!")
        
        o_db = sql_init.SQL_Class
        l_connection, l_c = o_db.connect("test.db")
        
        sql_objects.SQL_Create_All_Objects.create_all_tables(l_connection, l_c)
        # sql_objects.SQL_Drop_All_Objects.drop_all_tables(l_connection, l_c)

        print("import")
        from_and_to_csv.Csv2Sqlite.convert_test("demo1.csv", l_connection, l_c, "demo1")
        
        sql_init.SQL_Class.close(l_connection)

        print("Data")
        return l_connection, l_c


    
if __name__ == '__main__':
    
    g_connection, g_c = InitDB().runDB()

    
