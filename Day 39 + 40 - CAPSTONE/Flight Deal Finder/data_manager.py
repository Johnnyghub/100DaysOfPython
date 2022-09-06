from requests import get, put
from pprint import pprint
from flight_search import FlightSearch


class DataManager:
    """This class contains a privatized variable containing the sheety data and a get method for security"""

    def __init__(self):
        self._SHEET_ENDPOINT = "https://api.sheety.co/e05cec963399e42a3b96c83cde4dd2b4/flightDeals/prices"
        self._HEADERS = {
            "Authorization": "Bearer FWEAFERDFVERASGFVREDfcafgagfaga",
        }
        self._data = self.getSheetyData()

    def getSheetyData(self, sheety_called: bool = False):
        """Gets all the data from the sheety and returns it as a variable"""
        if sheety_called:
            with get(url=self._SHEET_ENDPOINT, headers=self._HEADERS) as response:
                response.raise_for_status()
                sheetydata = response.json()
                pprint(sheetydata)
        else:  ## copy paste data from first runtime to save sheety API calls since it is limited
            sheetydata = {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
                                     {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42},
                                     {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485},
                                     {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 551},
                                     {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95},
                                     {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414},
                                     {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240},
                                     {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260},
                                     {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 378}]}

        return sheetydata

    def getData(self):
        return self._data

    def updateSheety(self):
        """Updates the IATA codes of all row, call this only when you add rows to your google sheet to update the data"""
        flight_search = FlightSearch()
        for row in self._data['prices']:
            PUT_ENDPOINT = f"https://api.sheety.co/e05cec963399e42a3b96c83cde4dd2b4/flightDeals/prices/{row['id']}"
            body = {
                "price": {
                    'iataCode': flight_search.getIATACode(city_name=row['city']),
                }
            }
            with put(url=PUT_ENDPOINT, json=body, headers=self._HEADERS) as response:
                response.raise_for_status()
