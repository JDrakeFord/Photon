from src.Display import Splash

Splash.drive()

# Drive player entry screen
from tkinter import Tk
from src.Display.Entry import PlayerEntryScreen


def main():
    # create the Tk object

    root = Tk()

    # create an instance of PlayerEntryScreen, passing the Tk object as the master
    player_entry_screen = PlayerEntryScreen(root)

    # call the drive() method of the instance to start the tkinter application
    player_entry_screen.drive()

if __name__ == '__main__':
    main()