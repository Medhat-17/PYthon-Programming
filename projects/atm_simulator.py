print("1.Enter your card")
print("2.Select Money")
print("3.withdrawing Money")
print("4.checking balance")
print("5.exit")
user_choice = input("enter your choice! ")
if user_choice=="1":
    print("okay enter you have select the card option!")
    print("waiting....")
    card_number = int(input("Enter your four digit card number: "))
    if card_number >=4: 
        print(f"okay your card is approved {card_number}")
        print("okay waiting ")
        print("1.25$")
        print("2.50$")
        print("3.$100")
        print("4.$150")
        user_money_choice = input("enter amount or select! ")
        if user_money_choice=="1":
            print(f"okay you have select 25$")
            deposit_message= "you have successful made you depotsit!"
            print(f" your {deposit_message}")
        elif user_money_choice=="2":
            print("okayyou have select $50")
            deposit_message= "you have successful made you depotsit!"
            print(f" your {deposit_message}")
        elif user_money_choice=="3":
            print("you have select $100")
            deposit_message= "you have successful made you depotsit!"
            print(f" your {deposit_message}")



    else:
        print("your card is not approved yet!")
        quit()#break the bank and reutrn 


elif user_choice=="5":
    print('quiting ')
    quit()
    
