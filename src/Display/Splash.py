from tkinter import *
from PIL import ImageTk, Image


def drive():
    # Creates the screen and sets the size
    screen = Tk()
    screen.geometry("720x480")

    # Puts the Image onto the screen
    imgframe = Frame(screen, width=720, height=480)
    imgframe.pack()
    imgframe.place(anchor='nw')
    img = ImageTk.PhotoImage(Image.open("../Resources/Splash480p.jpg"))
    splash = Label(imgframe, image=img)
    splash.pack()

    # Function to delete the splashscreen
    def deleteSplash():
        screen.destroy()

    screen.after(1250, deleteSplash)

    mainloop()
