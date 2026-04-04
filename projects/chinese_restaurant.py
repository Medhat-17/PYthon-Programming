import time #used for simulating text
welcome = "欢迎来到中国店 🍵☕"
for char in welcome: 
    print(char, end="", flush=True)
    time.sleep(0.5)
print()#new line 
#user_input 
print("1.call the waiter")
print("2.checkout ")
print("3.exit")
print("4.Tip your choice!")
user_choice = input("Enter your choice? ")
if user_choice=="1": 
    waiter_coming =  "calling the waiter" 
    for x in waiter_coming: 
        print(x, end="", flush=True)
        time.sleep(0.5)
    print()
    waiter_greeting = input("welcome sir how are you? ")
    for xy in waiter_greeting: 
        print(xy, end="", flush=True)
        time.sleep(0.7) 
        greeting = ["fine", "good", "okay", "great"]
    if waiter_greeting in greeting: 
         print(f"okay sire you are {greeting}")#creating buggy cod. 
    else:
        print("bullshit bro!")
        
    user_choice2 = input('do you want to see the menu? ').lower().strip()
    if user_choice2=="menu": 
        print("okay showing the menu bro? ")
        menu = ["1.🍔 (25.0$)", "2.☕ (50$)", "2.🍕(27.9$)"]
        for x_iterating in menu: 
            time.sleep(0.10)
            print(x_iterating, end='', flush=True)
            print()

        user_menu_choice = input("select form above 👆 menu?")
        if user_menu_choice=="1":
            print(f"okay waiting to grab the first 🍔")
            checkout  = input("are you sure you want to buy a hamburger? ").lower().strip()
            if checkout=="yes":
                print("okay you got a hamburger 🍔")
            else:
                print("you cna;t get hamburger!")
elif user_choice=="2": 
    print("you have go the checkout option ")

elif user_choice=="4":
    quit() 
