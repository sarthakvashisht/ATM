name = input("Name on your bank account? ")
balance = float(input("Your current balance? "))


def printMenu():
    print(name, "Welcome to the Bank")
    print("Enter 'b'(balance), 'd'(deposit), 'w'(withdraw), or'q'(quit)")


def getTransaction():
    transaction = str(input("What would you like to do? "))
    return transaction


def withdraw(bal, amt):
    global balance
    balance = bal - amt
    if balance < 0:
        balance = balance - 10


def formatCurrency(amt):
    return "$%.2f" % amt


###MAIN PROGRAM###

printMenu()
command = str(getTransaction())

while command != "q":
    if command == "b":
        print(name, "Your current balance is", formatCurrency(balance))
        printMenu()
        command = str(getTransaction())
    elif command == "d":
        amount = float(input("Amount to deposit? "))
        balance = balance + amount
        printMenu()
        command = str(getTransaction())
    elif command == "w":
        amount = float(input("Amount to withdraw? "))
        withdraw(balance, amount)
        printMenu()
        command = str(getTransaction())
    else:
        print("Incorrect command. Please try again.")
        printMenu()
        command = str(getTransaction())

print(name, "Goodbye! See you again soon")
