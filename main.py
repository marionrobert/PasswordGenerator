from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_list = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for n in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for n in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Missing data", message="It seems that you have left some fields empty. Check again!")

    else:
        user_is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                      f"\nEmail: {email} "
                                                      f"\nPassword: {password} "
                                                      f"\nIs it ok to save?")
        if user_is_ok:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file)
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#  labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, padx=5, pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, padx=5, pady=5)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, padx=5, pady=5)

# entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "mrobert148@gmail.com")
password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky="W")

# buttons
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()