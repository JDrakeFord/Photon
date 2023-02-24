from src.Display import Splash

Splash.drive()

# Drive player entry screen
from tkinter import Tk
from src.Display.Entry import PlayerEntryScreen
from src.Data.Game import LaserTagPlayerActionScreen


def main():
    # create the Tk object

    root = Tk()

    # create an instance of PlayerEntryScreen, passing the Tk object as the master
    #player_entry_screen = PlayerEntryScreen(root)

    # call the drive() method of the instance to start the tkinter application
    #player_entry_screen.drive()

    screen = LaserTagPlayerActionScreen(root, 'Red team', 'Green team')
    screen.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
