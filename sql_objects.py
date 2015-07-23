import sqlite3

class SQL_Create_Object(object):
    def create_log_table(p_connection, p_cursor):
        p_cursor.execute('''
        create table if not exists xx_log(
                       session_id integer primary key autoincrement, 
                       log_text text,
                       creation_date timestamp default current_timestamp not null
                        ) ''')
        p_connection.commit()
    
    def create_column_dist_table(p_connection, p_cursor):
        p_cursor.execute('''
        create table if not exists xx_demo_dist_clmn_values(
                       column_name text, 
                       distinct_value_count integer,
                       generalization_value integer
                        ) ''')
        p_connection.commit()   

    def create_demo1_table(p_connection, p_cursor):
        p_cursor.execute('''
        create table if not exists xx_demo1(
                       data1 integer, 
                       data2 text,
                       data3 timestamp,
                       data4 text 
                        ) ''')
        p_connection.commit()  

    def create_demo2_table(p_connection, p_cursor):
        p_cursor.execute('''
        create table if not exists xx_demo2(
                       unikalus_id integer, 
                       rase text,
                       gimimo_data timestamp,
                       lytis text,
                       pasto_kodas text,
                       issilavinimas text,
                       liga text
                        ) ''')
        p_connection.commit()  

    def create_demo3_table(p_connection, p_cursor):
        p_cursor.execute('''
        create table if not exists xx_demo3(
                       rase text,
                       lytis text,
                       amzius integer,
                       liga text
                        ) ''')
        p_connection.commit()     

    def create_generalization_miestai_table(p_connection, p_cursor):
        p_cursor.execute('''
        create table if not exists xx_generalization_miestai(
                       level_0 text, 
                       level_1 text,
                       level_2 text,
                       level_max text
                        ) ''')
        p_connection.commit() 
        
    def create_generalization_lytis_table(p_connection, p_cursor):
        p_cursor.execute('''
        create table if not exists xx_generalization_lytis(
                       level_0 text, 
                       level_1 text,
                       level_2 text,
                       level_max text
                        ) ''')
        p_connection.commit() 
        
    def create_generalization_rase_table(p_connection, p_cursor):
        p_cursor.execute('''
        create table if not exists xx_generalization_rase(
                       level_0 text, 
                       level_1 text,
                       level_2 text,
                       level_max text
                        ) ''')
        p_connection.commit() 
        
    def create_generalization_issilavinim_table(p_connection, p_cursor):
        p_cursor.execute('''
        create table if not exists xx_generalization_issilavinim(
                       level_0 text, 
                       level_1 text,
                       level_2 text,
                       level_max text
                        ) ''')
        p_connection.commit() 

class SQL_Drop_Object(object):
    def drop_log_table(p_connection, p_cursor):
        p_cursor.execute(''' drop table if exists xx_log ''')
        p_connection.commit()

    def drop_column_dist_table(p_connection, p_cursor):
        p_cursor.execute(''' drop table if exists xx_demo_dist_clmn_values ''')
        p_connection.commit()

    def drop_demo1_table(p_connection, p_cursor):
        p_cursor.execute(''' drop table if exists xx_demo1 ''')
        p_connection.commit()

    def drop_demo2_table(p_connection, p_cursor):
        p_cursor.execute(''' drop table if exists xx_demo2 ''')
        p_connection.commit()

    def drop_demo3_table(p_connection, p_cursor):
        p_cursor.execute(''' drop table if exists xx_demo3 ''')
        p_connection.commit()

    def drop_generalization_miestai_table(p_connection, p_cursor):
        p_cursor.execute(''' drop table if exists xx_generalization_miestai ''')
        p_connection.commit()
        
    def drop_generalization_lytis_table(p_connection, p_cursor):
        p_cursor.execute(''' drop table if exists xx_generalization_lytis ''')
        p_connection.commit()
        
    def drop_generalization_rase_table(p_connection, p_cursor):
        p_cursor.execute(''' drop table if exists xx_generalization_rase ''')
        p_connection.commit()
        
    def drop_generalization_issilavinim_table(p_connection, p_cursor):
        p_cursor.execute(''' drop table if exists xx_generalization_issilavinim ''')
        p_connection.commit()
        
class SQL_Create_All_Objects(object):
    def create_all_tables(connection, cursor):
        SQL_Create_Object.create_log_table(connection, cursor)
        SQL_Create_Object.create_column_dist_table(connection, cursor)
        SQL_Create_Object.create_demo1_table(connection, cursor)
        SQL_Create_Object.create_demo2_table(connection, cursor)
        SQL_Create_Object.create_demo3_table(connection, cursor)
        SQL_Create_Object.create_generalization_miestai_table(connection, cursor)
        SQL_Create_Object.create_generalization_lytis_table(connection, cursor)
        SQL_Create_Object.create_generalization_rase_table(connection, cursor)
        SQL_Create_Object.create_generalization_issilavinim_table(connection, cursor)
    
        print('All objects are created')
        
class SQL_Drop_All_Objects(object):
    def drop_all_tables(connection, cursor):
        SQL_Drop_Object.drop_log_table(connection, cursor)
        SQL_Drop_Object.drop_column_dist_table(connection, cursor)
        SQL_Drop_Object.drop_demo1_table(connection, cursor)
        SQL_Drop_Object.drop_demo2_table(connection, cursor)
        SQL_Drop_Object.drop_demo3_table(connection, cursor)
        SQL_Drop_Object.drop_generalization_miestai_table(connection, cursor)
        SQL_Drop_Object.drop_generalization_lytis_table(connection, cursor)
        SQL_Drop_Object.drop_generalization_rase_table(connection, cursor)
        SQL_Drop_Object.drop_generalization_issilavinim_table(connection, cursor)
        
        print('All objects are droped')
        
