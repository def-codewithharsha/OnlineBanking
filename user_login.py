from bankdatabase import BankDataBase
from user_session import UserSession
import getpass



class LoginPage:

    def __init__(self):
        self.bank_db = BankDataBase()
        
    def auth_creds(self):
        self.auth_user=self.bank_db.auth_user(self.user_id,self.user_pswd)
       
        if self.auth_user:
            self.show_homepage=UserSession(self.user_id,self.bank_db)
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