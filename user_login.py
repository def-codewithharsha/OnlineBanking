from bankdatabase import BankDataBase
from user_session import UserSession
import getpass



class LoginPage:

    ATTEMPTS=3

    def __init__(self):
        self.bankdatabase = BankDataBase()
        self.attempt_count=0
        
    def auth_creds(self):
        self.auth_user=self.bankdatabase.auth_user(self.user_name,self.user_password)
        
        if self.auth_user:
            self.show_homepage=UserSession(self.user_name,self.bankdatabase)
            self.show_homepage.show_dashboard()
        else:
            self.attempt_count+=1
            self.block_user(self.attempt_count)

            print("Please enter correct creds")

    def block_user(self):
        attempts=3
        
        if self.attemt_count > attempts:
            print("You Have Blocked for 24 hours") #block user for 24 hours
            #create a new data table for login and log out timings and checking user account status


    def Show_login_page(self): # Validation of len and multiple attempts are pending
        print(f"Welcome To SREE BANK OF INDIA\n")
        self.user_name=input("Please Enter Your User Name: ").strip().lower()
        self.user_password=getpass.getpass("Please Enter Your Password: ").strip()
        input("Press Enter To Continue")
        if(len(self.user_name)>5 and len(self.user_password)>7):
            self.auth_creds()
        else:
            print("Please Enter Vaild Username and Password")




if __name__=="__main__" :
    LoginPage().Show_login_page()