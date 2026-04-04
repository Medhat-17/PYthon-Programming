
#created a phonebook recorder.
contacts = [] #empty list 

while True: 
    name = input("enter your name? ")
    phone = input("Phone: ")
    contacts.append([name, phone])#2d list 

    more  = input("ADD more (y/n): ")
    if more=="n": 
        break 

for x in contacts: 
    print(["name", x[0], "phone: ", x[1]])
