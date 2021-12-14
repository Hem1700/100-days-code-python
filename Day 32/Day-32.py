# Email SMTP and Date Time
import datetime as dt
# import smtplib

# my_email = ""
# my_pass = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # Securing connection to the email server
#     connection.login(user=my_email, password=my_pass)
#     connection.sendmail(from_addr=my_email, to_addrs="learning1599@gmail.com",
#                         msg="Subject: Hello\n\nThis is the body of my email")



now = dt.datetime.now()
year = now.year
day_of_weak = now.weekday()
print(day_of_weak)
if year == 2021:
    print('Hello')

print(year)


date_of_birth = dt.datetime(year= 2000, month= 2, day= 17)
print(date_of_birth)