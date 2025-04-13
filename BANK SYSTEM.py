x=2000000000
#x is the balance 
while True:
 print('welcome')
 print("please choose what would you like to do")
 print("1.deposite money")
 print("2.withdraw money")
 print("3.check your account balance")
 print("4.logout")
 choice = input("please choose a number : ")
 if choice == "1":
        amount =float(input("please enter the amount you want to deposite:"))
        x+=amount
        print("your new balance is :" )
        print(x)
 elif choice == "2":
    amount =float(input("please enter the amount you want do withdraw :")) 
    if amount > x:
     print("Insufficient balance")
    else:    
     x-=amount
    print("your new balance is :" )
    print(x)
 elif choice == "3":    
     amout=x
     print("your account balance is :") 
     print(x) 
 elif choice == "4":
    print("YOU ARE ALL DONE") 
    break
 else:
    print("invalid choice'please try again'\n")    
       
        






