# import PySimpleGUI as psg
# psg.set_options(font=("Arial Bold", 14))
# toprow = ['S.No.', 'Name', 'Age', 'Marks']
# rows = [[1, 'Rajeev', 23, 78],
#         [2, 'Rajani', 21, 66],
#         [3, 'Rahul', 22, 60],
#         [4, 'Robin', 20, 75]]
# tbl1 = psg.Table(values=rows, headings=toprow,
#    auto_size_columns=True,
#    display_row_numbers=False,
#    justification='center', key='-TABLE-',
#    selected_row_colors='red on yellow',
#    enable_events=True,
#    expand_x=True,
#    expand_y=True,
#  enable_click_events=True)
# layout = [[tbl1]]
# window = psg.Window("Table Demo", layout, size=(715, 200), resizable=True)
# while True:
#    event, values = window.read()
#    print("event:", event, "values:", values)
#    if event == psg.WIN_CLOSED:
#       break
#    if '+CLICKED+' in event:
#       psg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
# window.close()



col_list = [[], [], [], []]
test = ['123']

col_list[2] = test


print(col_list)
# dd_list = ['Ключ в CMS', '', '', '', '', '', '', '', 'hasSnapshot = true', 'ReferalLink = ""', 'ReferalLink = ""', 'isBettingEnabled = true', 'BettingEnabledGeo = string_array']
# print(dd_list[1:])
    




# import PySimpleGUI as sg

# headings = ['President', 'Date of Birth']
# data = [
#     ['Ronald Reagan', 'February 6'],
#     ['Abraham Lincoln', 'February 12'],
#     ['George Washington', 'February 22'],
#     ['Andrew Jackson', 'March 15'],
#     ['Thomas Jefferson', 'April 13'],
#     ['Harry Truman', 'May 8'],
#     ['John F. Kennedy', 'May 29'],
#     ['George H. W. Bush', 'June 12'],
#     ['George W. Bush', 'July 6'],
#     ['John Quincy Adams', 'July 11'],
#     ['Garrett Walker', 'July 18'],
#     ['Bill Clinton', 'August 19'],
#     ['Jimmy Carter', 'October 1'],
#     ['John Adams', 'October 30'],
#     ['Theodore Roosevelt', 'October 27'],
#     ['Frank Underwood', 'November 5'],
#     ['Woodrow Wilson', 'December 28'],
# ]

# sg.theme('DarkBlue3')
# sg.set_options(("Courier New", 12))

# layout = [
#     [sg.Button('Change')],
#     [sg.Table(data, headings=headings, visible_column_map=[True, False],
#         justification='left', select_mode=sg.TABLE_SELECT_MODE_BROWSE,
#         enable_events=True, metadata=False, key='President')],
#     [sg.Text('', size=(22, 1), key='Birthday')],
# ]
# window = sg.Window("Title", layout, finalize=True)
# president = window['President']

# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     elif event == 'President':
#         index = values[event][0]
#         window['Birthday'].update(value=f'Birthday: {data[index][1]}')
#     elif event == 'Change':
#         show = president.metadata = not president.metadata
#         displaycolumns = ['President', 'Date of Birth'] if show else ['President']
#         president.Widget.configure(displaycolumns=displaycolumns)

# window.close()