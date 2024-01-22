import PySimpleGUI as sg
import webbrowser
import pyperclip
import getpass
sg.theme('DarkBlue')

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_country():
        layout = [
            [sg.Text(f"Choose country (available = {len(countries)})")],
            [sg.Input(size=35, key='SEARCH', enable_events=True), sg.Button('Clear')],
            [sg.Listbox(countries, size=(40, 15), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, key='LISTBOX')],
            [sg.Button('Copy', size=(10, 1)), sg.Button('Go to geo_list', key='LINK', button_color="#0b68d9")],
        ]
        window = sg.Window(f'geo v0.21 [{getpass.getuser()}]', layout, finalize=True)
        while True:
            event, values = window.read(close=False)
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            
            if event == 'LINK':
                # link = "https://docs.google.com/spreadsheets/d/1H8LMowJnKyn-eqJQNLGk-0JpUB5PoBs8Ns4JDIeM-jo/edit?usp=sharing"
                link = "https://docs.google.com/spreadsheets/d/1wQvjk85tEePvITUwSPjp0rU8nbBD6rLS77Ut1GUT_tg/edit#gid=1822072927"
                webbrowser.open(link, new=0, autoraise=True)

            search = values['SEARCH']
            if values['SEARCH'] != '':
                new_values = [x for x in countries if search.title() in x]
                window.Element('LISTBOX').Update(new_values)
            else:
                window.Element('LISTBOX').Update(countries)
            
            if event == 'Clear':
                window.Element('SEARCH').Update('')
                window.Element('LISTBOX').Update(countries)
            
            if event == 'Copy':
                try:
                    selected = values['LISTBOX']
                    pyperclip.copy(cntr_info[countries.index(selected[0])])
                    
                    # sg.popup_auto_close('Copied!!', auto_close_duration=0.4, no_titlebar=1)
                    sg.popup_annoying('Copied!!')
                except(IndexError):
                    pass
        window.close()


# ----------------------------------------------------------------------
if __name__ == '__main__':
    sg.theme('Dark2')
    black_list = []
    scope = ['https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]
    
    key_jsfile = {
    "type": "service_account",
    "project_id": "changegeo",
    "private_key_id": "6ac20b5da1cad225008b2e095448046ef8f6a626",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC16ce/nYQ2NDZR\ntqJJWOzkQPo1ySeiP+pId2GObTqIymV2szD0RiYsuwf7g5cwn3YqcxVXaQXC2wTF\nIZINTg3j9jCJ2lBCxtK0ZuUmhZdlQ0j4mqkVqTeA9zknhUBw55ntWc3BV5lvXD53\nhFuqQTP3xjaxrexeg6zra9igVCPqYMdLVcgVCH6O6mjC5/Ju28vfOqa+w7qpe2S1\n1hBHCzNHHs5UlTVhjrddTlXCyUsgSLUfVeBrwGYN13To6qZsReyo6496XFiGyqn0\n1kpVh7CxJ8RDSPhDSNSlzpFPQQ78TKuprIoWGp+jKrsDyUvnk34uWtwQ9FSzC98z\nOEOWqbIlAgMBAAECggEAEQqnE0zS028dvZbx6hQiERoDNqGzDFCXhpVkdr7F0oW/\nbpjH18JwlhUpYMcJlV0C6WQhljA5AXGaJ0uHTqbGx1nLX0ar6S2OFKdlBTBTqAFf\nJyb5+xUApZzDZm/lww33ThRxIZEuxw9prLGiEreMAkS33/pOn+YO/3j5cL+hI7Yn\nqDI9aKgspft1rHR3HC9+hdtsSGbVeMT8Cfpw9dm0YmyMyE6Cl1hJz0vLASqtGEgd\nX4HWSt14kuyFF+6UcuP6Er+C/+6ebiOGglizdva1TjH5MVYPakc7JFY+aH/MIy2u\nbhvxP7OJJ1kJatsqnTrpG3qxBb+zINZwZia0Gwr2uwKBgQDtOAp05mw45cOztoum\nZP1zapJHE9+0ItMobUvhPZG6e3KGJsUDMymXPxx0cDBV24uRkT95OHBYUoK0v+UN\nJy3XUEP5X1VbaCJm4oxbFipGUbn8u5jsGTNEcSbLM8Yulw/MEQSe4cP/4sqkNp0Q\n2WslxKeNi2yEvXmG1qf3EsV9UwKBgQDEUM1KbhHzIqxXG6hZms29yT4k7Gm7nNeH\nMaYaQne7TBplSiJirl5n4BUjZL/EbAeaiG3EYqDIL2mD3jsPO4cVNjrkak9BeLmf\nak2HRMdArfmIQzCBkdIfFA2L6KR8Eq9T5gfJXHXHI6tXam4nu6NGh4W19Doyt7Cw\n3DHNZBgrpwKBgB4AxYnNjwiPPvZe80DDay8K3p9wyw18jhqB4GQHpoPgkzaWdrqV\n4P/JMq8jdWmWkAuERHPviH4TSYbU8oJ8Xxbphv9maGRcQmWi57+piQVF1vE5RPkv\nosVYTmDLFpjT8GKOEHiL839MzvaAFdOIvD2Vpt+HL92GHXXJdosQa7wTAoGBAJYF\n9cxyb08x6SgsX6wSTDZD6zTGYkrYojCTtY8NyngcwXM0gzCMdmLFcQH6RT5zHCBx\nMAlLIfm5mdYHZ3TNlf6U0c6qm2S6QIhd8V91JRv9l9sVFaV+7WeIqI2JvOGAWfIw\nsTSlbvA/BvqnwASnNTB58qnJOQx3KhUOQRTn8DyzAoGBAINagwwFUwbaL+/8OG/s\nfibefrbzPbcIz7UdAMqfOUklY1Db16VhIY6IWd7wDCtIujtiZVeGvhTq/o4kAtQ5\n2dCyJd0NbopAYYcLAc+CdUiA8FiAWJW8Z/o0fWw2zQkca6YxOo6EvqpoXxz6HMOP\npSqLzDK3t+o2fm/P5c+gwRTL\n-----END PRIVATE KEY-----\n",
    "client_email": "changegeo@changegeo.iam.gserviceaccount.com",
    "client_id": "113877804435623252598",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/changegeo%40changegeo.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
                }
    
    creds = ServiceAccountCredentials.from_json_keyfile_dict(key_jsfile, scope)
    client = gspread.authorize(creds)
    sheet = client.open("Гео").sheet1
    
    countries = sheet.col_values(3)
    cntr_info = sheet.col_values(5)
    
    get_country()