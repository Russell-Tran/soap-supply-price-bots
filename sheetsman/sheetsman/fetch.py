import json
import selbots.common as common
import gspread
import multiprocessing
import selbots.picking
import pendulum
from .elasticsearch import *

CONVERT = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# ===== DEV CONSTANTS =====
PROFILE_CALIFORNIA = common.Profile({
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


# ============================


def sanity(sheetdocname):
    gc = gspread.service_account(filename='config/service_account.json')
    sh = gc.open(sheetdocname)
    return sh.worksheet("sanity").get('A1')

def worker(datum):
    try:
        row, product_url, columns, sheetdocname, target_qty, sheetidx = datum
    except:
        row, product_url, columns, sheetdocname, target_qty = datum
        sheetidx = 0
    gc = gspread.service_account(filename='config/service_account.json')
    sh = gc.open(sheetdocname)
    sheet = sh.get_worksheet(sheetidx)
    print(f"Working on {product_url}...")
    bot = selbots.selbots.picking.pick(product_url)

    # === HARDCODED ===
    profile = PROFILE_CALIFORNIA
    # =================

    try:
        result = generic_sim(bot, profile, product_url, target_qty)
    except Exception as e:
        print(e)
        return
    size_col = columns['size']
    subtotal_col = columns['subtotal']
    fees_col = columns['fees']
    tax_col = columns['tax']
    shipping_col = columns['shipping']
    total_col = columns['total']
    size_base_units_col = columns['size_base_units']

    sheet.update(CONVERT[size_col] + str(row), str(result.size))
    sheet.update(CONVERT[subtotal_col] + str(row), result.subtotal)
    sheet.update(CONVERT[fees_col] + str(row), result.fees)
    sheet.update(CONVERT[tax_col] + str(row), result.tax)
    sheet.update(CONVERT[shipping_col] + str(row), result.shipping)
    sheet.update(CONVERT[total_col] + str(row), result.total)
    sheet.update(CONVERT[size_base_units_col] + str(row), str(result.size.to_base_units()))

    print(f"Done! {result}")
    
def fulfill(sheetdocname, sheetidx=0):
    print(f"FULFILLING SHEET {sheetidx}")
    gc = gspread.service_account(filename='config/service_account.json')
    sh = gc.open(sheetdocname)
    sheet = sh.get_worksheet(sheetidx)

    config_sheet = sh.get_worksheet(1)
    target_qty = config_sheet.acell('A1').value
    target_qty = common.extract_quantity(target_qty)
    print(f"target quantity is {target_qty}")

    column_header = sheet.row_values(1)

    product_url_col = column_header.index("product_url") + 1
    size_col = product_url_col + 1
    subtotal_col = size_col + 1
    fees_col = subtotal_col + 1
    tax_col = fees_col + 1
    shipping_col = tax_col + 1
    total_col = shipping_col + 1
    size_base_units_col = total_col + 1

    sheet.update(CONVERT[size_col] + "1", "size")
    sheet.update(CONVERT[subtotal_col] + "1", "subtotal")
    sheet.update(CONVERT[fees_col] + "1", "fees")
    sheet.update(CONVERT[tax_col] + "1", "tax")
    sheet.update(CONVERT[shipping_col] + "1", "shipping")
    sheet.update(CONVERT[total_col] + "1", "total")
    sheet.update(CONVERT[size_base_units_col] + "1", "size_base_units")



    columns = {
        'size' : size_col,
        'subtotal' : subtotal_col,
        'fees' : fees_col,
        'tax' : tax_col,
        'shipping' : shipping_col,
        'total' : total_col,
        'size_base_units' : size_base_units_col
    }

    product_urls = sheet.col_values(product_url_col)[1:]
    print(f"product_url values:\n {product_urls}")

    input_data = [(i+2, product_urls[i], columns, sheetdocname, target_qty, sheetidx) for i in range(len(product_urls))]
    p = multiprocessing.Pool(6)
    p.map(worker, input_data)
    
def generic_sim(b: common.Bot, profile: common.Profile, product_url: str, target_qty) -> common.Result:
    b.start()
    try:
        result = b.run(product_url, profile, target_qty)
    except Exception as e:
        if b.headless:
            b.stop()
        raise e
    if b.headless:
        b.stop()
    return result

class SheetOperator:
    CONFIG_LAYOUT = [
        "query_raw",
        "target_qty",
        "address",
        "city",
        "state",
        "country",
        "zipcode"
    ]

    def __init__(self, sheetdocname):
        self.sheetdocname = sheetdocname
        gc = gspread.service_account(filename='config/service_account.json')
        self.sh = gc.open(sheetdocname)
    
    def paste_config_layout(self):
        sh = self.sh
        try:
            worksheet = sh.worksheet("config")
        except:
            worksheet = sh.add_worksheet(title="config", rows=1000, cols=26)
        for i, parameter in enumerate(self.CONFIG_LAYOUT):
            row_number = i + 1
            worksheet.update(f'A{row_number}', parameter)

    def get_config(self):
        sh = self.sh
        worksheet = sh.worksheet("config")
        output = {}
        for i, parameter in enumerate(self.CONFIG_LAYOUT):
            row_number = i + 1
            output[parameter] = worksheet.acell(f'B{row_number}').value
        return output

    def create_result_sheet(self):
        sh = self.sh
        return sh.add_worksheet(title=str(pendulum.now("America/Los_Angeles")), rows=1000, cols=26)

    def paste_search_results(self, worksheet, results):
        ROW_OFFSET = 2
        for i, result in enumerate(results):
            row_number = i + ROW_OFFSET
            url = result['url']
            worksheet.update(f'A{row_number}', url)
            try:
                title = result['title']
                worksheet.update(f'B{row_number}', title)
            except:
                pass

    def run_fulfillment(self, sheet, target_qty):
        column_header = sheet.row_values(1)

        product_url_col = column_header.index("product_url") + 1
        title_url_col = product_url_col + 1
        size_col = title_url_col + 1
        subtotal_col = size_col + 1
        fees_col = subtotal_col + 1
        tax_col = fees_col + 1
        shipping_col = tax_col + 1
        total_col = shipping_col + 1

        sheet.update(CONVERT[product_url_col] + "1", "product_url")
        sheet.update(CONVERT[title_url_col] + "1", "product_title")
        sheet.update(CONVERT[size_col] + "1", "size")
        sheet.update(CONVERT[subtotal_col] + "1", "subtotal")
        sheet.update(CONVERT[fees_col] + "1", "fees")
        sheet.update(CONVERT[tax_col] + "1", "tax")
        sheet.update(CONVERT[shipping_col] + "1", "shipping")
        sheet.update(CONVERT[total_col] + "1", "total")

        columns = {
            'size' : size_col,
            'subtotal' : subtotal_col,
            'fees' : fees_col,
            'tax' : tax_col,
            'shipping' : shipping_col,
            'total' : total_col
        }

        product_urls = sheet.col_values(product_url_col)[1:]
        print(f"product_url values:\n {product_urls}")

        input_data = [(i+2, product_urls[i], columns, self.sheetdocname, target_qty) for i in range(len(product_urls))]
        p = multiprocessing.Pool(6)
        p.map(worker, input_data)

    def orchestrate(self):
        config = self.get_config()
        worksheet = self.create_result_sheet()
        query = config['query_raw']
        search_results = search(query)
        self.paste_search_results(worksheet, search_results)
        print(search_results)

        target_qty = config['target_qty'] # target_qty = common.extract_quantity(target_qty)
        self.run_fulfillment(worksheet, target_qty)

        

# NOTE: weird multiprocessing use of sheetdocname is required since you can't pickle the gspread objects directly

if __name__ == "__main__":
    print("helo werld")