import unittest
from Bank import Bank_Account
from constants import CLIENTS
CLIENT_NAMES = [client for client in CLIENTS]
class TestBank(unittest.TestCase):
    #Estas son las pruebas que se tienen planeadas para revisar el funcionamiento de la herramienta

    def test_deposito(self):
        """Prueba que los depositos se hacen correctamente"""
        # Obten el saldo de una cuenta 
        # Manda a llamar la funcion de deposito
        # Llamar la funcion de revision de saldo
        # Comparar las cantidad
        s = Bank_Account()
        print(s.clients)
        client = s.get_client_by_name('marco')
        antes = client.get_balance()
        s.deposit(client.name, 200)
        despues = client.get_balance()
        self.assertEqual(antes+200, despues)

    def test_retiro(self):
        """Prueba que los retiros se hacen correctamente"""
        # Obten el saldo de una cuenta 
        # Manda a llamar la funcion de retiro
        # Llamar la funcion de revision de saldo
        # Comparar la cantidad
        s = Bank_Account()
        print(s.clients)
        client = s.get_client_by_name('marco')
        antes = client.get_balance()
        s.withdraw(client.name, 200)
        despues = client.get_balance()
        self.assertEqual(antes - 200, despues)

if __name__ == '__main__':
    unittest.main()