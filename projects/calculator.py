import math 
print("Welcome to Calculator.py")
print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.DIV")
print("5.EXIT")
print("6.ADvanced Features")
#user choice 
user = int(input("Enter your choice:")) 
if user==1: 
    print("okay welcome to ADDition")
    num1 = int(input("enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"Result: {num1+num2}")
elif user==2: 
    print("okay welcome to SUBtraction")
    num1 = int(input("enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"Result: {num1-num2}")
elif user==3: 
    print("okay welcome to MULtiplication")
    num1 = int(input("enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"Result: {num1*num2}")
elif user==4: 
    print("okay welcome to DIVision")
    num1 = int(input("enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"Result: {num1/num2}")
elif user==5: 
    print("Exiting...")
    exit()
elif user==6:
    print("welcome to advanced Feature of calcutr ")
    print("1.Power")
    print("2.Maximum")
    print("3.Sqrt")
    print("4.Factorail")
    user_advanced = int(input("Enter your choice: ?"))
    if user_advanced==1:
        print("okay and welcome to advanced calcauotr: ")
        num1 = int(input("enter num1:"))
        num2 =int(input('enter num2: '))
        print(f"Result: {pow(num1,num2)}")
    elif user_advanced==2:
        print("okay and welcome to advanced calcauotr: ")
        num1 = int(input("enter num1:"))
        num2 =int(input('enter num2: '))
        print(f"Result: {max(num1,num2)}")
