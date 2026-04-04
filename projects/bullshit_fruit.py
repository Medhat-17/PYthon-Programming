print("welocme to the fruit shop!🍅 ")
print("1.Enter the shop")
print('2.leave')

user_choice = int(input("Enter your choice: "))
if user_choice==1: 
    print("welocme to the fruit shop!🍅 ")
    fruits = input("do you want to see the fruits? ")
    if fruits=="y".lower(): 
        print("the fruits are herE: ")
        print("1.🍌, 25$")
        print("2.🍇, 30$")
        print("3.🍎, 35$")
    #wan to buy 
    fruit_selection = input("enter your fruit name and price to buy it: ")
    if fruit_selection=="🍌" and "🍎" and "🍇":
        print(f"you have selected a fruit {fruit_selection} and the price is 34 $")
        #okay payment option 
        payment_method = input("enter your payment method (cash, card, mobile): ")
        if payment_method=="cash":
            print("you have selected cash as your payment method. please pay at the counter")
        elif payment_method=="card":
            print("you have selected card as your payment method. please swipe your card at the counter")
        elif payment_method=="mobile":
            print("you have selected mobile payment. please scan the QR code at the counter")
        else:
            print("invalid payment method. please select a valid payment method")


#buy stuff-> fruit 
#payment method 
#fruit -> any fruit with specififc price. 
