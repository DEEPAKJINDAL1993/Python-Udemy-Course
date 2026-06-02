from tkinter import *
from tkinter import messagebox
import pyperclip
from password_generator import generate_password
FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please make sure to fill all fields")
    else:
        is_ok =  messagebox.askokcancel(title=website, message=f"Here are the details you entered:\n Website: {website}\n"
                                                      f" Username: {username}\n Password: {password}\n Do you want to save?")
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {username} | {password}\n")
                file.close()

            messagebox.showinfo("Saved Successfully", "Data saved successfully")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2,column=1,columnspan=2)
username_entry.insert(0,"deepakjindal121@gmai.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Buttons
generate_password_button = Button(width = 15,text='Generate Password',command=assign_password)
generate_password_button.grid(row=3,column=2)
add_password_button = Button(width=30,text='Add',command=save)
add_password_button.grid(row=4,column=1,columnspan=2,pady=5)


window.mainloop()