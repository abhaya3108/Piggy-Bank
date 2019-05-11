# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# piggy bank code
class PiggyBank:
    def __init__(self,balance):
        self.balance = balance
        
# function to add money to current balance
    def addMoney(self,money):
        print(" ")
        money = float(input("Add amount : "))
        print(" ")
        self.balance += money
        print("After adding,  your updated balance is " + str(self.balance) + " rupees")

# function to withdraw money from current amount
    def withdrawMoney(self,money):
        print(" ")
        money = float(input("Withdraw amount : "))
        print(" ")
        self.balance -= money
        print("After withdrawing, balance amount is " + str(self.balance) + " rupees")

# function to display current amount
    def currentMoney(self):
        print(" ")
        print("Your current balance is " + str(self.balance) + " rupees")
        
# main code
pigg = PiggyBank(1000)
print(" ")
print("--------------------Start-------------------")
while True:
    print(" ")
    user = input("Start or End : ")
    if user.strip() == "Start":
        controlPiggy = input("Add, Withdraw or Check : ")
        if controlPiggy.strip() == "Add":
            print(pigg.addMoney(500))
            continue
        elif controlPiggy.strip() == "Withdraw":
            print(pigg.withdrawMoney(200))
            continue
        elif controlPiggy.strip() == "Check":
            print(pigg.currentMoney())
            continue
        else :
            print(" ")
            print("Invalid Input.Try again")
            continue

    elif user.strip() == "End" :
        print(" ")
        print("------------Program Ended-----------")
        print(" ")
        break

    else :
        print(" ")
        print("Invalid Input. Try again")
        continue