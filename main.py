#########################################
# Made at https://discord.gg/E42nEXjGkx #
#########################################

import os

os.system('pip install requests colorama')
os.system('cls')

import threading
import requests
from colorama import init, Fore

init(autoreset=True)

b = r"""
    __  _____  ____  _______________ ____  ___    __  _____  _____________ 
   /  |/  / / / / / /_  __/  _/ ___// __ \/   |  /  |/  /  |/  / ____/ __ \
  / /|_/ / / / / /   / /  / / \__ \/ /_/ / /| | / /|_/ / /|_/ / __/ / /_/ /
 / /  / / /_/ / /___/ / _/ / ___/ / ____/ ___ |/ /  / / /  / / /___/ _, _/ 
/_/  /_/\____/_____/_/ /___//____/_/   /_/  |_/_/  /_/_/  /_/_____/_/ |_|
                            Made by SH_Dev
                             .gg/E42nEXjGkx                                                                   
"""

def loadwebhooks():
    with open("./config/webhooks.txt") as webhooks:
        return webhooks.read().splitlines()


def menu():
    webhooks = loadwebhooks()
    print(Fore.LIGHTMAGENTA_EX + b)
    msg = input(Fore.LIGHTMAGENTA_EX + "Message >> ")
    amt = int(input(Fore.LIGHTMAGENTA_EX + "Amount: "))

    json = {
        "username": "Multispammer", # you can change this if you want. ( from sh_dev )
        "content": msg
    }

    for i in range(amt):
        for webhook in webhooks:
            requests.post(webhook, json=json)
    print(Fore.LIGHTMAGENTA_EX + "| Done | Thanks for using our Tool! |")

menu()
