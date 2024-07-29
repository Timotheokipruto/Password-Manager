from tkinter import *
from tkinter import messagebox
import random
# import pyperclip #for copying and pasting to clipboard
import json

LABEL_FONT =( "Courier", 10, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    
    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)

   

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()

    new_dict = {website: 
                {"email": email, 
                 "password": password
                 }}
    
    def dump_json(data):
        with open("passwords.json","w") as password_file:
            json.dump(data, password_file, indent=4)

          

    if website =="" or len(password) == 0:
        messagebox.showinfo(title="Empty Field(s)",message="One of more fields are empty")
    else:
        is_ok = messagebox.askokcancel(title="Confirm Details",message=(f"Are these details corrrect?" 
                                                                    f"\n website: {website}"
                                                                    f"\n email: {email}"
                                                                    f"\n Password: {password}"))

        if is_ok:
            try:
                with open("passwords.json","r") as password_file:
                    data = json.load(password_file)
                    
            
                dump_json(data)
        
            except FileNotFoundError:
                dump_json(new_dict)

            else:
                data.update(new_dict)
                dump_json(data)
        
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

#--------------------------- SEARCH ------------------------------------# 
def search():
    website = website_entry.get().capitalize()
    try:
        with open("passwords.json","r") as password_file:
            data = json.load(password_file)
           
    except FileNotFoundError:
        messagebox.showinfo(title="File not Found",message="File does not exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title={website},message=(f"email: {email}\n password: {password}"))
        else:
            messagebox.showinfo(title="Website not Found",message="Webstie not found in Passwords")
            
               



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=18)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.insert(0, "timothykipruto007@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# Buttons
pw_generator_button = Button(text="Generate Password", command=password_generator,width=11)
pw_generator_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search",command=search,width=10,)
search_button.grid(row=1,column=2)


window.mainloop()