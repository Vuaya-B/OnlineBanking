import math
print("Welcome to the online banking application")


def signin():
    global name   # username
    global pin     # password
    global cb     # current balance

    name = str(input("Please create username: \n"))
    pin = str(input("Please create your 6 digits pin: \n"))

    while(len(pin) != 6):
         print("The pin has to be in 6 digits")
         pin = str(input("Please create your 6 digits pin: \n"))

    print("Thanks for creating your bank account")



def forgotPin():
     global pin
     recoverPin = str(input("To recover your pin, please create your new 6 digits pin: \n"))
     while(len(recoverPin) != 6):
         print("The pin has to be in 6 digits")
         recoverPin = str(input("Please create your 6 digits pin: \n"))

     print("The new pin has been restored")
     pin = recoverPin
     login()


def depositInterest(p,r,t):
     # A = Pe^(rt)
     p = float(p)
     r = float(r)
     t = float(t)
     e = math.exp(r*t)

     # calculation
     a = p * e # future value of your investment
     return a


def login():
     username = str(input("Please enter your username: \n"))
     user_pin = str(input("Please enter your pin: \n")) 

     if (username == name) and (user_pin == pin):
          print("Welcome to the online banking application" + " " + name)
          print("Please choose the menu down here")
          list_menu = ["1-Deposit","2-Withdraw", "3-Transfer", "4-Check Balance", "5-Deposit interest rate", "6-calculate compound interest"]
          for b in list_menu:
               print(b)

          choose = int(input("Please enter the number of your choice: \n"))
          d = 0    # deposit
          w = 0    # withdrawl
          cb = 0   # current balance
          
          match choose:
               case 1:
                    d  = int(input("Enter the amount to deposit:\n"))
                    cb = cb  + d
                    print("Your current balance is" + " " + str(cb))
                    exit()

               case 2:
                    w  = int(input("Enter the amount of money to withdraw:\n"))
                    if w>cb:
                         print("Your current balance is not sufficient for this transaction")
                         login()
                    else:
                         cb = cb - w
                         print(str(w) + " " + "has been withdrawn from your account" + " " + "and your current balance is" +" "+ str(cb))
                         exit()
               case 3:
                    dest = str(input("Please enter the account number of your destination in 8 digits: \n"))
                    if len(dest) == 8:
                         amount = int(input("Please enter the amount you want to transfer:\n"))
                         if amount>cb:
                              print("Your current balance is not sufficient for this transaction")
                              login()
                         else:
                              cb = cb - amount 
                              print("The transaction of" + " "+ str(amount)+ " "+ "has been transferred to"+ " "+ str(dest)+ " "+ " your current balance is" + str(cb))
                              exit()
                    else:
                         print("The transaction has been rejected since the destination account number is invalid")
                         login()

               case 4:
                    print("Your current balance is " + " " + str(cb))
                    exit()

               case 5:
                    if d>50000:
                         rate = 3
                    elif d >30000:
                         rate = 2
                    else:
                         rate = 1.5
                    
                    print("Your current deposit  interest rate is" + " "+ str(rate) + " %")
                    exit()

               case 6:
                    option = ["1-Calculate your deposit compound insterest based on your current balance", "2-Calculate your deposit compound insterest based on your input deposit"]
                    for o in option:
                         print(o)
                    opt = int(input("Please enter your choice from the options above\n"))

                    if opt == 1:
                         timing= str(input("How many years do you want to invest your money?\n"))
                         if d>50000:
                            ratex = 3/100
                         elif d >30000:
                            ratex = 2/100
                         else:
                            ratex = 1.5/100

                         print("Your current balance in" + " " + timing + " "+" years will be")
                         print(depositInterest(cb,ratex, timing))
                         exit()

                    elif opt == 2:
                         timing= str(input("How many years do you want to invest your money?\n"))
                         money = int(input("Enter the amount of money you would like to deposit:\n"))
                         if d>50000:
                            ratex = 3/100
                         elif d >30000:
                            ratex = 2/100
                         else:
                            ratex = 1.5/100

                         print("Your current balance in" + " " + timing + " "+" years will be")
                         print(depositInterest(money,ratex, timing))
                         exit()
                    else:
                         print("Option is not available, back to main menu")
                         login()

               case _:
                    print("Choose one of the options above")
                    exit()
     else:
          print("Either your username or pin is incorrect, did you create your account?")
          list1 = ["1-yes", "2-no"]
          for i in list1:
               print(i)
          inp = int(input("Enter your choice below:\n"))

          if inp == 1:
               list2 = ["1-Do you want to attempt to login again?", "2-Did you forget your pin?"]
               for t in list2:
                    print(t)
               inp_1 = int(input("Please enter your choice below:\n"))

               if inp_1 == 1:
                    login()
               elif inp_1 == 2:
                    forgotPin()
               else:
                    print("Option is not available")
                    login()

          elif inp == 2:
               print("Please create your account first")
               signin()

def main_menu():
     option_one =int(input("Choose 1 to sign in and 2 to log in \n"))

     if option_one == 1:
          signin()
     elif option_one == 2:
          login()
     else:
          print("Option is not available")
          main_menu()
     exit()

def exit():
     ans = (str(input("Do you still want to conduct transactions? yes or no \n"))).lower()

     if ans == "yes":
          login()
     elif ans == "no":
          print("Thank you for using this app")
     else:
          print("Option is not available")
          main_menu()
          
          

main_menu()
     

# signin()
# forgotPin()
# print(depositInterest(1000, 0.038,6))