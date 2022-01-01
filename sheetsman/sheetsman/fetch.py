import json
import selbots.common as common
import gspread
import multiprocessing
import selbots.picking

CONVERT = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def sanity(sheetdocname):
    gc = gspread.service_account(filename='config/service_account.json')
    sh = gc.open(sheetdocname)
    return sh.worksheet("sanity").get('A1')

def worker(datum):
    row, product_url, columns, sheetdocname = datum
    gc = gspread.service_account(filename='config/service_account.json')
    sh = gc.open(sheetdocname)
    sheet = sh.sheet1
    print(f"Working on {product_url}...")
    bot = selbots.selbots.picking.pick(product_url)
    profile = common.Profile({
        "first_name" : "John",
        "last_name" : "Snow",
        "email" : "winteriscoming@gmail.com",
        "phone" : "(949) 361-8200",
        "fax" : "(949) 493-8729",
        "company" : "Cool Soap, Inc.",
        "address" : "15 Calle Loyola",
        "address_2" : "Suite #15",
        "city" : "San Clemente",
        "state" : "California",
        "country" : "United States",
        "zipcode" : "92673"
    })
    result = generic_sim(bot, profile, product_url)
    subtotal_col = columns['subtotal']
    fees_col = columns['fees']
    tax_col = columns['tax']
    shipping_col = columns['shipping']
    total_col = columns['total']
    sheet.update(CONVERT[subtotal_col] + str(row), result.subtotal)
    sheet.update(CONVERT[fees_col] + str(row), result.fees)
    sheet.update(CONVERT[tax_col] + str(row), result.tax)
    sheet.update(CONVERT[shipping_col] + str(row), result.shipping)
    sheet.update(CONVERT[total_col] + str(row), result.total)

    print(f"Done! {result}")
    
def fulfill(sheetdocname):
    gc = gspread.service_account(filename='config/service_account.json')
    sh = gc.open(sheetdocname)
    sheet = sh.sheet1
    column_header = sheet.row_values(1)

    product_url_col = column_header.index("product_url") + 1
    subtotal_col = product_url_col + 1
    fees_col = subtotal_col + 1
    tax_col = fees_col + 1
    shipping_col = tax_col + 1
    total_col = shipping_col + 1

    sheet.update(CONVERT[subtotal_col] + "1", "subtotal")
    sheet.update(CONVERT[fees_col] + "1", "fees")
    sheet.update(CONVERT[tax_col] + "1", "tax")
    sheet.update(CONVERT[shipping_col] + "1", "shipping")
    sheet.update(CONVERT[total_col] + "1", "total")



    columns = {
        'subtotal' : subtotal_col,
        'fees' : fees_col,
        'tax' : tax_col,
        'shipping' : shipping_col,
        'total' : total_col
    }

    product_urls = sheet.col_values(product_url_col)[1:]
    print(f"product_url values:\n {product_urls}")

    input_data = [(i+2, product_urls[i], columns, sheetdocname) for i in range(len(product_urls))]
    p = multiprocessing.Pool(6)
    p.map(worker, input_data)
    
def generic_sim(b: common.Bot, profile: common.Profile, product_url: str) -> common.Result:
    b.start()
    try:
        result = b.run(product_url, profile)
    except Exception as e:
        if b.headless:
            b.stop()
        raise e
    if b.headless:
        b.stop()
    return result