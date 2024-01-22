import gspread
from oauth2client.service_account import ServiceAccountCredentials
import PySimpleGUI as sg

def get_partner():
        layout = [
            [sg.Text(f"partner")],
            [sg.Input(size=40, key='SEARCH', enable_events=True)],
            [sg.Listbox(partners, size=(40, 15), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, key='LISTBOX')],
            [sg.Button('Ok', size=(10, 1))],
        ]
        window = sg.Window("", layout, finalize=True)
        while True:
            event, values = window.read(close=False)
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            
            search = values['SEARCH']
            if values['SEARCH'] != '':
                new_values = [x for x in partners if search.title() in x]
                window.Element('LISTBOX').Update(new_values)
            else:
                window.Element('LISTBOX').Update(partners)
            
        window.close()

def show_tablet():
    row_list = []
    col_list = []
    
    layout = [
        [sg.Table(
            values = col_list, headings=row_list,
            auto_size_columns = 1,
            vertical_scroll_only = 0,
            justification = 'center',
            num_rows = 30,
            key = 'tablet',
            selected_row_colors=('yellow', None),
            alternating_row_color=('#383734'),
            # font="Consolas"
            font=(None, 15),
            enable_events=True,
            expand_x=True,
            expand_y=True,
            enable_click_events=True,
            )
        ]
    ]
    window = sg.Window('test_tablet title', layout, resizable=1)
    while True:
        event, value = window.read()
        try:
            window.TKroot.title(col_list[value['tablet']])
        except(TypeError):
            pass
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()



if __name__ == '__main__':
    sg.theme('DarkGrey15')
    scope = ['https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("partners-408812-1e1ad75adee7.json", scope)
    client = gspread.authorize(creds)
    # sheet = client.open("Мобильные приложения (ссылки, версии, даты релизов)").sheet1
    
    sheet_android = client.open("Мобильные приложения (ссылки, версии, даты релизов)").worksheet('Андроид')
    sheet_ios = client.open("Мобильные приложения (ссылки, версии, даты релизов)").worksheet('iOS')
    
    partners = sheet_android.col_values(1)
    
    get_partner()