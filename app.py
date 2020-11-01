import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import Timer

class Pomodoro(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Pomodoro')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.short_break = tk.StringVar(value=5)
        self.long_break = tk.StringVar(value=15)

        self.timer_order = ['Pomodoro', 'Short Break', 'Pomodoro', 'Short Break', 'Long Break']
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        timer_frame = Timer(container, self)
        timer_frame.grid(row=0, column=0, sticky='NSEW')

app = Pomodoro()
app.mainloop()