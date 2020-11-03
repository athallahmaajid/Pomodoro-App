import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import Timer, Setting

COLOR_PRIMARY = '#2e3f4f'
COLOR_SECONDARY = '#293846'
COLOR_LIGHT_BACKGROUND = '#fff'
COLOR_LIGHT_TEXT = '#eee'
COLOR_DARK_TEXT = '#8095a8'

class Pomodoro(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)
        style.theme_use(themename='clam')

        style.configure('Timer.TFrame', background=COLOR_LIGHT_BACKGROUND)
        style.configure('Background.TFrame', background=COLOR_PRIMARY)
        style.configure('TimerText.TLabel', background=COLOR_LIGHT_BACKGROUND, foreground=COLOR_DARK_TEXT, font=('FreeMono', 44))
        style.configure('LightText.TLabel', background=COLOR_PRIMARY, foreground=COLOR_LIGHT_TEXT, font=('Times New Roman', 18))
        style.configure('PomodoroButton.TButton', background=COLOR_SECONDARY, foreground=COLOR_LIGHT_TEXT)
        style.map('PomodoroButton.TButton', background=[('active', COLOR_PRIMARY), ('disabled', COLOR_LIGHT_TEXT)])

        self['background'] = COLOR_PRIMARY

        self.title('Pomodoro')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.short_break = tk.StringVar(value=5)
        self.long_break = tk.StringVar(value=15)

        self.timer_order = ['Pomodoro', 'Short Break', 'Pomodoro', 'Short Break', 'Long Break']
        self.timer_schedule = deque(self.timer_order)

        self.frames = dict()

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        timer_frame = Timer(container, self, lambda:self.show_frame(Setting))
        timer_frame.grid(row=0, column=0, sticky='NEWS')

        settings_frame = Setting(container, self, lambda:self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky='NEWS')

        self.frames[Timer] = timer_frame
        self.frames[Setting] = settings_frame

        self.show_frame(Timer)
    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

app = Pomodoro()
app.mainloop()