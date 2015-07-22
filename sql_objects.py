import sqlite3

class SQL_Create_Object(object):
    def create_log_table(l_connection, l_cursor):
        # Get a cursor object
        l_cursor.execute('''
        create table if not exists xx_jm_log(
                       session_id INTEGER PRIMARY KEY, 
                       log_text TEXT,
                       creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                        ) ''')
        l_connection.commit()
        
class SQL_Drop_Object(object):
    def drop_log_table(l_connection, l_cursor):
        # Get a cursor object
        l_cursor.execute(''' drop table if exists xx_jm_log ''')
        l_connection.commit()
        
class SQL_Create_All_Objects(object):
    def create_all_table(connection, cursor):
        print('All objects are created')