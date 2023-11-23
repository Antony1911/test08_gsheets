import gspread

gc = gspread.service_account(filename="C:\\repo\\test08_gsheets\\credentials.json")

sh = gc.open("geo_list")
sh = sh.create('A new spreadsheet')
print(sh.sheet1.get('A1'))