import tkinter
from tkinter import messagebox,ttk

window=None
login_button=None
frame=None
username_entry=None
password_entry=None

def display_questions(filename):
    clear_screen()
    window.geometry('1400x700')



def on_select(event,combo):
    selected_item = combo.get()
    filename=f"{selected_item}.txt"
    print(f'Selected: {selected_item}')
    display_questions(filename)

def clear_screen():
    for widget in frame.winfo_children():
        widget.destroy()

def select_genre():
    clear_screen()
    window.title('Genre Select')

    header_label = tkinter.Label(frame, text='Select your topic of choice', bg="#9d9d9d", font=("Georgia", 16))
    header_label.pack(pady=40)

    combo = ttk.Combobox(frame, values=['Physics', 'Chemistry', 'Maths', 'English', 'Logical Reasoning', 'General Knowledge'])
    combo.pack(pady=10)
    combo.set('Chemistry')

    select_button = tkinter.Button(frame, text='Select', command=lambda: on_select(None, combo))
    select_button.pack(pady=10)

    combo['state'] = 'readonly'

def on_enter(event):
    login_button.config(cursor="hand2") 
    login_button.configure(fg="green")

def on_leave(event):
    login_button.config(cursor="")
    login_button.configure(fg="#FFFFFF")

def login():
    username=username_entry.get()
    password=password_entry.get()
    print(f'Username: {username}, Password: {password}')

    with open('Credentials.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            st_username, st_password = line.strip().split('-')

            if username == st_username.strip() and password == st_password.strip():
                messagebox.showinfo(title="Login Success", message="You successfully logged in.")
                select_genre()

        messagebox.showerror(title="Error", message="Invalid login.")


def initialize():
    window = tkinter.Tk()
    window.title("Login Form")
    window.geometry('500x500')
    window.configure(bg='#9D9D9D')

    frame = tkinter.Frame(bg='#9D9D9D')

    login_label = tkinter.Label(
        frame, text="Login", bg='#9D9D9D', fg="#170F11", font=("Times New Roman", 30))

    username_label = tkinter.Label(
        frame, text="Username", bg='#9D9D9D', fg="#FFFFFF", font=("Georgia", 16))

    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    password_label = tkinter.Label(
        frame, text="Password", bg='#9D9D9D', fg="#FFFFFF", font=("Georgia", 16))

    login_button = tkinter.Button(
        frame, text="Login", bg="#170F11", fg="#FFFFFF", font=("Georgia", 16), command=login)

    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=60)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    login_button.bind("<Enter>", on_enter)
    login_button.bind("<Leave>", on_leave)

    frame.pack()
    window.mainloop()