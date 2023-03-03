from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Missing data", message="It seems that you have left some fields empty. Check again!")

    else:
        user_is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                      f"\nEmail: {email} "
                                                      f"\nPassword: {password} "
                                                      f"\nIs it ok to save?")
        if user_is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
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
generate_button = Button(text="Generate Password", width=15)
generate_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()