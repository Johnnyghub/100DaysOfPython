from smtplib import *

my_email = "johnnyscsgosmurf@hotmail.com"

with SMTP("smtp-mail.outlook.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password="throwAway2022")
    connection.sendmail(
        from_addr=my_email,
        to_addrs="theslayerxx1090@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
