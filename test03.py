# from tkinter import *
# rows = []
# for i in range(5):
#     cols = []
#     for j in range(4):
#         e = Entry(relief=GROOVE)
#         e.grid(row=i, column=j, sticky=NSEW)
#         e.insert(END, '%d.%d' % (i, j))
#         cols.append(e)
#     rows.append(cols)

# mainloop()


# ----------------
# this
# ----------------
import tkinter as tk
import tksheet
top = tk.Tk()
sheet = tksheet.Sheet(top)
sheet.grid()
sheet.set_sheet_data([[f"{ri+cj}" for cj in range(4)] for ri in range(1)])
# table enable choices listed below:
sheet.enable_bindings(("single_select",
                       "row_select",
                       "column_width_resize",
                       "arrowkeys",
                       "right_click_popup_menu",
                       "rc_select",
                       "rc_insert_row",
                       "rc_delete_row",
                       "copy",
                       "cut",
                       "paste",
                       "delete",
                       "undo",
                    #    "edit_cell"
                       ))
top.mainloop()





# import time
# import tkinter as tk
# import tkinter.ttk as ttk
# from threading import Thread

# gui = tk.Tk()
# gui.geometry('360x270')
# gui.configure(bg='white')

# style = ttk.Style()
# style.theme_create('custom', settings={
#     'header.TLabel': {'configure': {
#         'background': 'white',
#         'foreground': 'dark green',
#         'font': 'Times 16 bold',
#         'padding': (10, 0)}},
#     'TLabel': {'configure': {'background': 'white', 'font': 'Times 12'}},
#     'TFrame': {'configure': {'background': 'white'}}})
# style.theme_use('custom')

# table_frame = ttk.Frame(gui)
# table_frame.pack(pady=(36, 0))

# values = [('Count', 'Date', 'Time', 'Phrase'),
#           ('5', '12/12/10', '03:15', 'blue car'),
#           ('13', '09/09/98', '16:20', 'red door')]

# total_rows = len(values)
# total_columns = len(values[0])

# for i in range(total_rows):
#     for j in range(total_columns):
#         if i == 0:
#             label = ttk.Label(table_frame, text=values[i][j], style='header.TLabel')
#             label.grid(row=i, column=j)
#         elif i == 1:
#             if j == 0:
#                 count1 = tk.StringVar()
#                 count1.set(values[i][j])
#                 label = ttk.Label(table_frame, textvariable=count1)
#                 label.grid(row=i, column=j)
#             else:
#                 label = ttk.Label(table_frame, text=values[i][j])
#                 label.grid(row=i, column=j)
#         elif i == 2:
#             if j == 0:
#                 count2 = tk.StringVar()
#                 count2.set(values[i][j])
#                 label = ttk.Label(table_frame, textvariable=count2)
#                 label.grid(row=i, column=j)
#             else:
#                 label = ttk.Label(table_frame, text=values[i][j])
#                 label.grid(row=i, column=j)


# def increment_count():
#     increment_count.status = 'run'

#     while increment_count.status == 'run':
#         new_minute1 = int(count1.get()) + 1
#         count1.set(str(new_minute1))

#         new_minute2 = int(count2.get()) - 1
#         count2.set(str(new_minute2))

#         time.sleep(1)


# Thread(target=increment_count).start()

# gui.mainloop()
# increment_count.status = 'exit'