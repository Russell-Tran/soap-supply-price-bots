import gspread

gc = gspread.service_account(filename='config/service_account.json')

sh = gc.open("fantastic-engine")

print(sh.sheet1.get('A1'))