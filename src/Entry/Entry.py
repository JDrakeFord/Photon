import tkinter as tk

class PlayerEntryScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Player Entry")

        # Create player name label and entry widget
        self.team_label1 = tk.Label(master, text="Red Team")
        self.team_label1.grid(row=0, column=1, padx=10, pady=10)
        self.team_label2 = tk.Label(master, text="Green Team")
        self.team_label2.grid(row=0, column=6, padx=10, pady=10)

        self.name_labels = []
        self.first_name_entries = []
        self.last_name_entries = []
        self.code_name_entries = []

        for i in range(20):
            i_str = str(i+1)
            name_label1 = tk.Label(master, text="Player #" + i_str + " First Name:")
            name_label1.grid(row=i+1, column=0, padx=5, pady=5)
            first_name_entry1 = tk.Entry(master)
            first_name_entry1.grid(row=i+1, column=1, padx=5, pady=5)
            last_name_label1 = tk.Label(master, text="Last Name:")
            last_name_label1.grid(row=i+1, column=2, padx=5, pady=5)
            last_name_entry1 = tk.Entry(master)
            last_name_entry1.grid(row=i+1, column=3, padx=5, pady=5)
            code_name_label1 = tk.Label(master, text="Code Name:")
            code_name_label1.grid(row=i+1, column=4, padx=5, pady=5)
            code_name_entry1 = tk.Entry(master)
            code_name_entry1.grid(row=i+1, column=5, padx=5, pady=5)

            self.name_labels.append(name_label1)
            self.first_name_entries.append(first_name_entry1)
            self.last_name_entries.append(last_name_entry1)
            self.code_name_entries.append(code_name_entry1)

        for i in range(20):
            i_str = str(i+1)
            name_label2 = tk.Label(master, text="Player #" + i_str + " First Name:")
            name_label2.grid(row=i+1, column=6, padx=5, pady=5)
            first_name_entry2 = tk.Entry(master)
            first_name_entry2.grid(row=i+1, column=7, padx=5, pady=5)
            last_name_label2 = tk.Label(master, text="Last Name:")
            last_name_label2.grid(row=i+1, column=8, padx=5, pady=5)
            last_name_entry2 = tk.Entry(master)
            last_name_entry2.grid(row=i+1, column=9, padx=5, pady=5)
            code_name_label2 = tk.Label(master, text=" Code Name:")
            code_name_label2.grid(row=i+1, column=10, padx=5, pady=5)
            code_name_entry2 = tk.Entry(master)
            code_name_entry2.grid(row=i+1, column=11, padx=5, pady=5)

            self.name_labels.append(name_label2)
            self.first_name_entries.append(first_name_entry2)
            self.last_name_entries.append(last_name_entry2)
            self.code_name_entries.append(code_name_entry2)

    def submit(self):
        # Add code here to handle the submission of player names
        for name_entry in self.first_name_entries:
            print(name_entry.get())

    def drive(self):
        # Create submit button
        submit_button = tk.Button(self.master, text="Submit", command=self.submit)
        submit_button.grid(row=21, column=3, padx=10, pady=10)

        self.master.mainloop()