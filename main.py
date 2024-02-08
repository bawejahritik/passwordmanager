passwords = {}

def create_new_password(account, user_name, password):
    if account in passwords:
        raise Exception("Account already exists. Please get the password or update the exisiting password \n")
    
    new_dict = {
        "user_name": user_name,
        "password": password
    }

    passwords[account] = new_dict

def get_existing_password(account):
    if account not in passwords:
        raise Exception("Account doesn't exist, create a new password for this account \n")
    
    curr_account = passwords[account]
    username = curr_account["user_name"]
    password = curr_account["password"]

    return username, password

if __name__ == "__main__":
    option = int(input(f"Press 1 to add a password \nPress 2 to get an existing password \nPress 3 to exit the program \n"))

    while option != 3:
        if option == 1:
            account = input("Enter the account: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            try:
                create_new_password(account, username, password)
                print("Successful")
            except Exception as e:
                print(e)
            except:
                print("Failed. Please try later!")

        elif option == 2:
            account = input("Enter the account: ")
            try:
                username, password = get_existing_password(account)
                print(f"Username: {username} \nPassword: {password} \n\n")
            except Exception as e:
                print(e)
            except:
                print(f"Failed to retrieve the username and password for {account}")
        
        option = int(input(f"Press 1 to add a password \nPress 2 to get an existing password \nPress 3 to exit the program \n"))
