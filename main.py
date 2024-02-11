import click
import os
import json
import random
import string

from cryptography.fernet import Fernet
from dotenv import load_dotenv

def generate_password(length=12, use_digits=True, use_special_chars=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

def create_config_if_not_exists():
    if not os.path.isfile(".env"):
        key = Fernet.generate_key()
        key = key.decode("utf-8")
        with open(".env", "w") as f:
            f.write(f"key={key}")

def encode_password(password):
    key = os.getenv("key")
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(password.encode("utf-8"))
    
    return encoded_text.decode()

def decode_password(encoded_password):
    key = os.getenv("key")
    cipher_suite = Fernet(key)
    decoded_text = cipher_suite.decrypt(encoded_password)
    return decoded_text.decode("utf-8")

def checkFileExists():
    if not os.path.isfile("passwords.json"):
        with open('passwords.json', 'w') as fp:
            pass

def read_from_json():
    with open("passwords.json", "r") as f:
        data = json.load(f)
    return data

def write_to_json(dict_to_add):
    json_object = json.dumps(dict_to_add, indent=4)
    with open('passwords.json', 'w+') as fp:
        fp.write(json_object)

def create_new_password(account, user_name, password):
    checkFileExists()
    passwords = read_from_json()

    if account in passwords:
        return Exception("Account already exists. Please get the password or update the exisiting password \n")
    
    encoded_password = encode_password(password)

    new_dict = {
        "user_name": user_name,
        "password": encoded_password
    }

    passwords[account] = new_dict

    write_to_json(passwords)

def get_existing_password(account):
    passwords = read_from_json()
    if account not in passwords:
        raise Exception("Account doesn't exist, create a new password for this account \n")
    
    curr_account = passwords[account]
    username = curr_account["user_name"]
    password = curr_account["password"]

    password = decode_password(password)

    return username, password


@click.command()
@click.option('-g', '--generate', is_flag=True,help='Generate a new password of length 12 chars with symbols, letters and digits')
@click.option('-c', '--create',nargs=3, help='create a new entry with the following args account username password')
@click.option('-r', '--get',nargs=1, help='get an existing entry')
def main(create, get, generate):

    create_config_if_not_exists()
    load_dotenv()

    if create:
        try:
            create_new_password(*create)
            print("Successfully Added!")
        except Exception as e:
            print(e)
        except:
            print("Error adding the account, please try again later.")
    
    if get:
        try:
            user_name, password = get_existing_password(get)
            print(f"{user_name} {password}")
        except Exception as e:
            print(e)
        except:
            print("Error getting the password, please try again.")
    
    if generate:
        new_password = generate_password()
        print(new_password)


if __name__ == "__main__":
    main()
