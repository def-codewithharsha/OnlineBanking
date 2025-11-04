import pypyodbc as odbc
import getpass

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
    
    def use_fetchall(self,query):
        self.query=query
        self.cursor.execute(self.query)
        return self.cursor.fetchall()
        
    def use_fetchone(self,query):
        self.query=query
        self.cursor.execute(self.query)
        return self.cursor.fetchone()








class UserSession:

    def __init__(self,user_id):
        self.bank_db = BankDataBase()
        self.user_id =user_id
        self.bank_db.cursor.execute("select fname from user_acts where uname=?",[self.user_id])
        self.user_fname=self.bank_db.cursor.fetchone()
        
    
    def user_balance(self):

        pass

    def transfer_user_funds():
        pass

    def view_user_transactions():
        pass
    
    def user_logout():
        pass

    def show_dashboard(self):
        while True:

            print(f"welcome {self.user_fname[0]}\n Menu:\n") 

            print(f"1. View Account Balance\n2. Transfer Funds\n3. View Transaction History\n4. Logout\n")

            try :
                int(self.nav)=input("Please select an option :").strip()
                match self.nav:
                    case 1:
                        pass
            except :
                print("Please enter vaild Option")

        



class LoginPage:

    def __init__(self):
        
        self.bank_db = BankDataBase()
        


    def auth_creds(self):
        
        self.auth_user=self.bank_db.auth_user(self.user_id,self.user_pswd)
       
        if self.auth_user:
            self.show_homepage=UserSession(self.user_id)
            self.show_homepage.show_dashboard()
        else:
            print("Please enter correct creds")


    def Show_login_page(self): # Validation of len and multiple attempts are pending
        print(f"Welcome To SREE BANK OF INDIA\n")
        self.user_id=input("Please Enter Your User Name: ").strip().lower()
        self.user_pswd=getpass.getpass("Please Enter Your Password: ").strip()
        
        self.auth_creds()


#AttributeError: 'OnlineBankApp' object has no attribute 'db'

if __name__=="__main__" :
    LoginPage().Show_login_page()