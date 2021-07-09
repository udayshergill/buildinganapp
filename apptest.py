import tkinter as tk #import library
from tkinter import filedialog, Text #bringing stuff from library
import os

root = tk.Tk() #setting up the main folder where everything attaches to
canvas = tk.Canvas(root, height=700, width=700, bg="#34d3eb") #making the canvas, delaring the root then changing height, width, and background color
canvas.pack() #attaching the canvas to the root
def addApp():
    filename= filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("executables", "*.exe"), ("allfiles", "*.*")))

frame = tk.Frame(root, bg="white")#Created a frame and attached it to the root made the bg white
frame.place(relwidth= 0.8, relheight= 0.8, relx= 0.1, rely= 0.1) #placed frame on gui and given it a width, height, and a x and y location

openFile = tk.Button(frame, text = "Open File", padx=10, pady=7, fg="black", bg="white", command = addApp) #created a button on the frame, with text "Open File", set x, set y, set foreground color, can set bg color, set a command to open an app with button
openFile.pack() #places the button
root.mainloop()