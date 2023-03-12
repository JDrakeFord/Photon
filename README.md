# PhotonLaserTag
Only Python 3.9 is supported for this project. Python 3.11 is known to break the program
This is written and designed for windows, but may work in other Operating Systems. YMMV


Prerequisites to run: 
1. Must have the PIL library installed through PIP
2. Must have supabase installed through PIP


This application creates and shows a splash screen, player entry screen and play action screen for a laser tag video game. 
When a player is entered into the player entry screen and the submit button is clicked, 
that player entry is sent to and stored in our supabase database. If you try to change the codename for 
a player already in the database, the program will refill. After submitting players from the player entry screen and waiting for the 30 second countdown, the user is greeted with a player action screen. Red team members and scores are shown on the right side of the screen, and green team on the left. 

If a player already exists in the database, 
our program will autofill the codename if given an existing first and last name.

## Installation
1. Install Python 3.9
2. Clone the "Photon" repository
3. Run the following commands in the terminal (in whatever environment you are going to run the program in)
    pip install pillow
    pip install supabase
4. Run "Application.py" *IN PYTHON 3.9*
