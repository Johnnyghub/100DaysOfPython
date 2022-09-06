class FlightData:
    def __init__(self, price, destination_airport_code, destination_city, origin_airport_code, origin_city, out_date, return_date):
        self.price = price
        self.destination_city = destination_city
        self.destination_airport_code = destination_airport_code  #IATA code
        self.origin_airport_code = origin_airport_code  #IATA code
        self.origin_city = origin_city
        self.out_date = out_date
        self.return_date = return_date
