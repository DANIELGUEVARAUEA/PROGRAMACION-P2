
# Definición 
balance = 0
interest_rate = 0.05

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

def calculate_interest():
    global balance, interest_rate
    interest = balance * interest_rate
    balance += interest

deposit(1000)
withdraw(500)
calculate_interest()

# Imprimir el saldo final
print("Balance (Traditional):", balance)
