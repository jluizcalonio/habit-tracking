# This was shared by user Tiago on the Q&A Session of the class

from tkinter import *
from tkcalendar import *
from datetime import datetime as dt
import requests
import webbrowser
from tkinter import messagebox

URL = "https://pixe.la/v1/users/joaoluizpyhon/graphs/graphbookread1.html"  # Change the URL to your graph
TODAY = dt.now()
TOKEN = "jondee123"
GRAPH_ID = "graphbookread1"

window = Tk()
window.title("Habit Tracker")
# root.iconphoto(True, PhotoImage(file="static/python-128.png"))  # Change the icon
window.resizable(width=False, height=False)
window.config(pady=20, padx=20)


def open_browser():
    webbrowser.open(URL, new=1)


def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    endpoint = "https://pixe.la/v1/users/joaoluizpyhon/graphs/graphbookread1/"
    pixel_add = {
        "date": format_date(),
        "quantity": user_in.get(),
    }
    add_pxl = requests.post(url=endpoint, json=pixel_add, headers=headers)
    user_in.delete(0, END)
    if add_pxl.status_code == 200:
        messagebox.showinfo(message="Pixel added.")
    elif add_pxl.status_code == 503:
        messagebox.showinfo(title=str(add_pxl.status_code), message="Please retry this request. Your request for some APIs will be rejected 25% of the time because you are not a Pixela supporter")
    elif add_pxl.status_code == 400:
        messagebox.showinfo(title=str(add_pxl.status_code), message="It is necessary to specify quantity or optional data.")

def del_pixel():
    endpoint = f"https://pixe.la/v1/users/joaoluizpyhon/graphs/graphbookread1/{format_date()}"
    del_pxl = requests.delete(url=endpoint, headers=headers)
    if del_pxl.status_code == 200:
        messagebox.showinfo(message="Pixel deleted.")
    elif del_pxl.status_code == 503:
        messagebox.showinfo(title=str(del_pxl.status_code), message="Please retry this request. Your request for some APIs will be rejected 25% of the time because you are not a Pixela supporter")

def change_pixel():
    endpoint = f"https://pixe.la/v1/users/joaoluizpyhon/graphs/graphbookread1/{format_date()}"
    pixel_update = {
        "quantity": user_in.get(),
    }
    change_pxl = requests.put(url=endpoint, json=pixel_update, headers=headers)
    user_in.delete(0, END)
    print(change_pxl.text)
    print(change_pxl)
    if change_pxl.status_code == 200:
        messagebox.showinfo(message="Pixel updated.")
    elif change_pxl.status_code == 503:
        messagebox.showinfo(title=str(change_pxl.status_code), message="Please retry this request. Your request for some APIs will be rejected 25% of the time because you are not a Pixela supporter")
    elif change_pxl.status_code == 400:
        messagebox.showinfo(title=str(change_pxl.status_code), message="It is necessary to specify quantity or optional data.")

cal = Calendar(window, selectmode="day", year=TODAY.year, month=TODAY.month, day=TODAY.day)
cal.grid(row=0, column=0, columnspan=4)
units = Label(text="Minutes/Day:")
units.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")
user_in = Entry(width=10)
user_in.grid(row=1, column=2, sticky="w")

headers = {
    "X-USER-TOKEN": TOKEN
}

add = Button(text="Add", command=add_pixel)
add.grid(row=2, column=0, pady=10)
update = Button(text="Update", command=change_pixel)
update.grid(row=2, column=1, pady=10, sticky="w")
delete = Button(text="Delete", command=del_pixel)
delete.grid(row=2, column=2, pady=10, sticky="w")
link = Button(text="Show\nJourney", command=open_browser)
link.grid(row=2, column=3)

window.mainloop()