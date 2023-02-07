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