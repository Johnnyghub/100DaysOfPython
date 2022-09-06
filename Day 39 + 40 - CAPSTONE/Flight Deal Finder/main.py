from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from FlightClub.email_sender import EmailSender

data = DataManager().getData()
flight_search = FlightSearch()
notif_manager = NotificationManager()
email_sender = EmailSender()

ORIGIN_CITY_CODE = 'LON'  # london
ORIGIN_CITY = 'London'

for location in data['prices']:
    flight = flight_search.findLowestPrice(fly_from=ORIGIN_CITY_CODE, fly_to=location['iataCode'])
    try:
        if flight.price < location['lowestPrice']:
            for customer in email_sender.customers['customers']:
                message = f"Dear {customer['firstName']} {customer['lastName']},\n\n" \
                          f"Low Price Alert!\nOnly £{flight.price} to fly from {ORIGIN_CITY}-{ORIGIN_CITY_CODE} to " \
                          f"{flight.destination_city.title()}-{flight.destination_airport_code}, from {flight.out_date} to " \
                          f"{flight.return_date}. Book now!"
                notif_manager.sendMail(message=message, to_mail=customer['email'])
                print(message + '\n')  # local verification that condition was fulfilled
    except:
        pass  # in order to not crash the program because it returns a NoneType if no flight is found

