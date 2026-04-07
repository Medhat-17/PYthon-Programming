import random 
lowesT_num = 1 
highest_num = 100 
answer  = random.randint(lowesT_num, highest_num)
guesses = 0 
is_running  = True 
print("Welcome to Number guessing game ")
print(f" select a number b/w {lowesT_num} and {highest_num}")


while is_running: 
    guess_number = input("Enter your guess: ")
    if guess_number.isdigit():
        guess_number = int(guess_number),
        guess_number+=1
        if guess_number<lowesT_num or guess_number > highest_num:
             print(f" please select a number b/w {lowesT_num} and {highest_num}" )
        elif guess_number < answer:
            print("too low try agian!")
        elif guess_number > answer: 
            print("too high! try again!")

    else: 
        print("invalid guess1")
        print(f" please select a number b/w {lowesT_num} and {highest_num}" )
