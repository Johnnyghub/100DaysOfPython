from requests import get
from pprint import pprint


class EmailSender:
    def __init__(self):
        self._CUSTOMER_ENDPOINT = "https://api.sheety.co/e05cec963399e42a3b96c83cde4dd2b4/flightDeals/customers"
        self._HEADERS = {
            "Authorization": "Bearer FWEAFERDFVERASGFVREDfcafgagfaga",
        }
        self.customers = self.getSheetyData()

    def getSheetyData(self, sheety_called: bool = False):
        """Gets all the data from the sheety and returns it as a variable"""
        if sheety_called:
            with get(url=self._CUSTOMER_ENDPOINT, headers=self._HEADERS) as response:
                response.raise_for_status()
                customer_data = response.json()
                pprint(customer_data)
                return customer_data
        else:  ## copy paste data from first runtime to save sheety API calls since it is limited
            return {'customers': [{'email': 'johnny@mail.com',
                                   'firstName': 'John',
                                   'id': 2,
                                   'lastName': 'Mo'},
                                  {'email': 'useran@mail.com',
                                   'firstName': 'User',
                                   'id': 3,
                                   'lastName': 'An'},
                                  {'email': 'joeys@mail.com',
                                   'firstName': 'Joey',
                                   'id': 4,
                                   'lastName': 'Cal'},
                                  {'email': 'ma@mail.com',
                                   'firstName': 'Manster',
                                   'id': 5,
                                   'lastName': 'Ma'}]}
