import tkinter as tk
from tkinter import ttk
from frames import Timer

class Setting(ttk.Frame):
    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)

        self['style'] = 'Background.TFrame'

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        settings_container = ttk.Frame(self, padding='30 15 30 15', style='Background.TFrame')
        settings_container.grid(row=0, column=0, sticky='EW', padx=10, pady=10)
        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(0, weight=1)

        pomodoro_label = ttk.Label(settings_container, text='Pomodoro: ', style='LightText.TLabel')
        pomodoro_label.grid(row=0, column=0, sticky='W')

        pomodoro_input = tk.Spinbox(settings_container, textvariable=controller.pomodoro, from_=0, to=120, justify='center', increment=1, width=10)
        pomodoro_input.grid(row=0, column=1, sticky='EW')

        short_break_label = ttk.Label(settings_container, text='Short Break: ', style='LightText.TLabel')
        short_break_label.grid(row=1, column=0, sticky='W')

        short_break_input = tk.Spinbox(settings_container, textvariable=controller.short_break, from_=0, to=120, justify='center', increment=1, width=10)
        short_break_input.grid(row=1, column=1, sticky='EW')

        long_break_label = ttk.Label(settings_container, text='Long Break: ', style='LightText.TLabel')
        long_break_label.grid(row=2, column=0, sticky='W')

        long_break_input = tk.Spinbox(settings_container, textvariable=controller.long_break, from_=0, to=120, justify='center', increment=1, width=10)
        long_break_input.grid(row=2, column=1, sticky='EW')

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self)
        button_container.grid(sticky='EW', padx=10)
        button_container.columnconfigure(0, weight=1)

        back_button = ttk.Button(button_container, text='Back', command=show_timer, style='PomodoroButton.TButton')
        back_button.grid(row=1, column=0, sticky='EW', padx=2)