import pypyodbc as odbc

class BankDataBase:
    DRIVER_NAME ='SQL SERVER'
    SERVER_NAME =r'HARSHA\SQLEXPRESS'
    DATABASE_NAME='BANK_DB'

    def __init__(self):
        connection_string = f"""
            DRIVER={{{self.DRIVER_NAME}}};
            SERVER={self.SERVER_NAME};
            DATABASE={self.DATABASE_NAME};
            Trust_Connection=yes;"""
        self.con =odbc.connect(connection_string)
        self.cursor =self.con.cursor()

    def auth_user(self,user_id,user_pswd):
        self.cursor.execute("Select 1 from user_acts where uname=? and user_pwd=?",[user_id,user_pswd])
        return self.cursor.fetchone() is not None
    
    def excute(self,query,params=None):
        self.cursor.execute(query,params or [])

    def use_fetchall(self):
        return self.cursor.fetchall()
        
    def fetchone(self):
        return self.cursor.fetchone()
    
    def close_con(self):
        self.cursor.close()
        self.con.close()