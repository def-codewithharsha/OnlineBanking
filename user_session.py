from bankdatabase import BankDataBase

class UserSession:

    def __init__(self,user_id:str,db:BankDataBase):
        self.bank_db = db
        self.user_id =user_id
        #self.bank_db.cursor.execute("select fname from user_acts where uname=?",[self.user_id])
        self.bank_db.excute("select fname from user_acts where uname=?",[self.user_id])
        self.user_fname=self.bank_db.fetchone()
        
    def get_balance(self,user_id):
        query=("select bal from user_acts where uname=?",[user_id])
        self.bank_db.excute(query)
        return self.bank_db.fetchone()
    

    def show_user_balance(self): #implement static or class method to update balance, add decorater to access 
        user_balance=self.get_balance(self.user_id)
        print(f"Your Account Balance is {user_balance} /- Rupees\n")
        input("Press enter for Dashboard")
        self.show_dashboard()
        

    def transfer_user_funds(self): #present lets update balance in future lets update transaction table as well
        user_balance=self.get_balance(self.user_id)

        print("Your Account Balance is {user_balance}/- rupees\n")
        send_amount=input("Enter Amount to send: ")

        if send_amount > user_balance or send_amount<0:
            print("Please Enter a Vaild Amount")

        recpient_account_number=input("\nPlease enter recepient account number : ")
        recpient_ifsc_code=input("\nEnter IFSC Code: ")

        user_confirmation=input("Press Yes to enter to confirm or No to cancel")

        query=("")


    def view_user_transactions():
        pass
    
    def user_logout():
        pass

    def show_dashboard(self):
        while True:

            print(f"welcome {self.user_fname[0]}\n Menu:\n") 

            print(f"1. View Account Balance\n2. Transfer Funds\n3. View Transaction History\n4. Logout\n")

            try :
                self.nav=input("Please select an option :").strip()
                match self.nav:
                    case "1":
                        break
            except :
                print("Please enter vaild Option")

        


