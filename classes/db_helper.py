import re
import sqlite3


class DB_Helper:
    def __init__(self, db_name):
        """
        ------------------------------------------------------------------------------------------
        Initialization. Connection to database file.

        type(db_name) >> str
        db_name = <file_name>.db or <file_name>.sqlite3
        ------------------------------------------------------------------------------------------
        """

        self.connect = sqlite3.connect(f"static/db/{db_name}")
        self.cursor = self.connect.cursor()
    
    def add(self, table_name, args):
        """
        ------------------------------------------------------------------------------------------
        Adding users to database.

        type(table_name) >> str
        type(args) >> list
        ------------------------------------------------------------------------------------------
        """
        
        request = f"INSERT INTO {table_name} VALUES ({','.join(['?'] * len(args))})"

        try: 
            self.cursor.execute(request, args)
        except Exception:
            return "EmailUsed"
        else:
            self.connect.commit()
            return "Success"
    
    def get(self, table_name, email):
        """
        ------------------------------------------------------------------------------------------
        Getting info about users from database.

        type(table_name) >> str
        type(email) >> str
        ------------------------------------------------------------------------------------------
        """

        request = f"SELECT * FROM {table_name} WHERE email='{email}'"

        self.cursor.execute(request)

        try: 
            data = self.cursor.fetchall()[0]
        except Exception:
            return "NotFound"
        else:
            return data

