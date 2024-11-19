# Deacon Steiner    
# UWYO COSC 1010
# 11/19/24
# Lab 10
# Lab Section: 11
# Sources, people worked with, help given to: 

#import modules you will need 
from pathlib import Path
from hashlib import sha256 

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

hash_file = Path("/home/deacon/cosc-1010/repos/lab-10-DeaconSteiner-class/hash")

try:
    password_to_crack = hash_file.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"{hash_file} not found")
else:

    dump_file = Path("/home/deacon/cosc-1010/repos/lab-10-DeaconSteiner-class/rockyou.txt")

    try: 
        passwords_to_test = dump_file.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"{dump_file} not found")
    else:
        
        lines = passwords_to_test.splitlines()

        for line in lines:
            hashed_pass = get_hash(line)
            
            if hashed_pass == password_to_crack:
                print(f"The password is: {line}")
                
            else:
                continue
        
    
    
