from arsenal.dbconfig import dbconfig
import arsenal.aes
import pyperclip

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64

from rich import print as printc
from rich.console import Console
from rich.table import Table

#creating master key
def createMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
    return key


def extract_entries(mp, ds, search, decryptPassword = True):
    db = dbconfig()
    cursor = db.cursor()

    query = ""

    if len(search) == 0:
        query = "SELECT * FROM sb.entries"
        
    else:
        query = "SELECT * FROM sb.entries WHERE "
        for i in search:
            query += f"{i} = '{search[i]}' AND "  #takes the search params 
        query = query[:-5]                        #removes the ' AND " from last

    cursor.execute(query)
    results = cursor.fetchall()

    #no matches of the search 
    if len(results) == 0:
        printc("[yellow][-][/yellow] No results for the search")
        return 
    
    #creating a table if more than 1 pass is in search results or if user doesnt want decrypted pass
    if(decryptPassword and len(results)>1):
        table = Table(title = f"Results")
        table.add_column("Site Name")
        table.add_column("Email")
        table.add_column("Username")
        table.add_column("Password")
        
        for i in results:
            table.add_row(i[0],i[1],i[2],"{hidden}")
        console = Console()
        console.print(table)

        return
    
    #if only 1 result and user wants to decrypt
    if len(results)==1 and decryptPassword:
        master_key = createMasterKey(mp,ds)
        decrypted_pass = arsenal.aes.decrypt(key=master_key, source=results[0][3], keyType=bytes)

        #using pyperclip to copy the password to clipboard
        pyperclip.copy(decrypted_pass.decode())
        printc("[green][+][/green] Password copied to clipboard!")

    db.close()
