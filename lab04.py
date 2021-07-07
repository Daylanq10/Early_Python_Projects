########################################################################
##
## CS 101 Lab
## Program #4
## Daylan Quinn
## drq9q7@mail.umkc.edu
##
## PROBLEM : Ask a user for input that describes a certain number, calculate the
##          remainders, output the number the user had in mind
##
## ALGORITHM : 
##      1. Loop for continuity
##      2. Tell user to think of number
##      3. Ask for reminders when modulus 3, 5, and 7
##      4. Calculate number that matches modulus's given
##      5. Output number
## 
## ERROR HANDLING:
##      Should be handled to take all invalid inputs
##
## OTHER COMMENTS:
##      Thank you for helping with the number thing is makes sense
##
########################################################################


#TO ALLOW REPLAY OR QUIT
def play():
    play = input("Do you want to play again? Y to continue, N to quit --> ")
    while True:
            
        if (play == 'Y') or (play == 'y'):
            play = True
            return play
        if (play == 'N') or (play == 'n'):
            play = False
            return play
        else:
            play = input("Invalid input. Enter 'Y' or 'N'")
    

#ENSURES A NUMBER VALUE HAS BEEN ENTERED
def remain_int(num):
    while True:
        try:
            num = int(num)
            return num
        except:
            num = input("Input must be a number")


#MAIN     
again = True
while again == True:

    print("Welcome to the Flarsheim Guesser!\n")
    print("Please think of a number between and including 1 and 100\n")

    while True:
        rem_1 = remain_int(input("What is the remainder when your number is divided by 3? --> "))
        if rem_1 >= 3:
            print("Must be less than 3")
        elif rem_1 < 0:
            print("Must be 0 or greater")
        else:
            break


    while True:
        rem_2 = remain_int(input("What is the remainder when your number is divided by 5? --> "))
        if rem_2 >= 5:
            print("Must be less than 5")
        elif rem_2 < 0:
            print("Must be 0 or greater")
        else:
            break


    while True:
        rem_3 = remain_int(input("What is the remainder when your number is divided by 7? --> "))
        if rem_3 >= 7:
            print("Must be less than 7")
        elif rem_3 < 0:
            print("Must be 0 or greater")
        else:
            break
    

    for i in range(0, 101):
        if (i % 3 == rem_1) and (i % 5 == rem_2) and (i % 7 == rem_3):
            print("Your number is -- > ", i)


    again = play()
    
        
    
        
