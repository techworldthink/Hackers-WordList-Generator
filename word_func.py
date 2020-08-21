from tkinter.ttk import *
from tkinter import*
from tkinter import font
from tkinter import messagebox
from array_list import*


def submit_message_1(get_value,get_mini,get_maxi):
    messagebox.showinfo("processing...", "Successfully  recorded")
    characters_send = get_value
    word_array(characters_send,get_mini,get_maxi)
def submit_cancel_1():
    messagebox.showwarning("warning","Cancelled")  

        
        
        


