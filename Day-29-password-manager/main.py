from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD FINDER ------------------------------- #

def find_password():

    website = website_input.get()
    if len(website) == 0:
        messagebox.showinfo(message="please input the website name you want to search")
    else:
        try:
            with open("password.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="error", message="There is no data file found")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(message=f"{website} details are not found")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for n in range(randint(8, 10))]
    randon_symbols = [choice(symbols) for i in range(randint(2, 4))]
    randon_numbers = [choice(numbers) for k in range(randint(2, 4))]
    password_list = random_letters + randon_symbols + randon_numbers

    shuffle(password_list)

    password = "".join([char for char in password_list])

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_details():
    website = website_input.get()
    mail = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": mail,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Website or password can't be blank")
    else:

        is_ok = messagebox.askokcancel(title=f"{website}", message=f"Your mail is {mail}\n"
                                                           f"Please press ok to save the changes")
        if is_ok:

            try:
                with open("password.json", "r") as password_file:
                    # password_file.write(f"{website} | {mail} | {password}\n")
                    data = json.load(password_file)
            except FileNotFoundError:
                with open("password.json", "w") as password_file:
                    json.dump(new_data, password_file, indent=4)
            else:
                data.update(new_data)
                with open("password.json", "w") as password_file:
                    json.dump(data, password_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_reset_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_reset_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry()
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()
username_input = Entry()
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
username_input.insert(0, "sai@gmail.com")
password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")


generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=35, command=add_details)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()