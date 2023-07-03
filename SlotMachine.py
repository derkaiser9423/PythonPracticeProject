#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:05:03 2023

@author: tin
"""

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



balance = amount() #call the "deposit" function and save the input into "balance" variable
