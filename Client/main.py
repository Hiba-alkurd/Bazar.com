import argparse

import os
import sys
import requests

exit = "/exit"
help = "/help"
search = "search"
info = "info"
purchase = "search"

def searchBycatagory(catagory):
    r = requests.get('https://api.github.com/events')
    print("Hello from a function")

def infobynumber(number):
    print("Hello from a function")

def purchasebynumber(number):
    print("item bought")

commandslist = ["search {catagory}", "info {item_num}", "purchase {item_num}", ""]

print("\n Welcome to Bazar.com! \n")
print("\n What would you like to do? (use /help for commands list) ")
print("(use /exit to exit) \n")

Userinput = ""
while (Userinput != exit) :
    Userinput = input("> ")

    if Userinput == help :
        for x in commandslist :
            print("> # "+x+"\n")
    elif len(Userinput.split) != 2 :
        print("> invalid command")
    else :
        command = Userinput.split
        if command[0] == search:
            searchBycatagory(command[1])

        elif (command[0] == info and command[1].isnumeric()) :
            infobynumber(int(command[1]))

        elif (command[0] == purchase and command[1].isnumeric()) :
            purchasebynumber(int(command[1]))

        else :
            print("> invalid command")


print("Hope You Enjoyed Your Shopping!")
