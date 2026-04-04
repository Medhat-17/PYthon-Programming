question  =0 

print("welcome to the Quiz Show: ")
ready=input("Are you Ready? Y/N ")
if ready=="y".lower(): 
    print("let's start hte show1")
    q1 = input("who was in the show of KBC?")
    if q1=="amitabh".lower().strip(): 
        print("correct!")
        question += 1
    q2 = input("what does RAM stands for? ")
    if q2=="random access memory".lower().strip(): 
        print("correct!")
        question += 1
    print("Enter your answer for question 3:")
    q3 = input("what was the first programming language ?")
    if q3=="fortran".lower().strip(): 
        print("correct!")
        question += 1
print(f"you scored {question} out of 3")