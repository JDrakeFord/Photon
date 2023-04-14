from src.Display import Splash


# Drive player entry screen
from tkinter import Tk
from src.Display.Entry import PlayerEntryScreen
from src.Display.Action import PlayerActionScreen


def main():
    # Splash creates itself during drive() because it is so simple
    Splash.drive()
    
    # We create the PlayerEntryScreen object and call drive(). *It will create its own master*
    player_entry_screen = PlayerEntryScreen()
    player_entry_screen.drive()

    # player_action_screen = PlayerActionScreen('Red team', 'Green team')
    # player_action_screen.drive()

if __name__ == '__main__':
    main()
