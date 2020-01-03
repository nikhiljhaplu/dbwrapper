#DBWRAPPER
import sqlite3
class DataBaseWrapper:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    ##################################################
    ############create table query method#########################
    def create_table(self, table_name, table_columns):
        query = f'create table if not exists {table_name}({table_columns})'
        #create table if not exists trip_details(id int primary key, title string, description string, price string)'
        self.c.execute(query)
        self.conn.commit()

    ##################################################
    ############insert query method#########################
    def insert_table(self, table_name, insert_values):
        query = f"insert into {table_name} values({insert_values})"
        #insert into trip_details values('1', 'kokcha  2019', 'very great trip', '5000-6000')
        try:
            self.c.execute(query)
            self.conn.commit()
        except:
            print("please select unique value or try update query")
        self.conn.commit()

    ##################################################
    ############update query method#########################
    def update_table(self, table_name, update_values, where_to_update):
        query = f'''update {table_name} set {update_values} where {where_to_update}'''
        self.c.execute(query)
        self.conn.commit()

    ##################################################
    ############fetch method#########################
    def fetch_table(self, table_name):
        query = f"select * from {table_name}"
        self.c.execute(query)
        self.conn.commit()
        fetch = self.c.fetchall()
        print(fetch)
        return fetch
    ##################################################
    ############close method#########################
    def close_connection(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

#########object created with the database name required
#obj1 = DataBaseWrapper("dbextra")    #//here dbextra is database name
#########to create table first we have to give table name and then column names
#obj1.create_table('tabextra','id int primary key, title string, description string, price string')
#tabextra = table name, id = 1st column, title = 2nd column , description = 3rd column, price = 4th column
#########to inser values we have to give table name first and than values for every columns
#obj1.insert_table('tabextra#----//(table name)//---#',"2#----//(id column1)//---#, 'testing2'#----//(title column2)//---#, 'damnnnnnnnn descript2'#----//(description column3)//---#, 1234#----//(price column 4)//---#")
#########to update first have to give table name and then the column name and values to update and then the location pointed where to update
#obj1.update_table("tabextra","description = 'updated', price = '5000'","id = '1'")
#########to fetch all result
#obj1.fetch_table('tabextra')

#db name = dbextra
#table name = tabextra
obj1 = DataBaseWrapper("dbextra")
obj1.create_table('tabextra','id int primary key, title string, description string, price string')
obj1.insert_table('tabextra',"2, 'testing2', 'damnnnnnnnn descript2', 1234")
obj1.update_table("tabextra","description = 'updated done', price = '5000'","id = '1'")
obj1.fetch_table('tabextra')