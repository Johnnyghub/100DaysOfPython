from smtplib import SMTP


class NotificationManager:
    def __init__(self):
        self._email = "johnnyscsgosmurf@hotmail.com"
        self._password = "throwAway2022"

    def sendMail(self, message, to_mail):
        with SMTP("smtp-mail.outlook.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self._email, password=self._password)
            connection.sendmail(
                from_addr=self._email,
                to_addrs=to_mail,
                msg=f"Subject:Cheap flight found!\n\n{message}".encode('utf-8', errors='ignore')
            )
