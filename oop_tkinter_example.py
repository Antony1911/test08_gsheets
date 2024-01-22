from tksheet import Sheet
import tkinter as tk

partner = 'wasaBet'
HEADERS = ['Name', 'CMS key', partner, 'Remote Config']
DATA = []

class Partner(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        

class show_tablet(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        
        self.sheet = Sheet(self.frame,
                           data = DATA,
                           zoom = 150,
                           auto_resize_columns = 0,
                           headers=HEADERS,
                           theme="dark",
                           width=1400,
                           height=800,
                           set_all_heights_and_widths=1
                            
                           
                           )
        self.sheet.enable_bindings()
        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")


app = show_tablet()
app.mainloop()