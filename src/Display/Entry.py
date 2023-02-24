import threading
import tkinter as tk

from src.Data.Player import Player
from src.Display.Action import PlayerActionScreen
from src.Util.Globals import *
import src.Util.Database as db


class PlayerEntryScreen:
    def checkCodename(self, event: tk.Event):
        caller: tk.Entry = event.widget
        index = str(caller.__str__())[7:]
        if not index:
            index = str(1)
        index = int(index) - 1
        index //= 3
        if db.checkIfPlayerExists(self.first_name_entries[index].get(), self.last_name_entries[index].get()):
            codename = db.getCodename(self.first_name_entries[index].get(), self.last_name_entries[index].get())
            self.code_name_entries[index].delete(0, tk.END)
            self.code_name_entries[index].insert(0, codename)

    def submit(self):
        self.success_text.set("")
        team_1_players = []
        team_2_players = []
        for i in range(0, 40):
            if (not (self.first_name_entries[i].get() and self.last_name_entries[i].get()
                     and self.code_name_entries[i].get())) \
                    and (self.first_name_entries[i].get() or self.last_name_entries[i].get()
                         or self.code_name_entries[i].get()):
                self.error_text.set("At least one of the players has incomplete information.")
                return 0
            else:
                self.error_text.set("")
        for i in range(0, 40):
            if (bool(self.first_name_entries[i].get())
                    and bool(self.last_name_entries[i].get())
                    and bool(self.code_name_entries[i].get())):
                if not db.checkIfPlayerExists(self.first_name_entries[i].get(), self.last_name_entries[i].get()):
                    db.newPlayer(self.first_name_entries[i].get(), self.last_name_entries[i].get(),
                                 self.code_name_entries[i].get())
                if i < 20:
                    team_1_players.append(Player(self.first_name_entries[i].get(), self.last_name_entries[i].get(),
                                          self.code_name_entries[i].get()))
                else:
                    team_2_players.append(Player(self.first_name_entries[i].get(), self.last_name_entries[i].get(),
                                                 self.code_name_entries[i].get()))

        self.success_text.set("Players created successfully!")
        action_screen = PlayerActionScreen('Red team', 'Green team', team_1_players, team_2_players)
        self.master.after(1000, self.master.destroy())
        threading.Thread(target=action_screen.drive()).start()

    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Player Entry")

        # Create player name label and entry widget
        self.team_label1 = tk.Label(self.master, text="Red Team", fg=red_color)
        self.team_label1.grid(row=0, column=0, padx=10, pady=10)
        self.team_label2 = tk.Label(self.master, text="Green Team", fg=green_color)
        self.team_label2.grid(row=0, column=6, padx=10, pady=10)

        self.name_labels = []
        self.first_name_entries = []
        self.last_name_entries = []
        self.code_name_entries = []

        for i in range(20):
            i_str = str(i + 1)
            name_label1 = tk.Label(self.master, text="Player #" + i_str + " First Name:")
            name_label1.grid(row=i + 1, column=0, padx=5, pady=5)
            first_name_entry1 = tk.Entry(self.master, fg=red_color)
            first_name_entry1.grid(row=i + 1, column=1, padx=5, pady=5)
            first_name_entry1.bind("<FocusOut>", self.checkCodename)
            last_name_label1 = tk.Label(self.master, text="Last Name:")
            last_name_label1.grid(row=i + 1, column=2, padx=5, pady=5)
            last_name_entry1 = tk.Entry(self.master, fg=red_color)
            last_name_entry1.grid(row=i + 1, column=3, padx=5, pady=5)
            last_name_entry1.bind("<FocusOut>", self.checkCodename)
            code_name_label1 = tk.Label(self.master, text="Code Name:")
            code_name_label1.grid(row=i + 1, column=4, padx=5, pady=5)
            code_name_entry1 = tk.Entry(self.master, fg=red_color)
            code_name_entry1.grid(row=i + 1, column=5, padx=5, pady=5)
            code_name_entry1.bind("<FocusOut>", self.checkCodename)

            self.name_labels.append(name_label1)
            self.first_name_entries.append(first_name_entry1)
            self.last_name_entries.append(last_name_entry1)
            self.code_name_entries.append(code_name_entry1)

        for i in range(20):
            i_str = str(i + 1)
            name_label2 = tk.Label(self.master, text="Player #" + i_str + " First Name:")
            name_label2.grid(row=i + 1, column=6, padx=5, pady=5)
            first_name_entry2 = tk.Entry(self.master, fg=green_color)
            first_name_entry2.grid(row=i + 1, column=7, padx=5, pady=5)
            first_name_entry2.bind("<FocusOut>", self.checkCodename)
            last_name_label2 = tk.Label(self.master, text="Last Name:")
            last_name_label2.grid(row=i + 1, column=8, padx=5, pady=5)
            last_name_entry2 = tk.Entry(self.master, fg=green_color)
            last_name_entry2.grid(row=i + 1, column=9, padx=5, pady=5)
            last_name_entry2.bind("<FocusOut>", self.checkCodename)
            code_name_label2 = tk.Label(self.master, text=" Code Name:")
            code_name_label2.grid(row=i + 1, column=10, padx=5, pady=5)
            code_name_entry2 = tk.Entry(self.master, fg=green_color)
            code_name_entry2.grid(row=i + 1, column=11, padx=5, pady=5)
            code_name_entry2.bind("<FocusOut>", self.checkCodename)

            self.name_labels.append(name_label2)
            self.first_name_entries.append(first_name_entry2)
            self.last_name_entries.append(last_name_entry2)
            self.code_name_entries.append(code_name_entry2)

            # Create submit button
            submit_button = tk.Button(self.master, text="Submit", command=self.submit)
            submit_button.grid(row=21, column=3, padx=10, pady=10)

            # Create error field
            self.error_text = tk.StringVar()
            self.error_label = tk.Label(self.master, textvariable=self.error_text, fg="red")
            self.error_label.grid(row=21, column=4, padx=10, pady=10, columnspan=3)

            # Create sucess field
            self.success_text = tk.StringVar()
            self.success_label = tk.Label(self.master, textvariable=self.success_text, fg="green")
            self.success_label.grid(row=21, column=1, padx=10, pady=10, columnspan=2)

    def drive(self):
        self.master.mainloop()
