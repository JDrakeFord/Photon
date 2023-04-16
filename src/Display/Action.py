import tkinter as tk
from random import random, choice
import os
from pygame import mixer

from src.Data import Player
from src.Util.Globals import *
import src.Util.Database as db

class PlayerActionScreen(tk.Frame):
    instances = []
    def __init__(self, team1_name, team2_name, team1_players: list[Player], team2_players: list[Player]):
        master = tk.Tk()
        super().__init__(master)
        master.geometry('1200x800')
        self.team1_name = team1_name
        self.team2_name = team2_name

        self.team1_score = 0
        self.team2_score = 0

        self.team1_players = team1_players
        self.team2_players = team2_players

        self.team1_player_scores: list[tk.StringVar] = []
        for player in team1_players:
            self.team1_player_scores.append(tk.StringVar(self, player.score))
        self.team2_player_scores: list[tk.StringVar] = []
        for player in team2_players:
            self.team2_player_scores.append(tk.StringVar(self, player.score))

        #Starts the music player
        mixer.init()

        PlayerActionScreen.instances.append(self)

        self.create_widgets()

        self.time_left = 30
        self.update_time_left()

    def create_widgets(self):
        self.team1_frame = tk.Frame(self)
        self.team2_frame = tk.Frame(self)
        self.countdown_frame = tk.Frame(self)

        # Create labels for team names and scores
        self.team1_label = tk.Label(self.team1_frame, text=self.team1_name, font=('Helvetica', 18), fg=red_color)
        self.team1_label.grid(row=0, column=0)

        self.team2_label = tk.Label(self.team2_frame, text=self.team2_name, font=('Helvetica', 18), fg=green_color)
        self.team2_label.grid(row=0, column=2, pady=(20, 0))

        self.team1_score_label = tk.Label(self.team1_frame, text=str(self.team1_score), font=('Helvetica', 25))
        self.team1_score_label.grid(row=1, column=0)

        self.team2_score_label = tk.Label(self.team2_frame, text=str(self.team2_score), font=('Helvetica', 25))
        self.team2_score_label.grid(row=1, column=2)

        self.team1_frame.grid(row=1, column=0, padx=200)
        self.team2_frame.grid(row=1, column=2, padx=200)
        self.countdown_frame.grid(row=0, column=0, columnspan=3)

        # Create buttons for team actions
        self.team1_button = tk.Button(self, text='Team 1 Action', command=self.team1_action)
        # self.team1_button.grid(row=2, column=0, padx=10, pady=10)

        self.team2_button = tk.Button(self, text='Team 2 Action', command=self.team2_action)
        # self.team2_button.grid(row=2, column=2, padx=10, pady=10)

        # Create label for time remaining
        self.time_left_label = tk.Label(self.countdown_frame, text='Time left: 30', font=('Helvetica', 18))
        self.time_left_label.grid(row=0, column=0)

        # Create labels for team players
        self.team1_player_labels = []
        self.team1_player_score_labels = []
        count = 0
        for i in self.team1_players:
            player_label = tk.Label(self.team1_frame, text=i.codeName, font=('Helvetica', 12), fg=red_color)
            player_label.grid(row=4 + count, column=0)
            player_score_label = tk.Label(self.team1_frame, textvariable=self.team1_player_scores[count], font=('Helvetica', 12), fg=red_color)
            player_score_label.grid(row=4 + count, column=1)
            count += 1

        count = 0
        self.team2_player_labels = []
        for i in self.team2_players:
            player_label = tk.Label(self.team2_frame, text=i.codeName, font=('Helvetica', 12), fg=green_color)
            player_label.grid(row=4 + count, column=2)
            player_score_label = tk.Label(self.team2_frame, textvariable=self.team2_player_scores[count], font=('Helvetica', 12), fg=green_color)
            player_score_label.grid(row=4 + count, column=3)
            count += 1

    def team1_action(self):
        # Add score for team 1 and update label
        self.team1_score += 1
        p: Player = choice(self.team1_players)
        p.score += 1
        self.team1_score_label.config(text=str(self.team1_score))
        self.__class__.updateScores()

    def team2_action(self):
        # Add score for team 2 and update label
        self.team2_score += 1
        p: Player = choice(self.team2_players)
        p.score += 1
        self.team2_score_label.config(text=str(self.team2_score))
        self.__class__.updateScores()

    def update_time_left(self):
        # Update time left label and decrease time_left variable by 1
        self.time_left_label.config(text=f'Time remaining before game start: {self.time_left}')
        self.time_left -= 1
        if self.time_left >= 0:
            self.after(1000, self.update_time_left)
        else:
            self.time_left = 360
            self.update_time_left_game()
            self.playTrack()
            #start track
        
    def update_time_left_game(self):   
        self.time_left_label.config(text=f'Time remaining before game end: {self.time_left}')
        self.time_left -= 1
        if self.time_left >= 0:
            self.after(1000,self.update_time_left_game)
        else:
            mixer.music.stop()
            self.time_left_label.config(text = f'GAME OVER!')
            #Ends the music, changes text

    def drive(self):
        self.pack(anchor='w')
        self.mainloop()

    def playTrack(self):
        Tracklist = os.listdir("./Resources/Tracks/")
        musicTrack = choice(Tracklist)
        musicTrack = "./Resources/Tracks/" + musicTrack
        mixer.music.load(musicTrack)
        mixer.music.play()

    @classmethod
    def updateScores(cls):
        for instance in cls.instances:
            for i in range(len(instance.team1_players)):
                instance.team1_player_scores[i].set(instance.team1_players[i].score)
            for i in range(len(instance.team2_players)):
                instance.team2_player_scores[i].set(instance.team2_players[i].score)


