class Account:
    def __init__(self, bal):
        self.balance = bal

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Debited:", amount)
            print("Current Balance:", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Credited:", amount)
        print("Current Balance:", self.balance)

    def show_balance(self):
        print("Available Balance:", self.balance)


s1 = Account(10000)

while True:
    print("\n1. Debit")
    print("2. Credit")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = int(input("Enter amount to debit: "))
        s1.debit(amt)

    elif choice == 2:
        amt = int(input("Enter amount to credit: "))
        s1.credit(amt)

    elif choice == 3:
        s1.show_balance()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
