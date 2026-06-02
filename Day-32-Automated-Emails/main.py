##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd
import os
import random

now = dt.datetime.now()
day = now.day
month = now.month
today = (now.month,now.day)

my_email = ""
password = ""


letter_templates_folder = "letter_templates"

birthdays_df = pd.read_csv("birthdays.csv")
today_bday_df = birthdays_df[(birthdays_df['month'] == month) & (birthdays_df['day'] == day)]

# Alternate solution
# birthday_dict = {(row["month"],row["day"]): row for (index,row) in birthdays_df.iterrows()}
# print(birthday_dict)

if len(today_bday_df) < 0:
    for name,email in zip(today_bday_df['name'],today_bday_df['email']):

        files = [f for f in os.listdir(letter_templates_folder) if os.path.isfile(os.path.join(letter_templates_folder,f))]
        random_template = os.path.join(letter_templates_folder,random.choice(files))

        with open(random_template, 'r', encoding='utf-8') as f:
            content = f.read()
            updated_content = content.replace('[NAME]', name)

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{updated_content}"
            )





