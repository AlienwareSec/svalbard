from getpass import getpass
import re
from rich import print as printc

def strength_checker():
    password = getpass("Please enter your password: ")
    flag = 0
    printc("[green][+][/green] Checking the Basic password policy checks")
    while True:
        if (len(password)<=12):
            flag =-1
            printc("[red][-][/red] Increase the length of your password")
            break
        elif not re.search("[a-z]", password):
            flag = -1
            printc("[red][-][/red] Include some lower-case characters in your password")
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            printc("[red][-][/red] Include some upper-case characters in your password")
            break
        elif not re.search("[0-9]", password):
            flag = -1
            printc("[red][-][/red] Include some numbers in your password")
            break
        elif not re.search("[_@$#%^&*!.:@]" , password):
            flag = -1
            printc("[red][-][/red] Include some symbols in your password")
            break
        elif not re.search("\s" , password):
            flag = -1
            printc("[red][-][/red] Try including some space in your password")
            break
        else:
            flag = 0
            printc("[green][+] Your password is strong and hard to bruteforce![/green]")
            break
    return flag,password