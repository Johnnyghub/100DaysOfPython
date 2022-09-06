from smtplib import SMTP
from pandas import read_csv
from datetime import datetime as date
from random import randint

MY_EMAIL = "johnnyscsgosmurf@hotmail.com"

bdays = read_csv('birthdays.csv').to_dict('records')  # create dict of all bdays

for bday in bdays:
    if date.now().month == bday['month']:
        if date.now().day == bday['day']:  # we only need to check against day and month
            with open(file=f"letter_templates/letter_{randint(1, 3)}.txt", mode='r') as file:
                letter = file.read().replace('[NAME]', bday['name'])

                with SMTP("smtp-mail.outlook.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password="throwAway2022")
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=bday['email'],
                        msg=f"Subject:Happy Birthday!!!\n\n{letter}"
                    )
