#Commented out due to application not running with it. Out of date implementation?

#import Splash
#Splash.drive()

# Drive player entry screen
from tkinter import Tk
from Entry import Entry
from src.Entry.Entry import PlayerEntryScreen


def main():
    # create the Tk object
    root = Tk()

    # create an instance of PlayerEntryScreen, passing the Tk object as the master
    player_entry_screen = PlayerEntryScreen(root)

    # call the drive() method of the instance to start the tkinter application
    player_entry_screen.drive()

if __name__ == '__main__':
    main()