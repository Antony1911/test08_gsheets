# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title('Treeview demo')
#         self.geometry('620x200')

#         self.tree = self.create_tree_widget()

#     def create_tree_widget(self):
#         columns = ('first_name', 'last_name', 'email')
#         tree = ttk.Treeview(self, columns=columns, show='headings')

#         # define headings
#         tree.heading('first_name', text='First Name')
#         tree.heading('last_name', text='Last Name')
#         tree.heading('email', text='Email')

#         tree.bind('<<TreeviewSelect>>', self.item_selected)
#         tree.grid(row=0, column=0, sticky=tk.NSEW)

#         # add a scrollbar
#         scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
#         tree.configure(yscroll=scrollbar.set)
#         scrollbar.grid(row=0, column=1, sticky='ns')

#         # generate sample data
#         contacts = []
#         for n in range(1, 100):
#             contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

#         # add data to the treeview
#         for contact in contacts:
#             tree.insert('', tk.END, values=contact)

#         return tree

#     def item_selected(self, event):
#         for selected_item in self.tree.selection():
#             item = self.tree.item(selected_item)
#             record = item['values']
#             # show a message
#             showinfo(title='Information', message=','.join(record))


# if __name__ == '__main__':
#     app = App()
#     app.mainloop()


import PySimpleGUI as sg
from PySimpleGUI import*



layout = [
# [B(SYMBOL_DOWN, pad=(0, 0), k='-HIDE TABS-'),
#     pin(Col([[TabGroup([[tab1, tab2, tab3, tab6, tab4, tab5, tab7, tab8, tab9]], 
#                        key='-TAB_GROUP-')]], k='-TAB GROUP COL-'))],

[sg.Button(SYMBOL_DOWN, pad=(0, 0), k='-HIDE TABS-'),
    pin(Col([[Listbox('', size=(25,10),key='-TAB_GROUP-', enable_events=True)]], k='-TAB GROUP COL-'))],



[sg.Button('Button', highlight_colors=('yellow', 'red'),pad=(1, 0)),
 sg.Button('Exit', tooltip='Exit button',pad=(1, 0))]]

window = sg.Window('', layout,
                finalize=True,
                enable_close_attempted_event=True,
                modal=False)

while True:
    event, value = window.read(close=True)
    
    if event == '-HIDE TABS-':
        window['-TAB GROUP COL-'].update(visible=window['-TAB GROUP COL-'].metadata == True)
        window['-TAB GROUP COL-'].metadata = not window['-TAB GROUP COL-'].metadata
        window['-HIDE TABS-'].update(text=SYMBOL_UP if window['-TAB GROUP COL-'].metadata else SYMBOL_DOWN)
    
    if event in ('Close', None) or event == sg.WIN_CLOSED:
        break
    window.close()