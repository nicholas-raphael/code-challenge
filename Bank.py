# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
from constants import CLIENTS
from Client import Client


class Bank_Account:
    def __init__(self, clients=CLIENTS):
        # self.clients = [Client(c['name']) for c in clients]
        self.clients = {k: Client(k, v['balance']) for k, v in clients.items()}
        # print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def get_client_by_name(self, client_name):
        return self.clients[client_name]

    def deposit(self, client_name, amount: int):
        if not isinstance(amount, int):
            raise TypeError('Cantidad no valida')
        self.clients[client_name].update_balance('DEPOSIT', amount)

    def withdraw(self, client_name, amount: int):
        if not isinstance(amount, int):
            raise TypeError('Cantidad no valida')
        self.clients[client_name].update_balance('WITHDRAW', amount)

    def display_clients(self):
        for k, v in self.clients.items():
            print("\n Usuario: ", k, "Balance: ", v.balance)
