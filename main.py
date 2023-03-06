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


# ---------------------------- SEARCH PASSWORD FOR WEBSITE ------------------------------- #
def search_password():
    website = website_input.get().capitalize()
    try:
        with open("data.json", "r") as previous_file:
            previous_data = json.load(previous_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"No information recorded ",
                            message="You have not yet saved any data with our program. Try it")
    else:
        try:
            website_data = previous_data[website]
        except KeyError:
            messagebox.showinfo(title=f"No data for {website}'s website ",
                                message=f"No details registered for the website: {website}."
                                        f"\nEnter an email and a password then register it")
        else:
            messagebox.showinfo(title=f"Data for {website}'s website ",
                                message="These are the details previously registered: "
                                        f"\nEmail: {website_data['email']}"
                                        f"\nPassword: {website_data['password']}")


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
            try:
                with open("data.json", "r") as previous_file:
                    # reading ald data
                    previous_data = json.load(previous_file)
            except FileNotFoundError as error_message:
                # create the file bcs it doesn't exit and writing data inside
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # everything went well, the program can go on, after line 48
                # updating ald data with new data (not appending) --> inside the same dictionary
                previous_data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(previous_data, data_file, indent=4)
            finally:
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
website_input = Entry(width=32)
website_input.grid(row=1, column=1, sticky="W")
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "mrobert148@gmail.com")
password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky="W")

# buttons
search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2, sticky="E")
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()