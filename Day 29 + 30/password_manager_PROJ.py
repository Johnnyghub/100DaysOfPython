from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generates a random password containing letters, numbers and symbols and then adds it to the password
    entry box. Also automatically adds the generated password to clipboard."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    generated_key = [choice(letters) for i in range(0, randint(9, 10))] + \
                    [choice(numbers) for j in range(0, randint(3, 4))] + \
                    [choice(symbols) for k in range(0, randint(5, 6))]

    shuffle(generated_key)
    key = ''.join(generated_key)

    copy(key)
    password.delete(0, END)  # just in case there is already text inside
    password.insert(END, key)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def savedata():
    """Verifies that all entries are populated, prompts the user to verify the entered details, and then saves the
    login to a txt file."""
    website_data = website.get()
    email_data = email.get()
    password_data = password.get()

    data_dict = {
        website_data: {
            "email": email_data, "password": password_data,
        }
    }

    if website_data == "" or email_data == "" or password_data == "":
        messagebox.showinfo(title="Empty Fields", message="Please do not leave any fields empty!")
    else:  # only if all the forms are populated
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(data_dict)
        except json.decoder.JSONDecodeError:
            with open("data.json", mode="w") as file:
                json.dump(data_dict, file, indent=4)  # for the first entry only
        except FileNotFoundError:
            with open("data.json", mode="w") as file:  # create file if it does not exist
                pass
        else:
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)

            password.delete(0, END)
            website.delete(0, END)

            messagebox.showinfo(title="Login Saved", message="Login has been saved to file.")


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_for_website():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", mode="w") as file:  # create file if it does not exist
            pass

    else:
        website_data = website.get()
        if website_data != "":
            try:
                messagebox.showinfo(title=f"Data for {website_data}", message=f"Email: {data[website_data]['email']}\n"
                                                                              f"Password: {data[website_data]['password']}")
            except KeyError:
                messagebox.showinfo(title="Not Found", message=f"A website with the name {website_data} was not found.\n"
                                                               "Keep in mind it is case sensitive.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website = Entry(width=32)
website.grid(row=1, column=1, sticky=E)
website.focus()

search_button = Button(text="Search", command=search_for_website, width=15)
search_button.grid(row=1, column=2, padx=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email = Entry(width=51)
email.insert(END, string="johnny@hotmail.com")  # my default email
email.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password = Entry(width=32)
password.grid(row=3, column=1, sticky=E)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, padx=5)

add_button = Button(text="Add", command=savedata, width=43)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
