# Automated Birthday Wisher

import datetime as dt
import smtplib
import pandas
import random

my_email = ""
my_pass = ""
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv('birthdays.csv')
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter:
        contents = letter.read()
        new_letter = contents.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Securing connection to the email server
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person['email'],
                            msg=f"Subject: Happy Birthday\n\n{new_letter}")
