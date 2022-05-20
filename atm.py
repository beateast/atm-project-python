from msilib.schema import Class


class Atm(object):
    def __init__(my, withdraw, balance, debit):

        my.withdraw = withdraw

        my.balance = balance

        my.debit = debit


atm = Atm("500", "5000", "0")
print(atm.balance)


        



    
