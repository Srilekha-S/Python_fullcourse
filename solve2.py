#Create a BankAccount class.

'''Requirements:

holder_name and balance → instance variables
bank_name = "SBI" → class variable
Create multiple accounts and print their details.

Question: If you change BankAccount.bank_name, what happens to all accounts?'''

class BankAccount:
    bank_name = "SBI"
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance
    def display_details(self):
        print(f"Holder Name: {self.holder_name}, Balance: {self.balance}, Bank Name: {self.bank_name}")
c1 = BankAccount("Alice", 1000)
c2 = BankAccount("Bob", 2000)
c1.display_details()  # Output: Holder Name: Alice, Balance: 1000, Bank Name: SBI
c2.display_details()  # Output: Holder Name: Bob, Balance: 2000