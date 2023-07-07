"""
Created on Sun Jul  2 14:05:03 2023

@author: tin
"""
MAX_LINES = 3 #get max 3 lines of a slot machine | constant value -> all capitalized
MAX_BET = 100
MIN_BET = 1

#collect user input (deposit amount)
def deposit():
    while True:
        amount = input("What would you like to deposit? Enter the amount: $") #string input
        if amount.isdigit(): #check whether the input amount is digit or not
            amount = int(amount) #convert into integer format
            if amount > 0: #check whether the amount is positive (greater than 0) or not
                break # stop the WHILE loop
            else:
                print("The amount must be greater than 0.") #inform user to enter a positive amount again
        else:
            print("Enter a number, please.") #inform user to enter a number again
    return amount #save the correct input into the "amount" variable

#get the number of bet lines
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1, 2 or " + str(MAX_LINES) +"): ") #get the input number of bet lines
        if lines.isdigit():
            lines = int(lines) #convert the number of lines into integer format
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("The number of lines must be between 1 and " + str(MAX_LINES) + ".")
        else:
            print("Please enter a number.")
    return lines

#get bet amount of each line
def get_bet():
    while True:
        bet = input("What would you like to bet for each line? Enter the amount: $") #string input
        if bet.isdigit(): #check whether the input amount is digit or not
            bet = int(bet) #convert into integer format
            if MIN_BET <= bet <= MAX_BET: #check whether the amount is positive (greater than 0) or not
                break # stop the WHILE loop
            else:
                print(f"The amount must be between ${MIN_BET} and ${MAX_BET}") #inform user to enter a positive amount again
        else:
            print("Enter a number, please.") #inform user to enter a number again
    return bet #save the correct input into the "amount" variable  
        

def main(): #so lazy to call a single function
    balance = deposit() #call the "deposit" function and save the input into "balance" variable
    lines = get_number_of_lines()
    bet = get_bet()
    print("The balance is:", balance)
    print("The number of bet lines is:", lines)
    print(f"The bet amount for each line is ${bet} for each line. Total bet amount is $", bet*lines)
    
main()
