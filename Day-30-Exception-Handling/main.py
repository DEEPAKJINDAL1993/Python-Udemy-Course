from re import search
from tkinter import *
from tkinter import messagebox
import json
import pyperclip
from password_generator import generate_password
FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "email" : username,
            "password" : password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please make sure to fill all fields")
    else:
        is_ok =  messagebox.askokcancel(title=website, message=f"Here are the details you entered:\n Website: {website}\n"
                                                      f" Username: {username}\n Password: {password}\n Do you want to save?")
        if is_ok:

            try:
                with open('data.json', 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file,indent=4)

            else:
                # Updating data
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                messagebox.showinfo("Saved Successfully", "Data saved successfully")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Oops", message="No data stored yet!")
    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(website, message= f"Email: {username}\nPassword: {password}")
        elif len(website) == 0:
            messagebox.showinfo("Oops", message=f"The website field is empty")
        else:
            messagebox.showinfo(website, message=f"No data found for {website}")

def assign_password():
    password = generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

# Icon canvas
canvas = Canvas(window,bg='white', width= 200,height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

# Labels
website_label = Label(text="Website:",anchor = 'center')
website_label.grid(row=1,column=0,pady=5)
username_label = Label(text="Email/Username:",anchor = 'center')
username_label.grid(row=2,column=0,pady=5)
password_label = Label(text="Password:",anchor = 'center')
password_label.grid(row=3,column=0,pady=5)

# Entries
website_entry = Entry(width=25)
website_entry.grid(row=1,column=1)
website_entry.focus()
username_entry = Entry(width=44)
username_entry.grid(row=2,column=1,columnspan=2)
username_entry.insert(0,"deepakjindal121@gmai.com")
password_entry = Entry(width=25)
password_entry.grid(row=3,column=1)

# Buttons
search_button = Button(width=15,text="Search",command=find_password)
search_button.grid(row=1,column=2)
generate_password_button = Button(width = 15,text='Generate Password',command=assign_password)
generate_password_button.grid(row=3,column=2)
add_password_button = Button(width=30,text='Add',command=save)
add_password_button.grid(row=4,column=1,columnspan=2,pady=5)

window.mainloop()