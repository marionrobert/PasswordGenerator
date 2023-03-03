from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

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
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky="W")

# buttons
generate_button = Button(text="Generate Password", width=15)
generate_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()