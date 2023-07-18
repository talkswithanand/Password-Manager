from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def genearte_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    random_password = "".join(password_list)
    password_entry.insert(0, random_password)
    # It copies generate password and can directly paste to any website.
    pyperclip.copy(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all details.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered.\n"
                                                          f"Email: {email}\nPassword: {password}\n"
                                                          f"Is it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as new:
                new.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=280, height=280)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text= "Website: ")
website_label.grid(column=0, row=1, sticky="w")

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2, sticky="w")

email_entry = Entry(width=35)
email_entry.insert(0, "anand190900@gmail.com")
email_entry.grid(columnspan=2, column=1, row=2, sticky="w")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", command=genearte_password)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")






window.mainloop()