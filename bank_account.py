import random
user=[]
class Bank:
    def __init__(self,name,address,adhaar,balance):
        self.name=name
        self.address=address
        self.adhaar=adhaar
        self.balance=balance
        self.acc_no=random.randint(100,500)
    def display(self):
        print("...............")
        print("Account created:")
        print("Name:",self.name)
        print("Address:",self.address)
        print("Adhaar no:",str(self.adhaar))
        print("Account no:",str(self.acc_no))
        print("Current balance:",str(self.balance))
    def deposit(self):
        print("...............")
        print("Would you like to deposit to account",str(self.acc_no),"?")
        y=input(":")
        if(y=="yes"):
            depo=int(input("Enter the amount to be deposited:"))
            self.balance=self.balance+depo
            print("New balance:",str(self.balance))
    def withdraw(self):
        print("..............")
        print("Would you like to withdraw from account",str(self.acc_no),"?")
        x=input(":")
        if(x=="yes"):
            draw=int(input("Enter amount to be withdrawn:"))
            self.balance=self.balance-draw
            print("New balance:",str(self.balance))
    def transfer(self):
        print(".............")
        print("Would you like to transfer from account",self.name,"?")
        z=input(":")
        if(z=="yes"):
            rec=input("Enter recipient:")
            for n in range(5):
                if(self.name[n]==rec):
                    trans=int(input("Enter the money to be transferred:"))
                    self.balance[n]+=trans
                    self.balance[self.acc_no]-=trans
            
            
    
    
while True:
    user_name=input("Enter name:")
    user_address=input("Enter address:")
    user_adhaar=int(input("Enter adhaar no:"))
    user_balance=int(input("Enter balance:"))
    u=user.append(Bank(user_name,user_address,user_adhaar,user_balance))
    another=input("Would you like to enter another?:")
    if(another=="no"):
        break

for u1 in user:
    u1.display()
for u2 in user:
    u2.deposit()
for u3 in user:
    u3.withdraw()
for u4 in user:
    u4.transfer()
    

