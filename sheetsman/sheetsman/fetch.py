import gspread

def fulfill(sheetdocname):
    gc = gspread.service_account(filename='config/service_account.json')
    sh = gc.open(sheetdocname)
    sheet = sh.sheet1
    column_header = sheet.row_values(1)
    col_idx = column_header.index("product_url") + 1
    print("product_url values:")
    print(sheet.col_values(col_idx)[1:])

def sanity(docname):
    gc = gspread.service_account(filename='config/service_account.json')
    sh = gc.open(sheetdocname)
    return sh.worksheet("sanity").get('A1')