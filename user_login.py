from bankdatabase import BankDataBase
from user_session import UserSession
import getpass



class LoginPage:
    ATTEMPTS=3

    def __init__(self):
        self.bankdatabase = BankDataBase()
        self.attempt_count=0
        
    def auth_creds(self):
        #self.auth_username thinklogic for check username based wrong tries
        self.auth_user=self.bankdatabase.auth_user(self.username,self.user_password)
        
        if self.auth_user:
            self.show_homepage=UserSession(self.username,self.bankdatabase)
            self.show_homepage.show_dashboard()
        else:
            self.failed_attempt+=1
            self.block_user(self.attempt_count)
            print("Please enter correct creds")

    def block_user(self):
        attempts=3
        if self.failed_count > attempts:
            print("You Have Blocked for 24 hours") #block user for 24 hours
            #create a new data table for login and log out timings and checking user account status


    def Show_login_page(self): # Validation of len and multiple attempts are pending
        while True:
            print(f"Welcome To SREE BANK OF INDIA\n")
            self.username=input("Please Enter Your Username: ").strip().lower()
            self.user_password=getpass.getpass("Please Enter Your Password: ").strip()
            input("Press Enter To Continue")
            if(len(self.username)>5 and len(self.user_password)>7):
                self.auth_creds()
            else:
                print("Please Enter Vaild Username and Password")




if __name__=="__main__" :
    LoginPage().Show_login_page()