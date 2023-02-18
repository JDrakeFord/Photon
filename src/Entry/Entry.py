import tkinter as tk


class PlayerEntryScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Player Entry")

        # Create player name label and entry widget
        self.team_label1 = tk.Label(master, text="Red Team")
        self.team_label1.grid(row=0, column=1, padx=10, pady=10)
        self.team_label2 = tk.Label(master, text="Green Team")
        self.team_label2.grid(row=0, column=3, padx=10, pady=10)

        self.name_labels = []
        self.name_entries = []

        for i in range(20):
            i_str = str(i+1)
            name_label1 = tk.Label(master, text="Player #" + i_str + " Name:")
            name_label1.grid(row=i+1, column=0, padx=5, pady=5)
            name_entry1 = tk.Entry(master)
            name_entry1.grid(row=i+1, column=1, padx=5, pady=5)
            self.name_labels.append(name_label1)
            self.name_entries.append(name_entry1)

            name_label2 = tk.Label(master, text="Player #" + i_str + " Name:")
            name_label2.grid(row=i+1, column=3, padx=5, pady=5)
            name_entry2 = tk.Entry(master)
            name_entry2.grid(row=i+1, column=4, padx=5, pady=5)
            self.name_labels.append(name_label2)
            self.name_entries.append(name_entry2)

        # Create submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.grid(row=21, column=3, padx=10, pady=10)


# Create main window and run application
root = tk.Tk()
app = PlayerEntryScreen(root)
root.mainloop()
