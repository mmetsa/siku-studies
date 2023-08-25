from bank_account import BankAccount

my_bank_account = BankAccount("AB123", 0, "Aadu")
peedu_bank_account = BankAccount("AC321", 0, "Peedu")

my_bank_account.add_funds(1000)

my_bank_account.transfer(500, peedu_bank_account)

print(my_bank_account.get_statement())
print(peedu_bank_account.get_statement())

