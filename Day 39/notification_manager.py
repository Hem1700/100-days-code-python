ACCOUNT_SID = 'AC90ea8a134dc896d037599c43b331c745'
AUTH_TOKEN = 'e80296aaad30a952d38f4ec0be676952'
PHONE_NUMBER  = '+13092206108'
from twilio.rest import Client
import smtplib

class NotificationManager:
    
    def __init__(self):
        self.client = Client("TWILIO_SID", 'TWILIO_AUTH_TOKEN')

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_='TWILIO_VIRTUAL_NUMBER',
            to='TWILIO_VERIFIED_NUMBER',
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP('EMAIL_PROVIDER_SMTP_ADDRESS') as connection:
            connection.starttls()
            connection.login('MY_EMAIL', 'MY_PASSWORD')
            for email in emails:
                connection.sendmail(
                    from_addr='MY_EMAIL',
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )