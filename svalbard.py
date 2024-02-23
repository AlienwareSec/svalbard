import argparse
from getpass import getpass
import hashlib
# import pyperclip
import re
import random
import string
import sys

from rich import print as printc
from rich.console import Console
from rich.prompt import Prompt
from rich.style import Style

console = Console()
import arsenal.add_entries as add_entries
import arsenal.extract_res
import arsenal.strength
from arsenal.dbconfig import dbconfig

parser = argparse.ArgumentParser(description='Description')
parser.add_argument('option', help='(s)trength/ (a)dd / (e)xtract')
parser.add_argument("-s", "--name", help="Site name")
parser.add_argument("-u", "--user", help="Username")
parser.add_argument("-e", "--mail", help="Email")
args = parser.parse_args()

# checking master password
def inputAndValidateMasterPassword():
	mp = getpass("\033[91m[!]\033[0m MASTER PASSWORD: ")
	hashed_mp = hashlib.sha256(mp.encode()).hexdigest()

	db = dbconfig()
	cursor = db.cursor()
	query = "SELECT * FROM sb.secrets"
	cursor.execute(query)
	result = cursor.fetchall()[0]
	if hashed_mp != result[0]:
		printc("[red][!] WRONG MasterPassword! [/red]")
		return None

	return [mp,result[1]]

def main():
    #if user asks to check the strength of the password
    if args.option in ["arsenal.strength", "s"]:
        flag,pwd = arsenal.strength.strength_checker()
        if flag == 0:
            add_pass = input("Do you want to add this Password to svalbard? (Y/N): ")
            if add_pass.lower() == 'y':
                site_name = input("\033[93m[!] Site name: \033[0m")
                email = input("\033[93m[!] Your E-mail: \033[0m")
                username = input("\033[93m[!] Username: \033[0m")
                add_entries.dataentry.password = pwd
                
                res = inputAndValidateMasterPassword()
                if res is not None:
                    add_entries.dataentry(res[0],res[1],site_name,email,username,pwd)
            else:
                print("Exiting!")
                sys.exit(0)
    #if user wants to add a password entry 
    if args.option in ["add","a"]:
        
        site_name = input("\033[93m[!] Site name: \033[0m")
        email = input("\033[93m[!] Your E-mail: \033[0m")
        username = input("\033[93m[!] Username: \033[0m")
        
        res = inputAndValidateMasterPassword()
        if res is not None:
            add_entries.dataentry(res[0],res[1],site_name,email,username)

    #if user calls for extraction 
    if args.option in ["extract","e"]:
        if args.name == None and args.mail == None and args.user == None:
         	# retrieve all
            printc("[red][!][/red] Please enter at least one search field (sitename/email/username)")
            return
        res = inputAndValidateMasterPassword()
        
        search = {}
        if args.name is not None:
            search["sitename"] = args.name
        if args.mail is not None:
            search["email"] = args.mail
        if args.user is not None:
            search["username"] = args.user

        if res is not None:
            arsenal.extract_res.extract_entries(res[0],res[1],search,decryptPassword = True)

main()





