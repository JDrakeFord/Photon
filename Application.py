from src.Display import Splash
# Drive player entry screen
from src.Display.Entry import PlayerEntryScreen


def main():
    # Splash creates itself during drive() because it is so simple
    Splash.drive()
    # We create the PlayerEntryScreen object and call drive(). *It will create its own master*
    player_entry_screen = PlayerEntryScreen()
    player_entry_screen.drive()

if __name__ == '__main__':
    main()
