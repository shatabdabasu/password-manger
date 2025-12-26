

from cryptography.fernet import Fernet

# 1. Generate the key just once and store it securely
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key) 
# 2. retriving the key
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter your master password:  ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def add(): 
    name = input("Enter the name of the website: ")
    pwd = input("Enter your password: ")
    with open('password.text','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode())# encryption
        pass

def view():
    with open('password.text','r') as f:
        for line in f.readlines():
            data=line.strip()
            name, tkn = data.split("|")
            print("Website:", name, "," "Password:", fer.decrypt(tkn.encode()).decode()) # decryption

while True:
    mode = input("  view esisting password or add new(view,add),press q to quit l ? : ").lower()
    if mode == "q":
        break
    elif mode == "v":
        view()
    elif mode == "a":
        add()
    else:
        print("invalid mode")
        continue