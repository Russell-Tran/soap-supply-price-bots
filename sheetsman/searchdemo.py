import sheetsman
import pendulum

if __name__ == '__main__':
    #sheetsman.elasticsearch.search()

    operator = sheetsman.SheetOperator("fantastic-engine")
    operator.paste_config_layout()
    operator.orchestrate()
    print()