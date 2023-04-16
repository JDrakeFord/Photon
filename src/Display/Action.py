import tkinter as tk
from random import random, choice
import os
import socket
from threading import Thread
from tkinter import END, DISABLED
from pygame import mixer
from src.Data import Player
from src.Data.Team import Team
from src.Util import TimerUtil
from src.Util.Globals import *

class PlayerActionScreen(tk.Frame):
    instances = []
    def __init__(self, team1_name, team2_name, team1_players: list[Player], team2_players: list[Player]):
        master = tk.Tk()
        super().__init__(master)
        master.geometry('1200x800')
        self.flash_on_white = False

        self.team1 = Team(team1_players)
        self.team2 = Team(team2_players)
        self.team1_score = tk.StringVar(self, self.team1.score)
        self.team2_score = tk.StringVar(self, self.team2.score)

        self.team1_player_scores: list[tk.StringVar] = []
        for player in self.team1.players:
            self.team1_player_scores.append(tk.StringVar(self, player.score))
        self.team2_player_scores: list[tk.StringVar] = []
        for player in self.team2.players:
            self.team2_player_scores.append(tk.StringVar(self, player.score))

        mixer.init()     # Starts the music player

        PlayerActionScreen.instances.append(self)

        self.create_widgets()
        Thread(target=self.socket_loop).start()

        self.time_left = 30
        self.update_time_left()
        self.update_scores()

    def create_widgets(self):
        self.team1_frame = tk.Frame(self)
        self.team2_frame = tk.Frame(self)
        self.countdown_frame = tk.Frame(self)
        self.event_frame = tk.Frame(self)

        # Create labels for team names and scores
        self.team1_label = tk.Label(self.team1_frame, text="Red", font=('Helvetica', 18), fg=red_color)
        self.team1_label.grid(row=0, column=0)

        self.team2_label = tk.Label(self.team2_frame, text="Green", font=('Helvetica', 18), fg=green_color)
        self.team2_label.grid(row=0, column=2, pady=(20, 0))

        self.team1_score_label = tk.Label(self.team1_frame, textvariable=self.team1_score, font=('Helvetica', 25))
        self.team1_score_label.grid(row=1, column=0)

        self.team2_score_label = tk.Label(self.team2_frame, textvariable=self.team2_score, font=('Helvetica', 25))
        self.team2_score_label.grid(row=1, column=2)

        self.event_text = tk.Text(self.event_frame, font=('Helvetica', 18), state=DISABLED)
        self.event_text.grid(row=0, column=0)

        self.high_score_label = self.team1_score_label

        self.team1_frame.grid(row=1, column=0, padx=200)
        self.team2_frame.grid(row=1, column=2, padx=200)
        self.countdown_frame.grid(row=0, column=0, columnspan=3)
        self.event_frame.grid(row=2, column=0, columnspan=3)


        # Create label for time remaining
        self.time_left_label = tk.Label(self.countdown_frame, font=('Helvetica', 18))
        self.time_left_label.grid(row=0, column=0)

        # Create labels for team players
        self.team1_player_labels = []
        count = 0
        for i in self.team1.players:
            player_label = tk.Label(self.team1_frame, text=i.codeName, font=('Helvetica', 12), fg=red_color)
            player_label.grid(row=4 + count, column=0)
            player_score_label = tk.Label(self.team1_frame, textvariable=self.team1_player_scores[count], font=('Helvetica', 12), fg=red_color)
            player_score_label.grid(row=4 + count, column=1)
            count += 1

        count = 0
        self.team2_player_labels = []
        for i in self.team2.players:
            player_label = tk.Label(self.team2_frame, text=i.codeName, font=('Helvetica', 12), fg=green_color)
            player_label.grid(row=4 + count, column=2)
            player_score_label = tk.Label(self.team2_frame, textvariable=self.team2_player_scores[count], font=('Helvetica', 12), fg=green_color)
            player_score_label.grid(row=4 + count, column=3)
            count += 1

    def update_time_left(self):
        # Update time left label and decrease time_left variable by 1
        self.time_left_label.config(text=f'Time remaining before game start: {self.time_left}')
        self.time_left -= 1
        if self.time_left >= 0:
            self.after(1000, self.update_time_left)
        else:
            self.time_left = 360    # sets time to 360 seconds, or 6 minutes (unformatted). Value will later be formatted and stored as another variable.
            self.update_time_left_game()
            self.playTrack()    # start track
        
    def update_time_left_game(self):
        self.time_left_label.config(text=f'Time remaining before game end: {TimerUtil.seconds_to_mm_ss(self.time_left)}')
        self.time_left -= 1
        if self.time_left >= 0:
            self.after(1000,self.update_time_left_game)
        else:
            mixer.music.stop()
            self.time_left_label.config(text = f'GAME OVER!')    # Ends the music, changes text

    def update_scores(self):
        self.team1_score.set(self.team1.score)
        self.team2_score.set(self.team2.score)
        for i in range(len(self.team1.players)):
            self.team1_player_scores[i].set(self.team1.players[i].score)
        for i in range(len(self.team2.players)):
            self.team2_player_scores[i].set(self.team2.players[i].score)
        if self.team1.score > self.team2.score:
            if self.high_score_label is not None:
                self.high_score_label.config(fg="black")
            self.high_score_label = self.team1_score_label
            self.flash()
        elif self.team2.score > self.team1.score:
            if self.high_score_label is not None:
                self.high_score_label.config(fg="black")
            self.high_score_label = self.team2_score_label
            self.flash()
        else:
            if self.high_score_label is not None:
                self.high_score_label.config(fg="black")
            self.high_score_label = None
        self.after(300, self.update_scores)

    def flash(self):
        if self.high_score_label is not None:
            if self.flash_on_white:
                self.high_score_label.config(fg="black")
                self.flash_on_white = False
            else:
                self.high_score_label.config(fg="white")
                self.flash_on_white = True

    def socket_loop(self):
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        s.bind(("127.0.0.1", 7501))
        bufferSize = 1024
        while True:
            data = s.recvfrom(bufferSize)
            attacker, defender = data[0].decode().split(':')
            self.event_text.config(state='normal')
            self.event_text.tag_configure("center", justify='center')
            self.event_text.insert("1.0", "\n" + attacker + " tagged " + defender)
            self.event_text.tag_add("center", "1.0", "end")
            self.event_text.config(state='disabled')
            if self.team1.hasPlayer(attacker):
                self.team1.playerScored(attacker)
            elif self.team2.hasPlayer(attacker):
                self.team2.playerScored(attacker)

    def drive(self):
        self.pack(anchor='w')
        self.mainloop()

    def playTrack(self):
        Tracklist = os.listdir("./Resources/Tracks/")
        musicTrack = choice(Tracklist)
        musicTrack = "./Resources/Tracks/" + musicTrack
        mixer.music.load(musicTrack)
        mixer.music.play()
