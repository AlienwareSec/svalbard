from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from rich import print as printc

import arsenal.aes
from arsenal.dbconfig import dbconfig

#creating master key
def createMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
    return key

def dataentry(mp, ds, sitename, email, username, password=None):
    if password is None:
        # Prompt for password input
        password = getpass("\033[93m[!] Password: \033[0m")

    master_key = createMasterKey(mp, ds)
    encrypted_pass = arsenal.aes.encrypt(key=master_key, source=password, keyType=bytes)

    #adding entries to database
    db = dbconfig()
    cursor = db.cursor()
    query = "INSERT INTO sb.entries (sitename, email, username, password) values (%s, %s, %s, %s)"
    val = (sitename, email, username, encrypted_pass)
    cursor.execute(query, val)
    db.commit()

    printc("[green][+][/green] Added entry")