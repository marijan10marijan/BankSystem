## Creating Banking system using Python OOP

class User():
    def __init__(self,name,dob,gender):
        self.name = name
        self.dob = dob
        self.gender = gender
    
    def personal_info(self):
        return f'Account holder name: {self.name}. Date of birth: {self.dob}. Gender: {self.gender}'

class Bank(User):
    def __init__(self,name,dob,gender):
        super().__init__(name,dob,gender)
        self.balance = 0
        self.transaction = []
    
    def deposit(self, amount):
        self.amount = amount
        self.transaction.append(f'Balance: {self.balance} Deposit: {self.amount} ')
        self.balance += self.amount
        return f'Account owner: {self.name}.  You deposit: {self.amount} $.  Account balance: {self.balance} $ '

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            return f"You don't have enough money on account. Balance: {self.balance} $"
        else:
            self.transaction.append(f'Balance: {self.balance} Withdraw: {self.amount} ')
            self.balance -= self.amount
            return f'Account owner: {self.name}.  You withdraw: {self.amount} $.  Account balance: {self.balance} $ '

    def account_balance(self):
        return f'Account owner: {self.name}.  Balance: {self.balance}'

    def all_transactions(self):
        return f"List of all {self.name}'s transactions: {self.transaction}"


## Example of creating user, deposit and withdraw money, see account balance and all the transactions created 

b1 = Bank('Andrea','13.02.2000','F')
b1.deposit(2000)
b1.withdraw(800)
b1.deposit(1000)
print(b1.account_balance())
print(b1.all_transactions())
print(b1.withdraw(3000))


    