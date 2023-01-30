from rich import print
from rich.prompt import (Prompt, FloatPrompt)
from Bank import Bank_Account
from constants import OPTIONS, REQUEST, DEPOSIT, WITHDRAW, TRANSFER
from constants import CLIENTS
from Client import Client

CLIENT_NAMES = [client for client in CLIENTS]


def main():
    s = Bank_Account()

    while True:
        option = Prompt.ask("Escoge una opcion", choices=OPTIONS)
        if option == DEPOSIT:
            client_name = Prompt.ask("Cual es el nombre del cliente", choices=CLIENT_NAMES)
            amount = FloatPrompt.ask("Cual es la cantidad")
            s.deposit(client_name, int(amount))
        if option == WITHDRAW:
            client_name = Prompt.ask("Cual es el nombre del cliente", choices=CLIENT_NAMES)
            amount = FloatPrompt.ask("Cual es la cantidad")
            s.withdraw(client_name, int(amount))
        if option == REQUEST:
            s.display_clients()


if __name__ == "__main__":
    main()
