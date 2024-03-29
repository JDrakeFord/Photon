from tkinter import *
from PIL import ImageTk, Image


def drive():
    # Creates splash screen and sets size
    screen = Tk()
    screen.geometry("720x480")

    # Displays Splash image
    imgframe = Frame(screen, width=720, height=480)
    imgframe.pack()
    imgframe.place(anchor='nw')
    img = ImageTk.PhotoImage(Image.open("./Resources/Splash480p.jpg"))
    splash = Label(imgframe, image=img)
    splash.pack()

    # Deletes Splash
    def deleteSplash():
        screen.destroy()
    screen.after(1250, deleteSplash)

    mainloop()
