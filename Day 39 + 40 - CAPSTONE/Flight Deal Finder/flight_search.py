from requests import get, post
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_API_KEY = "NnofK_XWJ7eWzPq0B2YxJY5gmFUPglUs"


class FlightSearch:
    def __init__(self):
        self._HEADERS = {
            "apikey": TEQUILA_API_KEY,
        }
        self._SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        self._LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

    def getIATACode(self, city_name):
        """Returns the IATA code when you pass in a city name."""
        search = {
            "term": city_name,
            "location_types": "city",
        }
        with get(url=self._LOCATION_ENDPOINT, headers=self._HEADERS, params=search) as response:
            response.raise_for_status()
            return response.json()["locations"][0]["code"]

    def findLowestPrice(self, fly_from, fly_to):
        query = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        with get(url=self._SEARCH_ENDPOINT, params=query, headers=self._HEADERS) as response:
            response.raise_for_status()
            try:
                data = response.json()["data"][0]  # we only need the cheapest flight
            except IndexError:
                return None
            except KeyError:
                return None

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport_code=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport_code=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
