from yahoo_something import *

if __name__ == "__main__":
    print("Hello there Aaron Figgyman")
    t = TestYahoosomething()
    t.setup_method(None)
    t.test_yahoosomething()
    t.teardown_method(None)

    # TODO: get firefox to close after it's done 