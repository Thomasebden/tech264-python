# Mini Password Manager

# Dictionary to store users and their passwords
users_db = {}

# Dictionary to store accounts and their associated passwords
account_db = {}


# Function to add a new user to the password manager
def add_user():
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists.")
    else:
        password = input("Enter a password: ")
        users_db[username] = password
        print(f"User '{username}' added successfully!")


# Function to login as a user
def login():
    username = input("Enter your username: ")
    if username not in users_db:
        print("Username not found.")
        return None
    password = input("Enter your password: ")
    if users_db[username] == password:
        print("Login successful!")
        return username
    else:
        print("Incorrect password.")
        return None


# Function to add an account to the password manager
def add_account(username):
    account_name = input("Enter the account name (e.g., Facebook, Email): ")
    account_password = input(f"Enter the password for {account_name}: ")
    account_db[username][account_name] = account_password
    print(f"Account for {account_name} added successfully!")


# Function to retrieve a stored password
def retrieve_password(username):
    account_name = input("Enter the account name: ")
    if account_name in account_db[username]:
        print(f"The password for {account_name} is: {account_db[username][account_name]}")
    else:
        print("Account not found.")


# Function to change an account's password
def change_password(username):
    account_name = input("Enter the account name to change the password: ")
    if account_name in account_db[username]:
        old_password = input("Enter your current password: ")
        if old_password == account_db[username][account_name]:
            new_password = input("Enter the new password: ")
            account_db[username][account_name] = new_password
            print(f"Password for {account_name} has been changed.")
        else:
            print("Incorrect password.")
    else:
        print("Account not found.")


# Main function to interact with the password manager
def main():
    while True:
        print("\n1. Add User")
        print("2. Login")
        print("3. Add Account")
        print("4. Retrieve Account Password")
        print("5. Change Account Password")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            username = login()
            if username:
                # Initialize the user's account data if logging in
                if username not in account_db:
                    account_db[username] = {}
                # Perform additional actions after successful login
                while True:
                    print("\n1. Add Account")
                    print("2. Retrieve Account Password")
                    print("3. Change Account Password")
                    print("4. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        add_account(username)
                    elif sub_choice == "2":
                        retrieve_password(username)
                    elif sub_choice == "3":
                        change_password(username)
                    elif sub_choice == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


# Run the password manager
if __name__ == "__main__":
    main()
