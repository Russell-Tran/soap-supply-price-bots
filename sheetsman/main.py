import sheetsman
import selbots

SPREADSHEET_DOCUMENT_NAME_HERE = 'cs_191_bot_scrape'

if __name__ == "__main__":
    for i in range(2, 17):
        sheetsman.fulfill(SPREADSHEET_DOCUMENT_NAME_HERE, i)
