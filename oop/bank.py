'''# import itertools
from itertools import count
class Account:
    # we will be assinging the number as account number . it will be incremental
    # count start the number automatically from 0 so 
    count = count(start=1)
       #count = count()
    # print(count)
    def __init__(self,name,balance):
      #  account_number=next(self.count)

     #   account_number = 
       # self.    = account_number
        self.name = name
        self.balance = balance
       # self.account_number = account_number

        self.name = name
        self.balance = balance
        print("hi its me",name, ".your current balance is",balance)
my_account = Account(name = "nishan",balance=100)
your_account = Account(name = "ram",balance=200)
# print(my_account.account_number)
# print(your_account.account_number)
# print(your_account.count)
#print(my_account)'''



# just importing count to make initial phase of count
# from itertools import count
# class Account:
#     count = count()
#     def __init__(self,name,balance):
#         account_number = self.count
#         self.account_number = account_number
#         self.name = name
#         self.balance = balance
#         # you cannot return by {self.name}  and the balance is {self.balance}
#         print("hi","your name is",name,"and the current balance is",balance)

# my_balance = Account(name ="nishan",balance=10)
# your_balance = Account(name ="hari",balance=50)

# print(my_balance.account_number)
# print(your_balance.account_number)



from itertools import count
accounts = {}# it take the amount with reciver in key value pair 
class Account:
    count = count(start=0)
    def __init__(self,name,balance,pin):
        # just put next variable if one variable --> 0 && next variable point to be --> 1
        account_number = next(self.count)
        self.account_number = account_number
        self.name = name
        self.balance = balance
        # pin = int(input("enter the pin number:"))
        self.pin = pin 
        accounts[account_number]=self
        
        # you cannot return by {self.name}  and the balance is {self.balance}
        print(f"Good!{name} your account has been opened with amount {balance} only. and your pin number is {pin}. felt free to visit your nearest bank")

    def change_pin (self,old_pin,new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
        else:
            print("your old pin is invalid")
    def trasfer(self,pin,reciver_name,reciver_account,amount):
        if pin == self.pin:
               if accounts.get(reciver_account)!= None: #{key:value} dct.get(key) => key exists : values... if key doesnot exist none
                   if self.balance >= amount: 
                       reciver = accounts.get(reciver_account)
                       if reciver.name == reciver_name:
                           sender_new_balance = self.balance - amount
                           self.balance= sender_new_balance
                           reciver_new_balance = reciver.balance + amount
                           reciver.balance = reciver_new_balance
                           print(f"your transfer has been succesfull. your new balance is {self.balance}")
                       else:
                           print("the name and account number didnot match.")
                   else:
                     print("your balance is insufficient")
                     
               else:
                   print("sorry the reciver's account doesnot exist.")
                  
        else:
            print("your pin is incorrect. please try again!")
    # cheak if pin is correct
    # cheak if enough balance
    # cheak if reciver exist
    # cheak if reciver account number and name match 

    def __str__(self):  # str means string representation or display  in the string format 
        return f"Account No:{self.account_number}. Name {self.name}"
my_balance = Account(name ="nishan",balance=10,pin = 123)
your_balance = Account(name ="hari",balance=50,pin = 2345)
my_balance.trasfer(pin = 123,reciver_name="shyam",reciver_account=1,amount=5)
print("the reciver balance is",your_balance.balance)
# print(accounts)

# print(my_balance.account_number)
# print(your_balance.account_number)
# print(my_balance)
