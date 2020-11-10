from Projet_Python import Car
from Projet_Python import Clients

class Concessionnaire :

    def __init__(self, car, client, price):

        self.car = {}
        self.client = {}
        self.price = price


if __name__ == "__main__":

    set_concession = Concessionnaire()
    set_car = Car()
    create_client_info = Clients()