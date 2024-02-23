import os
import sys
import string
import random
import hashlib
import sys
from getpass import getpass
from rich import print as printc
from rich.console import Console

# from arsenal.dbconfig import dbconfig
from arsenal.dbconfig import dbconfig

console = Console()

def generatedevicesecret(length=12):
     return ''.join(random.choices(string.ascii_lowercase + string.digits, k = length))

def config():
    #creating a database
    db = dbconfig()
    cursor = db.cursor()

    printc("[green][+] Creating new config [/green]")
    
    try:
        cursor.execute("CREATE DATABASE sb")
    except Exception as e:
        printc("[red][!] An error occurred while trying to create db.")
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green][+][/green] Database 'sb' created")

    #Creating tables for master pass & other passwords
    query = "CREATE TABLE sb.secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'secrets' created")

    query = "CREATE TABLE sb.entries (sitename TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL)"    
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created")

    #asking master password 
    mp=" "
    while 1:
            mp = getpass("Choose a MASTER PASSWORD: ")
            if mp==getpass("Re-Type: ") and mp!="":
                break
            printc("[yellow][-] Passwords doesn't match, Please try again![/yellow]")

    #hashing the master password
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of MASTER PASSWORD ")

    #generating device secret
    ds = generatedevicesecret()
    printc("[green][+][/green] Device Secret generated")

    #adding master pass to database
    query = "INSERT INTO sb.secrets (masterkey_hash, device_secret) values (%s, %s)"
    val = (hashed_mp, ds)
    cursor.execute(query, val)
    db.commit()

    printc("[green][+][/green] Added to the database")
    printc("[green][+] All configurations done![/green]")
    db.close()

config()