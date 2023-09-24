import num2words as n2w
from tkinter import *

def num_to_words():
    given_num = float(num.get())
    num_in_word = n2w.num2words(given_num)
    display.config(text=str(num_in_word).capitalize())

# Adding title
title = Label(root, text="Number to Words converter",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=220, y=10)