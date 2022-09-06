from requests import get
from datetime import datetime
from smtplib import SMTP

MY_LAT = 25.68302095
MY_LNG = 55.77758789062501


def iss_is_above():
    global MY_LAT, MY_LNG
    response = get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_position = (float(data["iss_position"]["longitude"]), float(data["iss_position"]["latitude"]))

    if (iss_position[0]-5) <= MY_LAT <= (iss_position[0]+5) and (iss_position[1] - 5) <= MY_LNG <= (iss_position[1] + 5):
        return True
    else:
        return False


def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = ":".join(data["results"]["sunrise"].split("T")[1].split(":")[0:2])  #gets sunrise including minutes
    sunset = ":".join(data["results"]["sunset"].split("T")[1].split(":")[0:2])  #gets sunset including minutes

    if datetime.now().hour >= int(sunset[0:2]) or datetime.now().hour <= int(sunrise[0:2]):
        return True
    else:
        return False


if iss_is_above() and is_nighttime():  # if the iss is visible, send a notification email to myself
    my_email = "johnnyscsgosmurf@hotmail.com"

    with SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="throwAway2022")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="johnnyscsgosmurf@hotmail.com",
            msg="Subject:The ISS is currently visible!\n\nLook Up. The ISS is currently visible from your location,"
                " as it is nighttime and it is within 10 degrees of your current coordinates."
        )
