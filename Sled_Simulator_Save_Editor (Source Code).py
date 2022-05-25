import os.path
import os
import sys
import tkinter
from tkinter import *

root1 = Tk()
root1.title('Sled Simulator - Save Editor')
root1.geometry("360x480")

message0 = Label(root1, text="Sled Simulator Save Editor.")
message0.pack()

message1 = Label(root1, text="Made By: Phinehas Beresford (Cracko298).")
message1.pack()

message2 = Label(root1, text=" ")
message2.pack()

#=======================================================#

data_in_byte = b'\xFF\xFF\xFF\xFF\xFF\xFF\x0D\x0A' #From V1 (UI Writes bytes to file.)
def myClick0():
    data_in_byte = b'\xFF\xFF\xFF\xFF\xFF\xFF\x0D\x0A' 
    Save = "Save" 

    with open(Save, 'rb+') as binary_file:
      binary_file.seek(401) 
      binary_file.write(data_in_byte) 

myButton0 = Button(root1, text="Max Money", command=myClick0, fg="white", bg="black")
myButton0.pack()

root1.mainloop()