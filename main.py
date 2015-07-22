import sql_init
import sql_objects
class Example(object):
    def run(self):
        print ("Data Anonymization!")
        l_connection, l_c = sql_init.SQL_Class.connect("test.db")
        
        sql_objects.SQL_Create_Object.create_log_table(l_connection, l_c)
        sql_objects.SQL_Drop_Object.drop_log_table(l_connection, l_c)
        sql_init.SQL_Class.close(l_connection)
        
        print("Data")
if __name__ == '__main__':
    Example().run()
    
