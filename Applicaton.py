import tkinter as tk

# Create the master object
master = tk.Tk()


# Function to print content of e1
def printE1():
    print(e1.get())


# Function to print content of e2
def printE2():
    print(e2.get())


# Create the label objects and pack them using grid
tk.Label(master, text="Label 1").grid(row=0, column=0)
tk.Label(master, text="Label 2").grid(row=1, column=0)

# Create the entry objects using master
e1 = tk.Entry(master)
e2 = tk.Entry(master)

# Create button to call fuction
b1 = tk.Button(master, command=printE1, text="print 1")
b2 = tk.Button(master, command=printE2, text="print 2")

# Pack them using grid
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

# The mainloop
tk.mainloop()
from tkinter import *
from PIL import ImageTk, Image

#TODO: Fix the image and make it resize with the window

#Creates the screen and sets the size
screen = Tk()
screen.geometry("1280x720")

#Puts the Image onto the screen
imgframe = Frame(screen, width=1280, height=720)
imgframe.pack()
imgframe.place(anchor = 'center')
img = ImageTk.PhotoImage(Image.open("SplashLogo.jpg"))
splash = Label(imgframe, image = img)
splash.pack()

#Function to delete the splashscreen
def deleteSplash():
    splash.destroy()

screen.after(1250, deleteSplash)

mainloop()