import gspread
from oauth2client.service_account import ServiceAccountCredentials
import PySimpleGUI as sg
import pyperclip


def get_checklist_for_partner():
    # row_list = ['Name', 'CMS key', 'Основа', f'{partner_name}']
    # col_list = [['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True],
    #             ['По телефону по умолчанию', 'isDefaultLoginByPhone = true', False, True],
    #             ['E-mail и ID', 'isAllowedLoginByEmailAndId = true', False, True],
    #             ['Логин', 'isAllowedLoginByLogin = false', False, True],
    #             ['Ввод кода страны вручную', 'isAllowedCustomPhoneCodeInput = true', False, True],
    #             ['Через соц. сети', 'isAllowedLoginBySocial = false', False, True]
    #             ]
    
        
    row_list = ['Name', 'CMS key', 'Основа', f'{partner_name}']
    col_list = [[], [], [], []]
    col_list[2] = sheet.col_values(13)
    
    print(col_list)
    return row_list, col_list

def get_partner_names():
    temp_list = sheet.row_values(1)
    except_list = ['','Функционал на сайте', 'Базовый', 'Android', 'iOS', 'Ключ в CMS', 'Настраивается']
    partners = []
    
    for i in temp_list:
        if i not in partners:
            if i not in except_list:
                partners.append(i)
    
    layout = [
        [sg.Text(f"Choose partner (available = {len(partners)})")],
        [sg.DropDown(values=partners, default_value=partners[0], auto_size_text=True, key='-DROPDOWN-')],
        [sg.Button('get', size=10)]
    ]
    
    window = sg.Window('partners list', layout)
    while True:
        event, value = window.read(close=True)
        
        if event == 'get':
            selected_partner = value['-DROPDOWN-']
            return selected_partner
            
        if event in ('Cancel', None) or event == sg.WIN_CLOSED:
            exit(0)
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
            font=(None, 17),
            enable_events=True,
            expand_x=True,
            expand_y=True,
            enable_click_events=True
            )
        ]
    ]

    window = sg.Window('test_tablet title', layout, resizable=1)
    while True:
        event, value = window.read()
                    
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if '+CLICKED+' in event:
            # val = value['tablet'][0]
            # pyperclip.copy(val)
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
    partner_name = get_partner_names()
    
    
    print(partner_name)
    show_tablet()

    # ключ смс
    # print(sheet.col_values(11))
    
    # основа
    # print(sheet.col_values(13))
    
    print(sheet.col_values(14))
    




# access data
# # print(sheet.col_values(4))
# print(sheet.get_all_records())
# print(sheet.row_values(2))
# print(sheet.cell(2,1).value)
# print(sheet.col_values(11))
# cell_list = sheet.findall('Логин')
# for cell in cell_list:
#     print(cell.value, ' ', cell.row, ' ', cell.col)
