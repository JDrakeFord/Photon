# PhotonLaserTag
This application is only known to work with Python ver. 3.9. ver 3.10 and 3.11 are known not to work.


Prerequisites to run: 
1. Must have the PIL library installed through PIP
2. Must have supabase installed through PIP


This application creates and shows a splash screen and player entry screen for a laser tag video game. 
When a player is entered into the player entry screen and the submit button is clicked, 
that player entry is sent to and stored in our supabase database.

If a player already exists in the database, 
our program will autofill the codename if given an existing first and last name.
