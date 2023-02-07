import tkinter as tk
from PIL import ImageTk, Image

# Creates the master and sets the size
screen = tk.Tk()
screen.geometry("1280x720")

# Puts the Image onto the master
imgframe = tk.Frame(screen, width=1280, height=720)
imgframe.pack()
imgframe.place(anchor='center')
img = ImageTk.PhotoImage(Image.open("SplashLogo.jpg"))
splash = tk.Label(imgframe, image=img)
splash.pack()


# def startPlayerEntry():
#     print("HIT")
#     # Create the master object
#     master = tk.Tk()
#     master.geometry("500x600")
#
#     # Function to print content of e1
#     def printE1():
#         print(e1.get())
#
#     # Function to print content of e2
#     def printE2():
#         print(e2.get())
#
#     # Create the label objects and pack them using grid
#     tk.Label(master, text="Label 1").grid(row=0, column=0)
#     tk.Label(master, text="Label 2").grid(row=1, column=0)
#
#     # Create the entry objects using master
#     e1 = tk.Entry(master)
#     e2 = tk.Entry(master)
#
#     # Create button to call fuction
#     b1 = tk.Button(master, command=printE1, text="print 1")
#     b2 = tk.Button(master, command=printE2, text="print 2")
#
#     # Pack them using grid
#     e1.grid(row=0, column=1)
#     e2.grid(row=1, column=1)
#     b1.grid(row=2, column=0)
#     b2.grid(row=2, column=4)
#
#     # The mainloop
#     tk.mainloop()


# Function to delete the splash
def deleteSplashAndStartPlayerEntry():
    splash.destroy()
    # startPlayerEntry()


screen.after(1250, deleteSplashAndStartPlayerEntry())
tk.mainloop()
