import smtplib
import datetime as dt
import random

my_email = "deepakjindal121@gmail.com"
password = "bylsodoqbtvnsmib"

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)


if day_of_week == 3:
    with open("quotes.txt") as f:
        file_contents = f.readlines()
        quote_of_the_day = random.choice(file_contents)

    message = f"Subject: Quote of the Day\n\n{quote_of_the_day}"

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pallvi.garg03@gmail.com",
            msg=message
        )