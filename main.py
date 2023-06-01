from tkinter import *
from tkinter import filedialog, messagebox, scrolledtext
import random
import datetime

FONT_NAME = "Courier"
COLOR_1 = "#FBF0F0"
COLOR_2 = "#DFD3D3"
COLOR_3 = "#B8B0B0"
COLOR_4 = "#7C7575"

def start_timer():
    global time_left
    time_left = 5
    count_down()

def count_down():
    global time_left
    if time_left > 0:
        window.after(1000, count_down)
        time_left -= 1
        print(time_left)

    if time_left == 0:
        text_field_input.delete(1.0, END)
        print(time_left)
        time_left = 5

def restart_timer(event):
    global time_left
    time_left = 5

def start():
    window.bind('<Key>', restart_timer)
    title_label2.pack_forget()
    start_button.pack_forget()
    text_field_input.pack()
    title_label.config(text="Type here!")
    start_timer()

window = Tk()
window.title("Disappearing text writer")
window.minsize(750, 600)
window.maxsize(750, 600)
window.config(padx=50, pady=50, bg=COLOR_1)

title_label = Label(text="Disappearing text writer", font=(FONT_NAME, 20, "bold"), bg=COLOR_1, fg=COLOR_4, pady=25)
title_label.pack()

title_label2 = Label(text="Your text will disappear 5 seconds after you stop typing", font=(FONT_NAME, 10, "bold"), bg=COLOR_1, fg=COLOR_4, pady=25)
title_label2.pack()

start_button = Button(text="Start", highlightthickness=0, command=start)
start_button.pack()

text_field_input = scrolledtext.ScrolledText()

window.mainloop()