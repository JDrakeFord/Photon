import tkinter as tk
from src.Util.Globals import *
import src.Util.Database as db


class PlayerActionScreen(tk.Frame):
    def __init__(self, parent, team1_name, team2_name):
        super().__init__(parent)

        self.team1_name = team1_name
        self.team2_name = team2_name

        self.team1_score = 0
        self.team2_score = 0

        db.getFirstName()

        self.team1_players = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5',
                              'Player 6', 'Player 7', 'Player 8', 'Player 9', 'Player 10',
                              'Player 11', 'Player 12', 'Player 13', 'Player 14', 'Player 15',
                              'Player 16', 'Player 17', 'Player 18', 'Player 19', 'Player 20']

        self.team2_players = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5',
                              'Player 6', 'Player 7', 'Player 8', 'Player 9', 'Player 10',
                              'Player 11', 'Player 12', 'Player 13', 'Player 14', 'Player 15',
                              'Player 16', 'Player 17', 'Player 18', 'Player 19', 'Player 20']

        self.create_widgets()

        self.time_left = 30
        self.update_time_left()

    def create_widgets(self):
        # Create labels for team names and scores
        self.team1_label = tk.Label(self, text=self.team1_name, font=('Helvetica', 18), fg=red_color)
        self.team1_label.grid(row=0, column=0, padx=10, pady=10)

        self.team2_label = tk.Label(self, text=self.team2_name, font=('Helvetica', 18), fg=green_color)
        self.team2_label.grid(row=0, column=2, padx=10, pady=10)

        self.team1_score_label = tk.Label(self, text=str(self.team1_score), font=('Helvetica', 36))
        self.team1_score_label.grid(row=1, column=0, padx=10, pady=10)

        self.team2_score_label = tk.Label(self, text=str(self.team2_score), font=('Helvetica', 36))
        self.team2_score_label.grid(row=1, column=2, padx=10, pady=10)

        # Create buttons for team actions
        self.team1_button = tk.Button(self, text='Team 1 Action', command=self.team1_action)
        self.team1_button.grid(row=2, column=0, padx=10, pady=10)

        self.team2_button = tk.Button(self, text='Team 2 Action', command=self.team2_action)
        self.team2_button.grid(row=2, column=2, padx=10, pady=10)

        # Create label for time remaining
        self.time_left_label = tk.Label(self, text='Time left: 30', font=('Helvetica', 18))
        self.time_left_label.grid(row=3, column=1, padx=10, pady=10)

        # Create labels for team players
        self.team1_player_labels = []
        for i in range(20):
            player_label = tk.Label(self, text=self.team1_players[i], font=('Helvetica', 12), fg=red_color)
            player_label.grid(row=4+i, column=0, padx=5, pady=1)

        self.team2_player_labels = []
        for i in range(20):
            player_label = tk.Label(self, text=self.team2_players[i], font=('Helvetica', 12), fg=green_color)
            player_label.grid(row=4+i, column=2, padx=5, pady=1)



    def team1_action(self):
        # Add score for team 1 and update label
        self.team1_score += 1
        self.team1_score_label.config(text=str(self.team1_score))

    def team2_action(self):
        # Add score for team 2 and update label
        self.team2_score += 1
        self.team2_score_label.config(text=str(self.team2_score))

    def update_time_left(self):
        # Update time left label and decrease time_left variable by 1
        self.time_left_label.config(text=f'Time remaining before game start: {self.time_left}')
        self.time_left -= 1

        if self.time_left >= 0:
            self.after(1000, self.update_time_left)
