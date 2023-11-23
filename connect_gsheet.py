import gspread
from oauth2client.service_account import ServiceAccountCredentials
import PySimpleGUI as sg

def get_gsheet_data():
    scope = ['https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("geo_list").sheet1
    return sheet


def print_result(sheet = get_gsheet_data()):
    # ключи смс
    for val in sheet.col_values(1):
        if len(val)>0:
            print(val)


def choose_project():
    pass


def show_tablet():
    sg.theme('Dark2')
    
    # there are test values // real values 'll get from "get_gsheet_data"
    headers = ['country', 'id', 'value']

    fields = [
        ['USA, Florida', 'id 153', '{ "Success": true, "Value": { "City": "Джексонвилл", "Region": "Флорида", "Country": "США", "CountryCode": "US", "CityId": 26292, "RegionId": 1697, "CountryId": 153, "Continent": "NA", "Ip": "171.22.76.4" } }'],
        ['Ангилья','id 10','{ "Success": true, "Value": { "Country": "Ангилья", "CountryCode": "AI", "CityId": 0, "RegionId": 0, "CountryId": 10, "Continent": "NA", "Ip": "5.62.58.9" } }'],
        ['Антигуа и Барбуда','id 12','{ "Success": true, "Value": { "Country": "Антигуа и Барбуда", "CountryCode": "AG", "CityId": 0, "RegionId": 0, "CountryId": 12, "Continent": "NA", "Ip": "5.62.56.15" } }'],
              ]

    layout = [
        [sg.Table(
            values=fields, headings=headers,
            auto_size_columns=1,
            # display_row_numbers=1,
            justification='right',
            num_rows=10,
            key='tablet',
            row_height=35,
            # select_mode=sg.TABLE_SELECT_MODE_BROWSE
            )
        ]
    ]

    window = sg.Window('test_tablet title', layout)
    while True:
        event, value = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    
    window.close()






show_tablet()











# access data
# print(sheet.get_all_records())
# print(sheet.row_values(2))
# print(sheet.cell(2,1).value)
# print(sheet.col_values(11))






# cell_list = sheet.findall('Логин')
# for cell in cell_list:
#     print(cell.value, ' ', cell.row, ' ', cell.col)
