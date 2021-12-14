import smtplib
import datetime as dt
import random


now = dt.datetime.now()
day = now.weekday()
my_email = ""
my_pass = ""


if day == 0:
    with open('quotes.txt' , 'r') as file:
        context = list(file)
        random_quote = random.choice(context)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Securing connection to the email server
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="learning1599@gmail.com",
                            msg=f"Subject: Motivational Quote\n\n{random_quote}")
