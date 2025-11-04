#from bankdatabase import BankDataBase

class UserSession:

    def __init__(self,user_id:str,db:BankDataBase):
        self.bank_db = db
        self.user_id =user_id
        #self.bank_db.cursor.execute("select fname from user_acts where uname=?",[self.user_id])
        self.bank_db.excute("select fname from user_acts where uname=?",[self.user_id])
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
                self.nav=input("Please select an option :").strip()
                match self.nav:
                    case "1":
                        break
            except :
                print("Please enter vaild Option")

        


