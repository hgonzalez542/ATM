# Name: Hector M Gonzalez
# Class: CompSci 230 ~ Lecture 02
# Instructor : Omar Rivera Morales
# Date: 10/14/2024


class ATM:
    def __init__(self): # Fixed account info for authentication
        self.account_number = "99999230"
        self.password = "0230"
        self.check_balance = 1000.00
        self.savings_balance = 1000.00
        self.transactions = []
        self.transaction_count = 0

    def authenticate_user(self): # Authentication Process
        for _ in range(3): # Range of times the user can try to input info before failure
            acc_num = input("Enter account number: ")
            pwd = input("Enter password: ")
            if acc_num == self.account_number and pwd == self.password:
                print("Authentication successful.")
                return True
            else:
                print("Invalid account number or password.")
        print("Maximum number of attempts reached.")
        return False

    def display_menu(self): # ATM Menu 
        print("\nATM Menu:")
        print("1. Make deposits")
        print("2. Make withdrawals")
        print("3. Make transfers")
        print("4. See balance")
        print("5. Exit")
        return input("Select an option (1-5): ")

    def process_menu(self, selection): # For UI purposes
        if selection == '1':
            self.deposit()
        elif selection == '2':
            self.withdrawal()
        elif selection == '3':
            self.transfer()
        elif selection == '4':
            self.balance()
        elif selection == '5':
            self.receipt()
            print("Exiting. Thank you for using the ATM Virtual Application!")
            return False
        return True

    def deposit(self): # Deposit Process ~ Checking or Savings
        account_type = input("Which account would you like to deposit into (check/savings)? ").strip().lower()
        amount = float(input("Enter deposit amount: "))
        if amount >= 0:
            if account_type == "check":
                self.check_balance += amount
                self.transaction_count += 1
                self.transactions.append((self.transaction_count, 1, amount))
            elif account_type == "savings":
                self.savings_balance += amount
                self.transaction_count += 1
                self.transactions.append((self.transaction_count, 2, amount))
            else:
                print("Invalid account type.")
        else:
            print("Deposit amount must be at least $0.00.")

    def withdrawal(self): # Withdrawal Process for either or acc
        account_type = input("Which account would you like to withdraw from (check/savings)? ").strip().lower()
        amount = float(input("Enter withdrawal amount: "))
        if amount >= 0 and amount <= 400:
            if account_type == "check" and self.check_balance >= amount:
                self.check_balance -= amount
                self.transaction_count += 1
                self.transactions.append((self.transaction_count, 1, amount))
            elif account_type == "savings" and self.savings_balance >= amount:
                self.savings_balance -= amount
                self.transaction_count += 1
                self.transactions.append((self.transaction_count, 2, amount))
            else:
                print("Insufficient funds or invalid account type.")
        else:
            print("Withdrawal amount must be between $0.00 and $400.00.")

    def transfer(self): # Transfer Process
        source_account = input("Which account  would you like to transfer from (check/savings)? ").strip().lower()
        dest_account = input("Which account to transfer to (check/savings)? ").strip().lower()
        
        if source_account == dest_account:
            print("Source and destination accounts must be different.")
            return
        
        amount = float(input("Enter transfer amount: "))
        if source_account == "check" and amount <= self.check_balance:
            self.check_balance -= amount
            if dest_account == "savings":
                self.savings_balance += amount
                self.transaction_count += 1
                self.transactions.append((self.transaction_count, 1, amount))  # Withdrawal
                self.transaction_count += 1
                self.transactions.append((self.transaction_count, 2, amount))  # Deposit
        elif source_account == "savings" and amount <= self.savings_balance:
            self.savings_balance -= amount
            if dest_account == "check":
                self.check_balance += amount
                self.transaction_count += 1
                self.transactions.append((self.transaction_count, 2, amount))  # Withdrawal
                self.transaction_count += 1
                self.transactions.append((self.transaction_count, 1, amount))  # Deposit
        else:
            print("Insufficient funds or invalid account type.")

    def balance(self):
        print(f"Check Balance: ${self.check_balance:.2f}")
        print(f"Savings Balance: ${self.savings_balance:.2f}")

    def receipt(self):
        print("\nTransaction Receipt:")
        print("TransactionNumber AccountType TransactionAmount")
        for transaction in self.transactions:
            print(f"{transaction[0]} {transaction[1]} {transaction[2]:.2f}")

    def run(self):
        if self.authenticate_user():
            while True:
                selection = self.display_menu()
                if not self.process_menu(selection):
                    break


if __name__ == "__main__":
    atm = ATM()
    atm.run()
