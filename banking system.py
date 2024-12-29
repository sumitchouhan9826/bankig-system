import random

# Dictionary to store user data
bank_users = {}
transactions = {}

def add_user():
    """Function to add a new user to the banking system."""
    name = input("Enter Full Name: ")
    
    # Generate a 10-digit account number
    account_number = str(random.randint(10**9, 10**10 - 1))
    
    dob = input("Enter Date of Birth (DD/MM/YYYY): ")
    city = input("Enter City: ")
    password = input("Create a Password (min. 6 characters): ")
    while len(password) < 6:
        print("Password too short! Please try again.")
        password = input("Create a Password (min. 6 characters): ")
    
    balance = float(input("Enter Initial Deposit (minimum $100): "))
    while balance < 100:
        print("Minimum balance is $100. Please enter a valid amount.")
        balance = float(input("Enter Initial Deposit (minimum $100): "))
    
    contact_number = input("Enter Contact Number: ")
    email = input("Enter Email ID: ")
    address = input("Enter Address: ")

    # Store the user details in the dictionary
    bank_users[account_number] = {
        "Name": name,
        "Date of Birth": dob,
        "City": city,
        "Password": password,
        "Balance": balance,
        "Contact Number": contact_number,
        "Email": email,
        "Address": address
    }

    # Initialize transactions for the user
    transactions[account_number] = []

    print(f"\nUser added successfully! Account Number: {account_number}\n")
    return account_number


def show_users():
    """Function to display all users in the banking system."""
    if not bank_users:
        print("No users found in the system!")
        return

    print("\n=== List of Users ===")
    for account_number, details in bank_users.items():
        print(f"""
        Account Number: {account_number}
        Name          : {details['Name']}
        Date of Birth : {details['Date of Birth']}
        City          : {details['City']}
        Balance       : ${details['Balance']}
        Contact Number: {details['Contact Number']}
        Email         : {details['Email']}
        Address       : {details['Address']}
        """)


def login():
    """Function to handle user login."""
    account_number = input("Enter Account Number: ")
    password = input("Enter Password: ")

    if account_number in bank_users and bank_users[account_number]['Password'] == password:
        print("\nLogin Successful!\n")
        user_dashboard(account_number)
    else:
        print("Invalid Account Number or Password! Please try again.")


def user_dashboard(account_number):
    """Function for the user's dashboard after logging in."""
    while True:
        print(f"\nWelcome {bank_users[account_number]['Name']}")
        print("1. Show Balance")
        print("2. Show Transactions")
        print("3. Transfer Money")
        print("4. Credit Money")
        print("5. Debit Money")
        print("6. Update Contact Number")
        print("7. Change Password")
        print("8. Deactivate Account")
        print("9. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your current balance is: ${bank_users[account_number]['Balance']}")
        elif choice == "2":
            print("=== Transaction History ===")
            for transaction in transactions[account_number]:
                print(transaction)
        elif choice == "3":
            transfer_money(account_number)
        elif choice == "4":
            credit_money(account_number)
        elif choice == "5":
            debit_money(account_number)
        elif choice == "6":
            update_contact_number(account_number)
        elif choice == "7":
            change_password(account_number)
        elif choice == "8":
            deactivate_account(account_number)
            break
        elif choice == "9":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice! Please try again.")


def transfer_money(account_number):
    """Function to transfer money."""
    recipient_account = input("Enter recipient account number: ")
    if recipient_account not in bank_users:
        print("Recipient account not found!")
        return
    
    amount = float(input("Enter amount to transfer: "))
    if amount > bank_users[account_number]['Balance']:
        print("Insufficient balance!")
        return
    
    bank_users[account_number]['Balance'] -= amount
    bank_users[recipient_account]['Balance'] += amount

    transactions[account_number].append(f"Transferred ${amount} to {recipient_account}")
    transactions[recipient_account].append(f"Received ${amount} from {account_number}")

    print(f"Successfully transferred ${amount} to {recipient_account}!")


def credit_money(account_number):
    """Function to credit money to the user's account."""
    amount = float(input("Enter amount to credit: "))
    bank_users[account_number]['Balance'] += amount
    transactions[account_number].append(f"Credited ${amount} to account")
    print(f"${amount} credited successfully!")


def debit_money(account_number):
    """Function to debit money from the user's account."""
    amount = float(input("Enter amount to debit: "))
    if amount > bank_users[account_number]['Balance']:
        print("Insufficient balance!")
        return
    
    bank_users[account_number]['Balance'] -= amount
    transactions[account_number].append(f"Debited ${amount} from account")
    print(f"${amount} debited successfully!")


def update_contact_number(account_number):
    """Function to update contact number."""
    new_contact = input("Enter new contact number: ")
    bank_users[account_number]['Contact Number'] = new_contact
    print("Contact number updated successfully!")


def change_password(account_number):
    """Function to change the password."""
    new_password = input("Enter new password (min. 6 characters): ")
    while len(new_password) < 6:
        print("Password too short! Please try again.")
        new_password = input("Enter new password (min. 6 characters): ")
    
    bank_users[account_number]['Password'] = new_password
    print("Password changed successfully!")


def deactivate_account(account_number):
    """Function to deactivate the user's account."""
    confirm = input("Are you sure you want to deactivate your account? (yes/no): ").lower()
    if confirm == "yes":
        del bank_users[account_number]
        del transactions[account_number]
        print("Account deactivated successfully!")
    else:
        print("Account deactivation cancelled.")


# Main Program
if __name__ == "__main__":
    while True:
        print("\n=== Welcome to the Banking System ===")
        print("1. Add User")
        print("2. Show Users")
        print("3. Login")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            login()
        elif choice == "4":
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
