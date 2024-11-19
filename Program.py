from pathlib import Path
from hashlib import sha256 

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

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