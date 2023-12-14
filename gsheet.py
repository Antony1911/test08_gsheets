import gspread
from oauth2client.service_account import ServiceAccountCredentials
import PySimpleGUI as sg
import pyperclip

def get_correct_name_list(name_list):
    corrected_list = []
    for sub_list in name_list:
        sub_list_index = name_list.index(sub_list)
        
        temp_list = []
        for sub in sub_list:
            sub_index = sub_list.index(sub)
            
            count_void = sub_list.count('')
            num = 0
            
            if sub == '':
                try:
                    while count_void != num:
                        sub = corrected_list[sub_list_index - 1][sub_index + num]
                        if sub not in temp_list:
                            temp_list.append(sub)
                        num = num + 1
                except:
                    pass
            else:
                temp_list.append(sub)
                
        corrected_list.append(temp_list)
    return corrected_list

def get_checklist_for_partner():
        
    row_list = ['Name', 'CMS key', 'Основа', f'{partner_name}', '']
    col_list = []
    
    get_name_col = sheet.get('B:F')
    name_col = get_correct_name_list(get_name_col)
    
    key_col = sheet.col_values(11)
    main_col = sheet.col_values(13)
    indx = partners.index(partner_name)
    partner_col = sheet.col_values(13 + indx)

    for i in range(0, 435):
        temp_list_add_to_col_list = []
        temp_list_add_to_col_list.append(name_col[i])
        temp_list_add_to_col_list.append(key_col[i])
        temp_list_add_to_col_list.append(main_col[i])
        temp_list_add_to_col_list.append(partner_col[i])
        
        col_list.append(temp_list_add_to_col_list)
    print(col_list)
    # https://docs.google.com/spreadsheets/d/1Ebof_JtrKXJiUmCKPnP_tbWAtfGjA-cINeQXhbxkuzQ/edit#gid=1628117538
    return row_list, col_list

def create_partner_list():
    temp_list = sheet.row_values(1)
    except_list = ['','Функционал на сайте', 'Базовый', 'Android', 'iOS', 'Ключ в CMS', 'Настраивается']
    partners = []
    for i in temp_list:
        if i not in partners:
            if i not in except_list:
                partners.append(i)
    return partners

def get_partner_names():
        layout = [
            [sg.Text(f"Choose partner (available = {len(partners)})")],
            [sg.Input(size=40, key='SEARCH', enable_events=True)],
            [sg.Listbox(partners, size=(40, 15), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, key='LISTBOX')],
            [sg.Button('Submit')],
        ]
        window = sg.Window('choose partner', layout, finalize=True)
        # window['SEARCH'].bind("<Return>", "+RETURN")
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            search = values['SEARCH']
            if values['SEARCH'] != '':
                new_values = [x for x in partners if search.title() in x]
                window.Element('LISTBOX').Update(new_values)
            else:
                window.Element('LISTBOX').Update(partners)
            
            if event == 'Submit':
                selected = values['LISTBOX']
                return selected
        window.close()

def show_tablet():
    row_list, col_list = get_checklist_for_partner()
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
            # display_row_numbers = 1
            
            )
        ]
    ]

    window = sg.Window('test_tablet title', layout, resizable=1)
    
    while True:
        event, value = window.read()
        # s_val = value['tablet']
                
        try:
            window.TKroot.title(col_list[value['tablet']])
        except(TypeError):
            pass
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
        # if event == 'tablet':
        #     print(col_list[value['tablet']])
        
        # re_val = value['tablet']
        if '+CLICKED+' in event:
            try:
                window.TKroot.title(col_list[value['tablet']])
            except(TypeError):
                pass
            # pyperclip.copy(event['tablet'])
            print('12345978')
    window.close()



if __name__ == '__main__':
    sg.theme('Dark2')
    scope = ['https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    # sheet = client.open("geo_list").sheet1
    sheet = client.open("Характеристики (сайты и приложения)").sheet1
    partners = create_partner_list()
    partner_name = get_partner_names()[0]
    
    
    print(partner_name)
    show_tablet()

    # ключ смс
    # print(sheet.col_values(11))
    
    # основа
    # print(sheet.col_values(13))
    
    # print(sheet.col_values(14))
    




# access data
# # print(sheet.col_values(4))
# print(sheet.get_all_records())
# print(sheet.row_values(2))
# print(sheet.cell(2,1).value)
# print(sheet.col_values(11))
# cell_list = sheet.findall('Логин')
# for cell in cell_list:
#     print(cell.value, ' ', cell.row, ' ', cell.col)
