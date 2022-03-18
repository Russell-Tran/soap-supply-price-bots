import matplotlib.pyplot as plt
from csv import reader
import matplotlib.ticker as mtick
import numpy as np
from adjustText import adjust_text

def p2f(x):
    return float(x.strip('%'))/100

def example():
    # https://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point
    y = [2.56422, 3.77284, 3.52623, 3.51468, 3.02199]
    z = [0.15, 0.3, 0.45, 0.6, 0.75]
    n = [58, 651, 393, 203, 123]

    fig, ax = plt.subplots()
    ax.scatter(z, y)

    for i, txt in enumerate(n):
        ax.annotate(txt, (z[i], y[i]))

    plt.show()
    
def ecommerce_scatter_old():
    # read csv file as a list of lists
    with open('ecommerce_results.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)

    labels = list_of_rows[0][1:]
    mean = [float(x) for x in list_of_rows[1][1:]]
    percentstddev = [p2f(x) for x in list_of_rows[3][1:]]

    outlier_idx = labels.index("chamomile eo")
    labels = labels[:outlier_idx] + labels[outlier_idx+1:]
    mean = mean[:outlier_idx] + mean[outlier_idx+1:]
    percentstddev = percentstddev[:outlier_idx] + percentstddev[outlier_idx+1:]

    y = percentstddev
    z = mean
    n = labels

    fig, ax = plt.subplots()
    ax.xaxis.set_ticks(np.arange(0, 550, 100))
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    ax.scatter(z, y)

    for i, txt in enumerate(n):
        ax.annotate(txt, (z[i], y[i]+.01), rotation=20, fontsize=8)

    plt.show()
    return

def ecommerce_scatter():
    # read csv file as a list of lists
    with open('ecommerce_results.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)

    labels = list_of_rows[0][1:]
    mean = [float(x) for x in list_of_rows[1][1:]]
    percentstddev = [p2f(x) for x in list_of_rows[3][1:]]

    outlier_idx = labels.index("chamomile eo")
    labels = labels[:outlier_idx] + labels[outlier_idx+1:]
    mean = mean[:outlier_idx] + mean[outlier_idx+1:]
    percentstddev = percentstddev[:outlier_idx] + percentstddev[outlier_idx+1:]

    y = percentstddev
    z = mean
    n = labels

    fig, ax = plt.subplots()
    #ax.xaxis.set_ticks(np.arange(0, 550, 100))
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    ax.scatter(z, y)

    annotations = []
    for i, txt in enumerate(n):
        annotations.append(ax.annotate(txt, (z[i], y[i]+0.01), rotation=00, fontsize=8))

    adjust_text(annotations)

    plt.xlim([0, 500])
    plt.title('Price variation for k=17 soapmaking ingredients among top 10 independent ecommerce sites (March 2022)')
    plt.xlabel('Mean price ($/kg) [n=5]')
    plt.ylabel('StdDev (%)')
    #plt.show()
    save("ecommerce_scatter.png")
    return

def amazon_scatter():
    # read csv file as a list of lists
    with open('amazon.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)

    labels = list_of_rows[0][1:]
    mean = [float(x) for x in list_of_rows[3][1:]]
    percentstddev = [p2f(x) for x in list_of_rows[5][1:]]

    outlier_idx = labels.index("chamomile eo")
    labels = labels[:outlier_idx] + labels[outlier_idx+1:]
    mean = mean[:outlier_idx] + mean[outlier_idx+1:]
    percentstddev = percentstddev[:outlier_idx] + percentstddev[outlier_idx+1:]

    y = percentstddev
    z = mean
    n = labels

    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    ax.scatter(z, y)

    annotations = []
    for i, txt in enumerate(n):
        annotations.append(ax.annotate(txt, (z[i], y[i]+0.01), rotation=00, fontsize=8))

    adjust_text(annotations, arrowprops=dict(arrowstyle='->', color='red'))

    plt.xlim([0, 500])
    plt.title('Price variation for k=17 soapmaking ingredients on Amazon (March 2022)')
    plt.xlabel('Mean price ($/kg) [n=5]')
    plt.ylabel('StdDev (%)')
    #plt.show()
    save("amazon_scatter.png")
    return

def superimposed_scatter():

    """ECOMMERCE"""
    # read csv file as a list of lists
    with open('ecommerce_results.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)

    labels = list_of_rows[0][1:]
    mean = [float(x) for x in list_of_rows[1][1:]]
    percentstddev = [p2f(x) for x in list_of_rows[3][1:]]

    outlier_idx = labels.index("chamomile eo")
    labels = labels[:outlier_idx] + labels[outlier_idx+1:]
    mean = mean[:outlier_idx] + mean[outlier_idx+1:]
    percentstddev = percentstddev[:outlier_idx] + percentstddev[outlier_idx+1:]

    y = percentstddev
    z = mean
    n = labels

    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    ax.scatter(z, y, label="Independent")

    # trendline
    z = np.polyfit(mean, percentstddev, 1)
    p = np.poly1d(z)
    plt.plot(mean,p(mean),"b-")

    # annotations = []
    # for i, txt in enumerate(n):
    #     annotations.append(ax.annotate(txt, (z[i], y[i]), rotation=00, fontsize=8))

    # adjust_text(annotations)

    """AMAZON"""
    # read csv file as a list of lists
    with open('amazon.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)

    labels = list_of_rows[0][1:]
    mean = [float(x) for x in list_of_rows[3][1:]]
    percentstddev = [p2f(x) for x in list_of_rows[5][1:]]

    outlier_idx = labels.index("chamomile eo")
    labels = labels[:outlier_idx] + labels[outlier_idx+1:]
    mean = mean[:outlier_idx] + mean[outlier_idx+1:]
    percentstddev = percentstddev[:outlier_idx] + percentstddev[outlier_idx+1:]

    y = percentstddev
    z = mean
    n = labels

    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    ax.scatter(z, y, label="Amazon")

    # trendline
    z = np.polyfit(mean, percentstddev, 1)
    p = np.poly1d(z)
    plt.plot(mean,p(mean),color='orange', linestyle='solid') #color='green', linestyle='dashed'

    # annotations = []
    # for i, txt in enumerate(n):
    #     annotations.append(ax.annotate(txt, (z[i], y[i]), rotation=00, fontsize=8))

    # adjust_text(annotations)

    """GENERAL"""
    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.xlim([0, 500])
    plt.title('Price variation for k=17 soapmaking ingredients on Amazon vs. independent web (March 2022)')
    plt.xlabel('Mean price ($/kg) [n=5]')
    plt.ylabel('StdDev (%)')
    #plt.show()
    save("superimposed.png")
    return

def declining_functionality():
    # https://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib
    import datetime as dt
    dates = ['01/10/2022','03/17/2022']
    x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
    y = [26/28, 25/(25+38)]
    import matplotlib.dates as mdates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=14))
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    plt.plot(x,y)
    for xy in zip(x, y):                                               
        plt.gca().annotate('({0}, {1:.0%})'.format(xy[0], xy[1]), xy=xy, textcoords='data')
    plt.gcf().autofmt_xdate()

    plt.title('Degradation of k=63 unit tests for price scraping bots on 10 ecommerce sites')
    plt.xlabel('Date of test rerun')
    plt.ylabel('Unit test pass rate')
    #plt.show()
    save("unittests.png")
    return


def usersurvey():
    Product = ['Concerned about inflation','Concerned about delivery times','Identifies sourcing as #1 frustration','Looks for new suppliers at least once per month','Concerned about price transparency', 'Frequently skips price comparisons']
    Quantity = [5,5,4,3,5,2]

    plt.style.use('ggplot')

    plt.barh(Product,Quantity)
    plt.title('Survey of artisan small business soapmakers from around the U.S. (n=5)')
    #plt.ylabel('Product')
    plt.xlabel('Number agree')
    save('survey.png')
    plt.show()
    return 

def save(filename):
    #plt.subplots_adjust(bottom=0.15)
    plt.savefig(filename, dpi=1200, bbox_inches="tight")

if __name__ == '__main__':
    print("hi")
    # ecommerce_scatter()
    # amazon_scatter()
    # superimposed_scatter()
    # declining_functionality()
    usersurvey()